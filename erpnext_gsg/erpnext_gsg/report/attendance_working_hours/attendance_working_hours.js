// Copyright (c) 2023, Rola Nabulsi and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Attendance Working Hours"] = {
	"filters": [
	    {'fieldname': 'attendance_date', 'label':'Attendance Date' , 'fieldtype':'Date'  },
        {'fieldname': 'employee', 'label':'Emplyee Name' , 'fieldtype':'Link' , 'options':'Employee' },
		{'fieldname': 'department', 'label': 'Department  ', 'fieldtype': 'Link','options':'Department'},

	]
};
