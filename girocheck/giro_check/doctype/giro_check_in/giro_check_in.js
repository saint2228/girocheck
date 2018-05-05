// Copyright (c) 2018, ridhosribumi and contributors
// For license information, please see license.txt

frappe.ui.form.on('Giro Check In', {
	setup: function(frm){
		// frm.trigger("set_query_for_cost_center");
		frm.trigger("set_query_for_account")
		// frm.add_fetch("company", "cost_center", "cost_center");
		// frm.add_fetch("company", "default_cash_account", "account");
		frm.set_query("account", "deductions", function() {
			return {
				filters: {
					"is_group": 0,
					"company": frm.doc.company
				}
			}
		});
	},

	refresh: function(frm) {

	},

	set_query_for_account: function(frm) {
		frm.fields_dict["bank_accept"].get_query = function() {
			return {
				filters: {
					"report_type": "Balance Sheet",
					"account_type": "Bank",
					//"account_type": ["in",["Bank","Cash"]],
					"is_group":0
				}
			};
		};
	},
});

// frappe.ui.form.on('Giro Check In Deduction', {
// 	amount: function(frm) {
// 		frm.events.set_unallocated_amount(frm);
// 	},
//
// 	deductions_remove: function(frm) {
// 		frm.events.set_unallocated_amount(frm);
// 	}
// })
