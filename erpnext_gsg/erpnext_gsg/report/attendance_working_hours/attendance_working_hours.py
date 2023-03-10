# Copyright (c) 2023, Rola Nabulsi and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import time_diff_in_hours


def execute(filters=None):
	columns, data = [], []
	data = get_all_value(filters)
	columns = get_columns()
	return columns, data

def get_all_value(filters):
	att_work_hours = frappe.db.get_all('Attendance' ,
				['employee_name','attendance_date','check_in', 'check_out', 'work_hours','name'],filters = filters)
	for row in att_work_hours:
		row.reference = f"<a target='_blank' href='/app/attendance/{row.name}'  title='{row.name}' data-doctype='Attendance' data-name='{row.name}'>View Attendance</a>"
	return att_work_hours

def get_columns():
	columns = [
		{'fieldname': 'employee_name', 'label': 'Emplyee Name', 'fieldtype': 'Link', 'options': 'Employee'},
		{'fieldname': 'attendance_date', 'label': 'Attendance Date', 'fieldtype': 'Date'},
		{'fieldname': 'check_in', 'label': 'Check in', 'fieldtype': 'Time'},
		{'fieldname': 'check_out', 'label': 'Check Out', 'fieldtype': 'Time'},
		{'fieldname': 'work_hours', 'label': 'Work Hours', 'fieldtype': 'float'},
		{"label": frappe._("Attendance Reference"), "fieldname": "reference", "fieldtype": "HTML"}]
	return columns

# , 'work_hours','late_hours'