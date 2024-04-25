# -*- coding: utf-8 -*-
{   
    'name': "Rapports CNAS - Algérie",
    'summary': """ Implémentation des rapports CNAS """,

    'version'       : "16.0.1.0",
    'category'      : "Human Resources/Employees",

    "contributors": [
        "1 <Sofiane AMRAOUI >",
        "2 <Abdelhakim ABOURA >",
        "3 <Fatima MESSADI >",
        "4 <Yassamine CHENAFA >",
        "5 <Chems Eddine SAHININE >",
    ],

    'sequence': 1,

    'company'       : 'Elosys',
    'author'        : 'Elosys',
    'maintainer'    : 'Elosys',

    'website': "https://www.elosys.net/",
    'support' : "support@elosys.net",
    'live_test_url' : "https://www.elosys.net/shop",

    'depends': [
        'base',
        'eloapps_hr_payroll_dz',
    ],

    'data': [
        'security/ir.model.access.csv',
        'security/rules.xml',
        'wizards/employee_list.xml',
        
        'reports/custom_header.xml',
        'reports/report_template.xml',
        'reports/report.xml',
        'reports/report_das.xml',
        'reports/format_report.xml',
        'views/declaration_cotisation.xml',
        'views/declaration_das.xml',
        'views/lot_declaration_cotisation.xml',
        'views/res_company.xml',
        'views/res_partner.xml',
        'views/activity_code.xml',
        'views/menu_item.xml',
    ],

    'license'       : "LGPL-3",
    'price'         : "180",
    'currency'      : 'Eur',

    'installable': True,
    'auto_install': False,
    "application": True,


}
