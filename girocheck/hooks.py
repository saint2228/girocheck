# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "girocheck"
app_title = "Giro Check"
app_publisher = "ridhosribumi"
app_description = "App for manage giro and check"
app_icon = "octicon octicon-plus"
app_color = "#FEE771"
app_email = "develop@ridhosribumi.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/girocheck/css/girocheck.css"
# app_include_js = "/assets/girocheck/js/girocheck.js"

# include js, css files in header of web template
# web_include_css = "/assets/girocheck/css/girocheck.css"
# web_include_js = "/assets/girocheck/js/girocheck.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "girocheck.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "girocheck.install.before_install"
# after_install = "girocheck.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "girocheck.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }
doc_events = {
    "Payment Entry": {
        # "on_change": [
        #     "preorder.preorder.operan.update_quotation"
        # ],
        "on_submit": [
            "girocheck.reference.submit_payment_entry"
            # "preorder.preorder.operan.submit_quotation_2",
            # "preorder.preorder.operan.submit_quotation_3",
            # "preorder.preorder.operan.submit_quotation_4"
        ],
        "on_cancel": [
            "girocheck.reference.cancel_payment_entry"
            # "preorder.preorder.operan.submit_quotation_2",
            # "preorder.preorder.operan.submit_quotation_3",
            # "preorder.preorder.operan.submit_quotation_4"
        ],
        # "before_cancel": [
        #     "preorder.preorder.operan.cancel_quotation",
        #     "preorder.preorder.operan.cancel_quotation_2"
        # ]
    },
}


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"girocheck.tasks.all"
# 	],
# 	"daily": [
# 		"girocheck.tasks.daily"
# 	],
# 	"hourly": [
# 		"girocheck.tasks.hourly"
# 	],
# 	"weekly": [
# 		"girocheck.tasks.weekly"
# 	]
# 	"monthly": [
# 		"girocheck.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "girocheck.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "girocheck.event.get_events"
# }
