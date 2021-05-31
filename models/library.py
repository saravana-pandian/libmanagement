
from odoo import models, fields, api, exceptions



class Library(models.Model):
	_name = 'library.books'
	_description = 'Brussels Library'

	name = fields.Char(string="ISBN", required=False)
	year = fields.Char(string="Year of Edition", required=False)
	book_name = fields.Char(string="Book Title", required=False)

	librarian_id = fields.Many2one('res.users', string="Library Admin", index=True)
	
