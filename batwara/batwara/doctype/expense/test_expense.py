# Copyright (c) 2025, mohtashim and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestExpense(FrappeTestCase):
	def test_split_calculation(self):
		test_expense = frappe.get_doc({
			"doctype":"Expense",
			"paid_by":"test@gmail.com",
		}).insert()
