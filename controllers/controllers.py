# -*- coding: utf-8 -*-
from odoo import http


class Bands(http.Controller):
    @http.route('/uber-uns', auth='public', website=True)
    def uber_uns(self, **kw):
        return http.request.render('bands.uber-uns')

    @http.route('/uber-uns/geschichte', auth='public', website=True)
    def geschichte(self, **kw):
        return http.request.render('bands.geschichte')

    @http.route('/uber-uns/philosophie', auth='public', website=True)
    def philosophie(self, **kw):
        return http.request.render('bands.philosophie')

    @http.route('/uber-uns/offene-stellen', auth='public', website=True)
    def offene_stellen(self, **kw):
        return http.request.render('bands.offene-stellen')

    @http.route('/uber-uns/zertifizierung', auth='public', website=True)
    def zertifizierung(self, **kw):
        return http.request.render('bands.zertifizierung')

    @http.route('/uber-uns/partner', auth='public', website=True)
    def partner(self, **kw):
        return http.request.render('bands.partner')

    @http.route('/uber-uns/messen', auth='public', website=True)
    def messen(self, **kw):
        return http.request.render('bands.messen')

    @http.route('/uber-uns/aktuelles', auth='public', website=True)
    def aktuelles(self, **kw):
        return http.request.render('bands.aktuelles')

    # @http.route('/bands/<model("bands.musicians"):musician>/', auth='public',
    #             website=True)
    # def musician(self, musician):
    #     return http.request.render('bands.biography', {
    #         'person': musician
    #     })

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
