# -*- coding: utf-8 -*-
# Copyright (c) 2019, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class LibraryMember(Document):
		def validate(self):
			frappe.msgprint("Hiii")
   # a=frappe.db.sql("""SELECT to_date (UPDAT)FROM tabLibrary Membership WHERE 'Libarary Membership' WHERE 'Library Member';""")

