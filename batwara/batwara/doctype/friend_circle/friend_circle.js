// Copyright (c) 2025, mohtashim and contributors
// For license information, please see license.txt

frappe.ui.form.on("Friend Circle", {
	refresh(frm) {
        frm.set_query("user",()=>{
            return{
                filters:{
                    "ignore_user_type":1
                }
            }
        })

	},
});


frappe.ui.form.on("Friend Circle", {
    refresh(frm) {
        frm.fields_dict["friends"].grid.get_field("user").get_query = function(doc, cdt, cdn) {
            return {
                filters: {
                    "ignore_user_type": 1
                }
            };
        };
    }
});
