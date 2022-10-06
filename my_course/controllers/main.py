from odoo import http
from odoo.http import request


class Main(http.Controller):
    @http.request('my_course/courses', type='http', auth='none')
    def course(self):
        courses = request.env['education.course'].sudo().search([])
        html_result = '<html><body><ul>'
        for course in courses:
            html_result += "<li> %s </li>" %course.name
        html_result += '</ul></body></html>'
        return html_result
