from odoo import fields, models


class CareNote(models.Model):
    _name = "care.note"
    _description = "Care note"

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
