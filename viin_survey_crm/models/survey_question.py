from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SurveyQuestion(models.Model):
    _inherit = 'survey.question'
    
    lead_field_id = fields.Many2one('ir.model.fields', string='Field of Lead', domain="[('id','in',lead_field_ids)]", help="The field of Lead "
                               "that will be generated from the answer of this question")
    lead_field_ids = fields.Many2many('ir.model.fields', string='Fields', compute='_compute_lead_field_ids')

# Todo: custom after other modules are upgraded
    # @api.constrains('lead_field_id', 'question_type')
    # def _check_lead_field_id(self):
        # for r in self:
            # if r.question_type == 'text_box' and r.lead_field_id.ttype != 'text':
                # raise ValidationError(_("You must select the Field with the type is 'text' when the question type is 'Multiple Lines Text Box'!"))
            # if r.question_type == 'char_box' and r.lead_field_id.ttype not in ('char', 'text'):
                # raise ValidationError(_("You must select the Field with the type is 'char' or 'text' when the question type is 'Single Line Text Box'!"))
            # if r.question_type == 'numerical_box' and r.lead_field_id.ttype not in ('float', 'integer'):
                # raise ValidationError(_("You must select the Field with the type is 'float' or 'integer' when the question type is 'Numerical Value'!"))
            # if r.question_type == 'date' and r.lead_field_id.ttype != 'date':
                # raise ValidationError(_("You must select the Field with the type is 'date' when the question type is 'Date'!"))
            # if r.question_type == 'datetime' and r.lead_field_id.ttype != 'datetime':
                # raise ValidationError(_("You must select the Field with the type is 'datetime' when the question type is 'Datetime'!"))
            # if r.question_type == 'simple_choice' and r.lead_field_id.ttype not in ('char', 'text'):
                # raise ValidationError(_("You must select the Field with the type is 'char' or 'text' when the question type is 'Multiple choice: only one answer'!"))

    @api.depends('question_type')
    def _compute_lead_field_ids(self):
        IrModelFields = self.env['ir.model.fields']
        for r in self:
            domain = []
            if r.question_type == 'text_box':
                domain = [('ttype', '=', 'text')]
            elif r.question_type == 'char_box':
                domain = [('ttype', 'in', ('char', 'text'))]
            elif r.question_type == 'numerical_box':
                domain = [('ttype', 'in', ('float', 'integer'))]
            elif r.question_type == 'date':
                domain = [('ttype', '=', 'date')]
            elif r.question_type == 'datetime':
                domain = [('ttype', '=', 'datetime')]
            elif r.question_type == 'simple_choice':
                domain = [('ttype', 'in', ('char', 'text'))]
                
            domain += [('model_id.model','=','crm.lead')]
            r.lead_field_ids = IrModelFields.search(domain)
