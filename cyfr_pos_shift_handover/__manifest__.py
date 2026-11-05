{
    "name": "POS Shift Handover",
    "summary": "Operational tasks between POS sessions on the same register",
    "version": "19.0.1.0.1",
    "category": "Sales/Point of Sale",
    "author": "Digicyfr (CYFR Sp. z o.o.)",
    "website": "https://digicyfr.com",
    "license": "LGPL-3",
    "images": ["static/description/main_screenshot.png"],
    "depends": ["point_of_sale"],
    "data": [
        "security/handover_rules.xml",
        "security/ir.model.access.csv",
        "views/handover_views.xml",
    ],
    "demo": ["demo/handover_demo.xml"],
    "installable": True,
    "application": False,
}
