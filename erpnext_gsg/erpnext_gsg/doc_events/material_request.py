import frappe

def on_submit(doc, method):
    if doc.material_request_type == 'Material Issue':
        # material_request_type = doc.material_request_type
        # material_target_warehouse = doc.set_warehouse
        # stock_entry_doc= frappe.new_doc("Stock Entry")
        # stock_entry_doc.stock_entry_type = material_request_type
        # stock_entry_doc.from_warehouse = material_target_warehouse
        # stock_entry_doc.material_request = doc.name
        # for material_item in doc.items:
        #     stock_entry_doc.append("items", {
        #         "item_code":material_item.item_code,
        #         "qty": material_item.qty,
        #         })
        from erpnext.stock.doctype.material_request.material_request import make_stock_entry
        stock_entry = make_stock_entry(doc.name)
                # stock_entry_doc.material_request = doc.name
        stock_entry.save(ignore_permissions=True)
        stock_entry.submit()




