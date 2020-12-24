# -*- coding: utf-8 -*-
from odoo import http


class Bands(http.Controller):
    @http.route('/bands/musicians/', auth='public', website=True)
    def musicians(self, **kw):
        Musicians = http.request.env['bands.musicians']
        return http.request.render('bands.musician_page', {
            'musicians': Musicians.search([])
        })

    @http.route('/bands/<model("bands.musicians"):musician>/', auth='public',
                website=True)
    def musician(self, musician):
        return http.request.render('bands.biography', {
            'person': musician
        })

#     @http.route('/bands/bands/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bands.listing', {
#             'root': '/bands/bands',
#             'objects': http.request.env['bands.bands'].search([]),
#         })

#     @http.route('/bands/bands/objects/<model("bands.bands"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bands.object', {
#             'object': obj
#         })
