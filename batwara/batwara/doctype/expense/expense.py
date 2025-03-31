# Copyright (c) 2025, mohtashim and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Expense(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from batwara.batwara.doctype.expense_split.expense_split import ExpenseSplit
		from frappe.types import DF

		amended_from: DF.Link | None
		amount: DF.Currency
		currency: DF.Link
		date: DF.Date | None
		description: DF.Data
		expense_split: DF.Table[ExpenseSplit]
		notes: DF.SmallText | None
		paid_by: DF.Link | None
		split_method: DF.Literal["Equally", "Manual"]
	# end: auto-generated types
	# pass

	def validate(self):
		self.apply_split()

	def apply_split(self):
		if self.split_method == "Equally": 
			self.calculate_equal_splits()
		else:
			# Manual
			pass

	def calculate_equal_splits(self):
		num_splits = len(self.expense_split)
		split_amount = self.amount / num_splits

		for s in self.expense_split:
			s.amount = split_amount

	def on_submit(self):
		self.create_ledger_entry()

	def create_ledger_entry(self):
		for split in self.expense_split:
			if split.user == self.paid_by:
				continue
			
			le = frappe.new_doc("Split Ledger Entry")
			le.amount = split.amount
			le.currency = split.currency
			le.credit_user = split.user
			le.debit_user = self.paid_by
			le.expense = self.name
			le.insert().submit()


