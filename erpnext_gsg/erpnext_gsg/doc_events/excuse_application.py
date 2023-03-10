import frappe
from frappe.utils import time_diff_in_hours, getdate


def validate(doc,method):
    if doc.from_time > doc.to_time:
        frappe.throw("To Time cannot be before from Time")

    get_hours = time_diff_in_hours(doc.to_time, doc.from_time)
    doc.hours = get_hours

    if doc.excuse_hours_alowed < doc.hours:
        frappe.throw("You Are Exceeded Limit Excuse Hours")