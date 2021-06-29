# -*- coding: utf-8 -*-
{
    'name': "do_luarprop",

    'summary': """
        Modul untuk customisasi bengkel""",

    'description': """
        + Tambah Field Jumlah Kembali
        + Tambah Field Tanggal Kembali
        + Tambah Field status kirim (kirim, kembali , done)
    """,

    'author': "Satusoft",
    'website': "https://satusoft.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Addon',
    'version': '2',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'stock',
                'purchase',
                'account',],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/stock.xml',

    ],
    # only loaded in demonstration mode

}