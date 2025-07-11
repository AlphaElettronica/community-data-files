# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ProductProduct(models.Model):
    _inherit = "product.product"

    full_class_name = fields.Char()
    special_disposition_id = fields.Many2one('product.special.dispositions')

    @api.onchange("is_dangerous")
    def _ochange_is_dangerous(self):
        self.is_dangerous_good = self.is_dangerous

    @api.onchange('is_dangerous_waste', 'un_ref', 'nag', 'label_first', 'label_second', 'label_third',
                  'packaging_group', 'tunnel_code', 'envir_hazardous', 'special_disposition_id')
    def onchange_get_full_class_name(self):
        fcn = self.get_full_class_name()
        self.full_class_name = fcn

    def get_full_class_name(self):
        class_name = _("UN")

        if self.is_dangerous_waste:
            class_name += _(" WASTE")
        class_name += " {}, {}".format(self.un_ref.name, self.un_ref.description)

        if self.nag:
            class_name += _(", N.A.G ({})").format(self.nag)

        if self.dangerous_class_id:
            class_number = self.dangerous_class_id.code.replace('ADR_', '')
            class_name += ", {}".format(class_number)

        # if self.label_first:
        #     class_name += ", {}".format(self._get_name_from_selection("label_first"))
        # if self.label_second and self.label_third:
        #     class_name += ", ({}, {})".format(
        #         self._get_name_from_selection("label_second"),
        #         self._get_name_from_selection("label_third"),
        #     )
        # elif self.label_second:
        #     class_name += ", ({})".format(self._get_name_from_selection("label_second"))

        if self.packaging_group:
            class_name += ", {}".format(
                self._get_name_from_selection("packaging_group")
            )

        if self.tunnel_code:
            class_name += ", {}".format(self._get_name_from_selection("tunnel_code"))

        if self.envir_hazardous == "yes":
            class_name += ", {}".format(_("Environmentally hazardous"))

        if self.special_disposition_id:
            class_name += ", {}".format(self.special_disposition_id.get_full_name())

        return class_name