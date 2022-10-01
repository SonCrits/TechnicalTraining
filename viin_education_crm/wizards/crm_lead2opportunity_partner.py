from odoo import fields, models, api


class Lead2OpportunityPartner(models.TransientModel):
    _inherit = 'crm.lead2opportunity.partner'
    
    @api.model
    def default_get(self, fields):
        res = super(Lead2OpportunityPartner, self).default_get(fields)
        if self._context.get('active_model') != 'crm.lead' or not self._context.get('active_id'):
            return res
        lead = self.env['crm.lead'].browse(self._context.get('active_id'))
        if 'action' in fields and not res.get('action'):
            if lead.student_id:
                res['action'] = 'existing_student' 
            elif lead.contact_name:
                res['action'] = 'create_student'
            else:
                res['action'] = 'nothing'
        if 'student_id' in fields:
            res['student_id'] = lead.student_id.id if lead.student_id else False
            
        if 'parent_action' in fields and not res.get('parent_action'):
            if lead.parent_id:
                res['parent_action'] = 'exist' 
            elif lead.parent_name:
                res['parent_action'] = 'create'
            else:
                res['parent_action'] = 'nothing'
        if 'parent_id' in fields:
            res['parent_id'] = lead.parent_id.id if lead.parent_id else False
            
        return res
    
    action = fields.Selection(selection_add=[('create_student', 'Create a new student'), ('existing_student', 'Link to an existing student'), ('create',)])
    parent_action = fields.Selection([
        ('create', 'Create a new parent'),
        ('exist', 'Link to an existing parent'),
        ('nothing', 'Do not link to a parent')
    ], string='Related Parent')
    parent_id = fields.Many2one('res.partner', string='Parent', compute='_compute_parent_id', store=True, readonly=False)
    student_id = fields.Many2one('education.student', string='Student', compute='_compute_student_id', store=True, readonly=False)
    relationship_id = fields.Many2one('education.relationship', string='Relationship', help="Relation between parent and student")
    show_relationship = fields.Boolean(string='Show Relationship', compute='_compute_show_relationship',
        help="Technical field computed to hide or show relationship based on parent and student")
    
    @api.depends('parent_action')
    def _compute_parent_id(self):
        for r in self:
            if r.parent_action != 'exist':
                r.parent_id = False
            else:
                r.parent_id = self._find_matching_parent()
                
    @api.depends('action')
    def _compute_student_id(self):
        for r in self:
            if r.action != 'existing_student':
                r.student_id = False
            else:
                r.student_id = self._find_matching_student()
    
    @api.depends('action', 'parent_action', 'parent_id', 'student_id')
    def _compute_show_relationship(self):
        for r in self:
            show_relationship = True
            if r.action not in ['create_student', 'existing_student'] or r.parent_action not in ['create', 'exist']:
                show_relationship = False
                r.relationship_id = False
            elif r.parent_id and r.student_id and r.student_id.parent_ids and r.student_id.parent_ids.filtered(lambda p: p.parent_id.id == r.parent_id.id):
                show_relationship = False
                r.relationship_id = False
            r.show_relationship = show_relationship
    
    def _convert_and_allocate(self, leads, user_ids, team_id=False):
        self.ensure_one()
        res = False
        if self.action in ('create_student', 'existing_student') or self.parent_action != 'nothing':
            for lead in leads:
                if lead.active:
                    # Create student or update student
                    if self.action == 'create_student':
                        student = lead._create_student()
                        lead.partner_id = student.partner_id
                        lead.student_id = student
                    elif self.action == 'existing_student':
                        lead.partner_id = self.student_id.partner_id
                        lead.student_id = self.student_id
                    # Create parent or update parent exist
                    if self.parent_action == 'create':
                        parent = lead._create_lead_parent()
                        lead.parent_id = parent
                    elif self.parent_action == 'exist':
                        lead.parent_id = self.parent_id
                          
                lead.convert_opportunity(lead.partner_id.id, [], False)
                 
            leads_to_allocate = leads
            if not self.force_assignment:
                leads_to_allocate = leads_to_allocate.filtered(lambda lead: not lead.user_id)
     
            if user_ids:
                leads_to_allocate.handle_salesmen_assignment(user_ids, team_id=team_id)
        else:
            res = super(Lead2OpportunityPartner, self)._convert_and_allocate(leads, user_ids, team_id)
        leads._add_student_parent_relationship(self.relationship_id)
        return res

    @api.model
    def _find_matching_student(self):
        """ Try to find a matching student regarding the active model data
            :return int student_id if any, False otherwise
        """
        # active model has to be a lead
        if self._context.get('active_model') != 'crm.lead' or not self._context.get('active_id'):
            return False
        
        lead = self.env['crm.lead'].browse(self._context.get('active_id'))
        
        if lead.student_id:  # a student is set already
            return lead.student_id
        
        return False
    
    @api.model
    def _find_matching_parent(self):
        """ Try to find a matching parent regarding the active model data
            :return int parent_id if any, False otherwise
        """
        # active model has to be a lead
        if self._context.get('active_model') != 'crm.lead' or not self._context.get('active_id'):
            return False
        
        lead = self.env['crm.lead'].browse(self._context.get('active_id'))
        
        if lead.parent_id:  # a parent is set already
            return lead.parent_id
        
        return False
