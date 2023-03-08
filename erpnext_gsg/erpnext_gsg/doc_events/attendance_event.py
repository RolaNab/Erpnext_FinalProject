from frappe.utils import time_diff_in_hours



def validate_attendance(doc,method):
    if not doc.check_in or not doc.check_out:
        doc.work_hours = 0
    else:
        get_hours = time_diff_in_hours(doc.check_out, doc.check_in)
        doc.work_hours = get_hours
