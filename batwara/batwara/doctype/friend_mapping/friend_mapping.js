// Copyright (c) 2025, mohtashim and contributors
// For license information, please see license.txt

frappe.ui.form.on("Friend Mapping", {
	refresh(frm) {
        frm.set_query("a",()=>{
            return{
                filters:{
                    "ignore_user_type":1
                }
            }
        }),
        frm.set_query("b",()=>{
            return{
                filters:{
                    "ignore_user_type":1
                }
            }
        })
	},
});
