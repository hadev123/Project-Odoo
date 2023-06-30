import json
from odoo import http
from odoo.http import request

class DtsAssetsContorller(http.Controller):

    @http.route('/dts-assets', auth='public', website=True)
    def dts_assets_handler(self):
        return json.dumps({
            "content": "Welcome to API!"
        })

    @http.route('/api/partners', type='http', auth='public', methods=['GET'], csrf=False)
    def get_partners(self):
        partners = request.env['res.partner'].sudo(
        ).search_read([], ['name', 'email', 'phone'])
        return json.dumps(partners)

    @http.route('/mountain', auth='public')
    def mountain_check(self):
        return request.render("web.login")
