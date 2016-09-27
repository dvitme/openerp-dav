# -*- coding: utf-8 -*-
{
    'name': 'Sale Order Tax',
    'summary': 'Sale Order Tax',
    'description': """
    This module adds a tax field whose value put in every product record.
    This is also being made in customer invoice.
     """,
    'version': '8.0.1.0',
    'category': 'Accounting',
    'author': 'DVIT.me',
    'website': 'http://dvit.me',
    'license': 'AGPL-3',
    'depends': [
        'account','sale'
    ],
    'data': ['templates.xml'],
    'installable': True,
    'auto_install': False,
    'application': False,

}