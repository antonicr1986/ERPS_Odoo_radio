# -*- coding: utf-8 -*-

from odoo import models, fields, api


class section(models.Model):
     _name = 'radio.section'
     _description = 'Radio sections'

     name = fields.Char('Name', required=True)
     description = fields.Char('Description')
     hours = fields.Float('Hours', required=True)
     participants = fields.Many2many('hr.employee', string='Employees')

class program(models.Model):
     _name = 'radio.program'
     _description = 'Radio programs'

     name = fields.Char('Name', required=True)
     duration = fields.Float('Duration', compute='calculo_durada')
     sections = fields.Many2many('radio.section', string='Sections')

     @api.depends('sections.hours')
     def calculo_durada(self):
          for program in self:
               duration_total = sum(program.sections.mapped('hours'))
               program.duration = duration_total