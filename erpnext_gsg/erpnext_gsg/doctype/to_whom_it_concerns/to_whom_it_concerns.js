// Copyright (c) 2023, Rola Nabulsi and contributors
// For license information, please see license.txt

frappe.ui.form.on('To Whom It Concerns', {
    employee:function(frm){
    frm.trigger('get_emloyee_salary')
    },

    get_emloyee_salary : function(frm){
    if(!frm.doc.employee ){
    return;
    }
    frappe.call({
    method:'erpnext_gsg.erpnext_gsg.doctype.to_whom_it_concerns.to_whom_it_concerns.get_emloyee_salary',
    args:{
    employee: frm.doc.employee
    },
    callback: (r) => {
    frm.doc.salary = r.message;
    frm.refresh()
    },
    })
    },
});
