# -*- coding: utf-8 -*-
# Copyright 2017 Ainara Galdona - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "MRP - BoM version extension",
    "version": "8.0.1.0.0",
    "license": "AGPL-3",
    "author": "AvanzOSC,",
    "website": "http://www.avanzosc.es",
    "contributors": [
        "Ainara Galdona <ainaragaldona@avanzosc.es>",
        "Ana Juaristi <anajuaristi@avanzosc.es>",
        ],
    "category": "Manufacturing",
    "depends": [
        "mrp_bom_version",
    ],
    "data": [
        "data/mrp_bom_version_extension_data.xml",
        "views/res_config_view.xml",
        "views/mrp_bom_view.xml",
    ],
    "installable": True,
}
