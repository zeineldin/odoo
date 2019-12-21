# -*- coding: utf-8 -*-
""" Partner Sequence Tests """

from odoo.tests.common import TransactionCase


class PartnerSequenceTest(TransactionCase):
    """PartnerSequence Tests"""

    def _create_partner(self, values=None):
        """Create partner and return its object."""
        if not values:
            values = {
                'name': 'Partner Sample #1',
            }
        return self.env['res.partner'].sudo().create(values)

    def test_00_partner_sequence(self):
        """ Test-Scenario: Partner Sequence. """
        partner = self._create_partner()
        self.assertTrue(partner.sequence,
                        'Partner Sequence is created successfully.')
        partner = self._create_partner({
            'name': 'Partner Sample #1',
            'customer': False
        })
        self.assertFalse(partner.sequence,
                         'Sequence is not generated contact is not a partner.')
        partner.customer = True
        self.assertTrue(partner.sequence,
                        'Partner Sequence is created when partner '
                        'is changed to customer')

    def test_01_search_by_sequence(self):
        """ Test-Scenario: Partner Search by Sequence. """
        partner = self._create_partner()
        sequence = partner.sequence
        res = self.env['res.partner'].name_search(name=sequence)
        self.assertEqual(res, partner.name_get(),
                         'Get partner by sequence successfully')
