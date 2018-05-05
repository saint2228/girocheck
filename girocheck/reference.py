from __future__ import unicode_literals
import frappe, math
from frappe.utils import nowdate, cstr, flt, now, getdate, add_months
from frappe import msgprint, _
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
from frappe.model.naming import make_autoname
from dateutil import parser
from num2words import num2words

def submit_payment_entry(doc, method):
    mother_guardian = get_mapped_doc("Payment Entry", doc.name,
        {"Payment Entry": {
            "doctype": "Giro Check In",
            "field_map": {
                "party": "customer",
                "name": "payment_entry"
            }
        }}, ignore_permissions=True)
    mother_guardian.save()

def cancel_payment_entry(doc, method):
    pick = frappe.db.sql("""select `name` from `tabGiro Check In` where docstatus = '0' and payment_entry = %s""", doc.name, as_dict=1)
    for picking in pick:
        cancel_picking = frappe.get_doc("Giro Check In", picking.name)
        # cancel_picking.cancel()
        cancel_picking.delete()
