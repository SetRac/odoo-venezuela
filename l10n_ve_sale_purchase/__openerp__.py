# -*- encoding: utf-8 -*-
##############################################################################
# Copyright (c) 2011 OpenERP Venezuela (http://openerp.com.ve)
# All Rights Reserved.
# Programmed by: Israel Fermín Montilla  <israel@openerp.com.ve>
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
###############################################################################
{
    'name' : 'ISLR Sale and Purchase Functionalities',
    'version' : '0.1',
    'author' : 'Vauxoo',
    'description' : '''
        Due to the Dependendy reduction on the l10n_ve_islr_withholding module, it was necesary to incorporate
        the functionalities wich has to do with the eliminated dependencies on another module. That's what this one
        was created for.
    ''',
    'category' : '',
    'website' : 'http://openerp.com',
    'depends' : ['sale', 'purchase', 'stock', 'l10n_ve_islr_withholding'],
    'update_xml' : [
        'view/purchase_view.xml',
        'view/sale_order_view.xml',
    ],
    'demo' : [],
    'active' : False,
    'installable': True,
}
