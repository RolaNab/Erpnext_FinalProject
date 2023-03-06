import frappe

def on_submit(doc, method):
    create_stock_entry(doc)

def create_stock_entry(doc):
    if doc.material_request_type == 'Material Issue':

        material_request_type = doc.material_request_type
        material_from_warehouse = doc.set_warehouse

        stock_entry_doc= frappe.new_doc("Stock Entry")

        stock_entry_doc.stock_entry_type = material_request_type
        stock_entry_doc.from_warehouse = material_from_warehouse

        for material_item in doc.items:
            stock_entry_doc.append("items", {
                "item_code":material_item.item_code,
                "qty": material_item.qty

        })
    stock_entry_doc.insert(ignore_permissions=True)
    stock_entry_doc.submit()
