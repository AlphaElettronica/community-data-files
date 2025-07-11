from odoo import fields, models, api, _

class SpecialDispositions(models.Model):
    _name = 'product.special.dispositions'
    _description = 'Description'

    name = fields.Char(required=True)

    def get_full_name(self):
        self.ensure_one()
        return _('Special disposition') + ' ' + self.name
