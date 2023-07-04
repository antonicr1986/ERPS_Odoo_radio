from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    show_sections = fields.Many2many('radio.section',string='Show sections')