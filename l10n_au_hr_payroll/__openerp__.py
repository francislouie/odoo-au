# -*- encoding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2014 One Click Software (<http://oneclick.solutions>)
#	 Contributed to the Odoo - Australian localisation project
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
	'name': 'Australia - Payroll',
    'category': 'Localization',
    'author': 'One Click Software',
    'depends': ['hr_payroll'],
    'version': '0.2',
    'description': """
Australian Payroll Rules.
======================
Support for Australian payroll
WORK IN PROGRESS
    """,

    'auto_install': False,
    'data':[
        'l10n_au_hr_payroll_data.xml',
        'l10n_au_hr_payroll_view.xml',
		'security/ir.model.access.csv',
    ],
    'installable': True
 }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
