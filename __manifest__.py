{
    'name':'Real Estate Advertisement',
    'summary': 'Real Estate Advertisement',
    'description': 'Real Estate Advertisement',
    'author': 'M Z Masi',
    'category': 'Real Estate',
    'version': '1.0',
    'installable': True,
    'application': True,
    'depends':[
        'base'
    ],

    'data':[
            'security/ir.model.access.csv',
            'views/estate_property_views.xml',
            'views/estate_menus.xml',
            'views/estate_property_type_views.xml',
            'views/estate_property_tag_views.xml',
            'views/estate_property_show_offer_list_views.xml',
            'views/res_user_views.xml'
        ]
}