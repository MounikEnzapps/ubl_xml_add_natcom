# -*- coding: utf-8 -*-
{
    'name': "UBL TEMPLATE ADDING",
    'author':
        'ENZAPPS',
    'summary': """
This module is for printing E-Invoice report for Masar Arabia.
""",

    'description': """
        This module is for printing E-Invoice report for Masar Arabia.
    """,
    'website': "",
    'category': 'base',
    'version': '12.0',
    'depends': ['base','account','uom_unece','base_unece','account_tax_unece','base_vat_sanitized','onchange_helper','base_iban','base_bank_from_iban','base_business_document_import','account_invoice_import','base_ubl_payment','account_invoice_import_ubl','account_invoice_ubl','sale','purchase','stock','natcom_jan_pdf','natcom_dec_last','credit_report_natcoms','natcom_jan_pdf'],
    'data': [
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
}
