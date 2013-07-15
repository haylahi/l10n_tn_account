# -*- coding: utf-8 -*-
##############################################################################
#
#    account_group_invoice_lines module for OpenERP, Change method to group invoice lines in account
#    Copyright (C) 2013 CREATIVE PLUS)
#              Haythem Lahmadi <cplus.contact@gmail.com>
#
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

class account_entries_report(osv.osv):
    _inherit  = 'account.entries.report'
    _columns = {
        'debit': fields.float('Debit', digits_compute=dp.get_precision('Account'), readonly=True),
        'credit': fields.float('Credit', digits_compute=dp.get_precision('Account'), readonly=True),
        'balance': fields.float('Balance', digits_compute=dp.get_precision('Account'), readonly=True),
        }
        
class account_invoice_report(osv.osv):
    _inherit = 'account.invoice.report'
    _columns = {
        'price_total': fields.float('Total Without Tax', digits_compute=dp.get_precision('Account'), readonly=True),
        }
        
class account_treasury_report(osv.osv):
    _inherit = 'account.treasury.report'
    _columns = {
        'debit': fields.float('Debit', digits_compute=dp.get_precision('Account'), readonly=True),
        'credit': fields.float('Credit', digits_compute=dp.get_precision('Account'), readonly=True),
        'balance': fields.float('Balance', digits_compute=dp.get_precision('Account'), readonly=True),
        }
    
