import frappe
from frappe.utils import time_diff_in_hours, getdate


def validate(doc,method):
    if doc.from_time > doc.to_time:
        frappe.throw("To Time cannot be before from Time")

    # doc.new_excuse_hours = doc.excuse_hours_alowed
    # set_value = frappe.db.set_value("Employee Excuse application",doc.new_excuse_hours,str(doc.excuse_hours_alowed))
    # doc.new_excuse_hours = set_value
    get_hours = time_diff_in_hours(doc.to_time, doc.from_time)
    doc.hours = get_hours

    after_excuse = doc.excuse_hours_alowed - doc.hours
    doc.new_excuse_hours = after_excuse
    # doc.excuse_hours_alowed = after_excuse
    # frappe.db.set_value("Employee Excuse application",doc.employee_name,doc.excuse_hours_alowed,after_excuse)
    if not doc.excuse_hours_alowed:
        frappe.throw("There is No  Excuse Hours available in your department")

        if str(doc.new_excuse_hours) < str(doc.hours):
            frappe.throw("You Are Exceeded Limit Excuse Hours")