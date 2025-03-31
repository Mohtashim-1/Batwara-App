# Copyright (c) 2025, mohtashim and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestExpense(FrappeTestCase):
	def test_split_calculation(self):
		test_expense = frappe.get_doc({
			"doctype":"Expense",
			"paid_by":"test@gmail.com",
			"description":"Test",
			"amount":200,
			{
				"user":"test@gmail.com"
			}
		}).insert()

		self.assertEqual(test_expense.expense_split[0].amount, 100)
		self.assertEqual(test_expense.expense_split[0].amount, 200)
