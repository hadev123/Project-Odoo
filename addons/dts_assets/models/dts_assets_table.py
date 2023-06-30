# -*- coding: utf-8 -*-
from odoo import fields, models, api

class DtsAssetsTable(models.Model):
    _name = "dts_assets_table"
    _description = "DTS Assets Table model"

    id_asset = fields.Many2one("dts_assets")
    name_propose_asset = fields.Char(string='Tên Tài sản đề xuất')
    quantity_assets = fields.Float(string='Số Lượng')
    asset_id = fields.Char(string='Part Number', size=8, trim=True)
    reference_price = fields.Float('Giá tham chiếu', default=0)
    name_code_property_use = fields.Char('Tên và Mã Tài sản đang sử dụng')
    total_asset = fields.Float('Tổng cộng')
