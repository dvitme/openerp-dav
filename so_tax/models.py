# -*- coding: utf-8 -*-

from openerp import models, fields, api

class SaleOrder(models.Model):
	_inherit = 'sale.order'

	tax_ids = fields.Many2many(
		'account.tax',
		string='Taxes',
		help='Note: this will be put on all Order Lines below.',
		states={'draft': [('readonly', False)]},
		domain=['|', ('active', '=', False), ('active', '=', True)]
	)

	@api.onchange("tax_ids")
	def onchange_tax_ids(self):
		for o in self.order_line:
			o.tax_id = self.tax_ids


class AccountInvoice(models.Model):
	_inherit = 'account.invoice'

	tax_ids = fields.Many2many(
		'account.tax',
		string='Taxes',
		help='Note: this will be put on all Invoice Lines below.',
		states={'draft': [('readonly', False)]},
		domain=[('parent_id', '=', False), '|', ('active', '=', False), ('active', '=', True)]
	)

	@api.onchange("tax_ids")
	def onchange_tax_ids(self):
		for o in self.invoice_line:
			o.invoice_line_tax_id = self.tax_ids