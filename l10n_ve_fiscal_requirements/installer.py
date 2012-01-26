#!/usr/bin/python
# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#    Copyright (C) OpenERP Venezuela (<http://openerp.com.ve>).
#    All Rights Reserved
###############Credits######################################################
#    Coded by: Vauxoo C.A.           
#    Planified by: Nhomar Hernandez
#    Audited by: Vauxoo C.A.
#############################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
################################################################################
from osv import osv
from osv import fields
from tools.translate import _

class fiscal_requirements_config(osv.osv_memory):
    """
    Fiscal Requirements installer wizard
    """
    _name = 'fiscal.requirements.config'
    _inherit = 'res.config'
    _description= __doc__

    def onchange_update_rif(self, cr, uid, ids, vat):
        context = {'exec_wizard': True, 'vat': vat}
        
        partner_info = self.pool.get('seniat.url').update_rif(cr, uid, ids, context)
        v = {'name': partner_info.get('name'), 'vat_apply': partner_info.get('vat_apply')}
        return {'value': v}

    def execute(self, cr, uid, ids, context=None):
        '''
        In this method I will configure all needs for work out of the box with 
        fiscal requirement and Venezuela Laws
        and update all your partners information.
        '''
        wiz_data = self.browse(cr, uid, ids[0])
        partner = self.pool.get('res.users').browse(cr, uid, uid).company_id.partner_id
        address_obj = self.pool.get('res.partner.address')
        #Data on res partner address - Invoice
        address_ids = address_obj.search(cr,uid,[('partner_id','=',partner.id),('type','like','invoice')])
        if address_ids:
            address_obj.write(cr, uid,address_ids, {'partner_id':partner.id,
                    'type':'invoice',
                    'street':wiz_data.add,
                    'country_id':self.pool.get("res.country").search(cr,uid,[('code','=','VE')])[0]})
        else:
            address_obj.create(cr, uid,{'partner_id':partner.id,
                    'type':'invoice',
                    'street':wiz_data.add,
                    'country_id':self.pool.get("res.country").search(cr,uid,[('code','=','VE')])[0]})
        #Data on res.partner
        data = {'name': wiz_data.name, 'vat': "VE%s" % wiz_data.vat.upper(), 'vat_apply': wiz_data.vat_apply,}
        self.pool.get('res.partner').write(cr, uid, [partner.id], data)

    _columns = {
        'vat': fields.char('VAT', 16, required=True, help='Partner\'s VAT to update the other fields'),
        'name': fields.char('Name', 64, help="The commercial name of the company"),
        'add':fields.char('Invoice Address',64,help='Put Here the address declared on your VAT information on SENIAT',required=True),
        'vat_apply': fields.boolean("Apply VAT?"),
    }
fiscal_requirements_config()
