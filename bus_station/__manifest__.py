{
    'name': "Bus Station",
    'summary': "Bus Station",

    'author': "Kseniia Voitko",

    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '15.0.1.0.0',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/bus_station_menus.xml',
        'views/res_partner_views.xml',
        'views/bus_route_views.xml',
        'views/bus_station_views.xml',
        'views/bus_timetable_views.xml',
        'views/bus_transport_views.xml',
        'wizard/create_timetable_wizard_views.xml',
        'report/bus_timetable_reports_templates.xml',
        'report/bus_timetable_report.xml',
    ],
    'demo': [
        'data/bus_transport_demo.xml',
        'data/bus_station_demo.xml',
        'data/bus_route_demo.xml',
        'data/res_partner_demo.xml',
        'data/bus_timetable_demo.xml',
    ],

}
