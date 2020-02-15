# -*- coding: utf-8 -*-
{
    'name': 'Whatsapp Odoo Pro MFH',
    'version': '13.0.1.0.0',
    'summary': 'Send Whatsapp from Odoo.',
    'description': 'Send Whatsapp from Odoo.',
    'category': 'Extra Tools',
    'author': 'Ynext SpA',
    'maintainer': 'Ynext SpA',
    'company': 'Ynext SpA',
    'website': 'https://www.ynext.cl',
    'depends': [
        'base',
        ],
    'data': [
        'views/view.xml',
        'views/res_company.xml',
        'wizard/wizard.xml',
    ],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'AGPL-3',
}
