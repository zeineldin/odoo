# -*- coding: utf-8 -*-
""" Base Partner Sequence """

from odoo import api, fields, models


class Partner(models.Model):
    """Res Partner Model
      Assign Each Partner a Unique Sequence Number
    """
    _inherit = 'res.partner'

    sequence = fields.Char()

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        """
            Use the sequence field in the searching for the partner
            in the relationship fields from res.partner
        """
        records = super(Partner, self).name_search(name, args,
                                                   operator=operator,
                                                   limit=limit)
        recs = []
        if name and operator in ('=', 'ilike', '=ilike', 'like', '=like'):
            recs = self.search([('sequence', operator, name)], limit=limit)
            recs = recs.name_get()
        return records + recs

    @api.multi
    def write(self, vals):
        """
        Check if the contact updated to be a customer and if true assign him
        a new sequence number

        :param vals: the updated fields
        :return: if the record updated or not
        :rtype: Boolean (True/ False)
        """
        result = super(Partner, self).write(vals)
        for record in self:
            if vals.get('customer') and not record.sequence:
                record.sequence = self.env['ir.sequence'].\
                    next_by_code('res.partner')
        return result

    @api.model
    def create(self, vals):
        """
        Assign the contact a new sequence number if the contact is a customer

        :param vals: the new record values
        :return: created record
        :rtype: res.partner model
        """
        record = super(Partner, self).create(vals)
        # pylint: disable=no-member
        if record.customer:
            record.sequence = self.env['ir.sequence']. \
                next_by_code('res.partner')
        return record
