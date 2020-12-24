# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Musicians(models.Model):
    _name = 'bands.musicians'
    _description = 'Bands'

    name = fields.Char(string="Musician")
    biography = fields.Html()
    song_ids = fields.One2many('bands.songs', 'musician_id', string="Songs")
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class Songs(models.Model):
    _name = 'bands.songs'

    name = fields.Char(string="Song")
    musician_id = fields.Many2one('bands.musicians', string="Musician")