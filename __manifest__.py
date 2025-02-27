{
    'name':'estate',
    'summary':'Real Estate Advertisment',
    'installable': True,
    'application': True,

    'data':[
        'security/ir.model.access.csv',
        'views/estate_property_show_offer_list_view.xml',
        'views/estate_property_type_view.xml',
        'views/estate_property_tag_view.xml',
        'views/estate_property_views.xml',
        'views/res_user_view.xml',
        'wizard/estate_sold_property_wizard_views.xml',
        'wizard/estate_read_browse_wizard_views.xml',
        'views/estate_menus.xml',
        'report/ir_actions_report.xml',
        'report/ir_actions_report_template_views.xml',
    ],

    "demo": [
        "data/estate_demo.xml"
    ]
}