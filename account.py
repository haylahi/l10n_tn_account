# -*- coding: utf-8 -*-
##############################################################################
#
#    account_group_invoice_lines module for OpenERP, Change method to group invoice lines in account
#    Copyright (C) 2013 CREATIVE PLUS)
#              Haythem Lahmadi <cplus.contact@gmail.com>
#
#    This file is a part of account_group_invoice_lines
#
#    account_group_invoice_lines is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    account_group_invoice_lines is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from openerp.osv import fields, osv, orm
from openerp.tools.translate import _
import openerp.addons.decimal_precision as dp


class account_tax_code(osv.osv):
    _inherit = 'account.tax.code'
    
    def _sum(self, cr, uid, ids, name, args, context, where ='', where_params=()):
    	return super(account_tax_code, self)._sum(cr, uid, ids, name, args, context,
                where=where, where_params=where_params)
        
    def _sum_year(self, cr, uid, ids, name, args, context=None):
        return super(account_tax_code, self)._sum_year(cr, uid, ids, name, args, context=context)
        
    def _sum_period(self, cr, uid, ids, name, args, context):
        return super(account_tax_code, self)._sum_period(cr, uid, ids, name, args, context=context)
    _columns = {
        'sum': fields.function(_sum_year, digits_compute=dp.get_precision('Account'), string="Year Sum"),
        'sum_period': fields.function(_sum_period, digits_compute=dp.get_precision('Account'), string="Period Sum"),
    }
