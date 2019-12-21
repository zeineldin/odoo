# -*- coding: utf-8 -*-
{
    'name': 'Partner Sequence',
    'summary': 'Generate unique sequence for each customer',
    'author': "Omnia Sameh",
    'category': 'base',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'contacts',
    ],
    'data': [
        'data/res_partner_sequence.xml',
        'views/res_partner.xml',
        'views/res_users.xml'
    ],
    'installable': True,
}
