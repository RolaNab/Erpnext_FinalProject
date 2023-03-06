frappe.ui.form.on('Payment Entry', {
	setup: function (frm) {
	 set_field_options("naming_series",["GSG-JV-.YYYY.-"])
	 frm.set_value('naming_series', 'GSG-JV-.YYYY.-')
	}
	});