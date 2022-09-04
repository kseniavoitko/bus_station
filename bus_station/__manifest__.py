{
    'name': "Bus Station",
    'summary': "Bus Station",

    'author': "Kseniia Voitko",

    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '15.0.1.0.0',

    'depends': ['base', 'res.partner'],

    'data': [
        'security/ir.model.access.csv',
        'views/bus_station_menus.xml',
        'views/bus_driver_views.xml',
        'views/bus_route_views.xml',
        'views/bus_station_views.xml',
        # 'views/bus_timetable_views.xml',
        'views/bus_transport_views.xml',
    ],
    'demo': [
        'data/bus_transport_demo.xml',
        'data/bus_station_demo.xml',
    ],

}
