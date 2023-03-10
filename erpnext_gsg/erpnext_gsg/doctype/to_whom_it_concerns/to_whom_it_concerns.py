# Copyright (c) 2023, Rola Nabulsi and contributors
# For license information, please see license.txt
import frappe
# import frappe
from frappe.model.document import Document

class ToWhomItConcerns(Document):
    def validate(self):
        if self.employee :
            emp_sal_slip = frappe.db.sql(""" select gross_pay from `tabSalary Slip`
                where employee = %s """,(self.employee,), as_dict=1)

        if emp_sal_slip:
            self.salary = str(emp_sal_slip[0].gross_pay)

@frappe.whitelist()
def get_emloyee_salary(employee):
    if employee:
        emp_sal_slip = frappe.db.sql(""" select gross_pay from `tabSalary Slip`
            where employee = %s """, (employee,), as_dict=1)

    if emp_sal_slip:
        return str(emp_sal_slip[0].gross_pay)
    else:
        return 0
