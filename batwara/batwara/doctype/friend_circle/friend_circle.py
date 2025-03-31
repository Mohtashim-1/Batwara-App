# Copyright (c) 2025, mohtashim and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FriendCircle(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from batwara.batwara.doctype.user_friend.user_friend import UserFriend
		from frappe.types import DF

		friends: DF.Table[UserFriend]
		user: DF.Link | None
	# end: auto-generated types
	pass
