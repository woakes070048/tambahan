# -*- coding: utf-8 -*-
# Copyright (c) 2015, hendrik and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.model.naming import make_autoname

class Factor(Document):
	def autoname(self):
		self.name = self.template_name
