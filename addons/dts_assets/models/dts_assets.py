# -*- coding: utf-8 -*-
from odoo import fields, models, api

class DtsAssets(models.Model):
    _name = "dts_assets"
    _description = "DTS Assets model"

    proposer = fields.Text('Người đề xuất')
    department_proposer = fields.Text('Khối/TT/Ban')
    propose_asset = fields.Selection([
        ('yes', 'Cấp Tài sản'),
        ('no', 'Đổi Tài sản')
    ], string='Đề xuất được', default='yes')
    time_has_assets = fields.Date('Thời gian có tài sản', required=False)
    recommended_reason = fields.Text('Lý do đề xuất')
    check_asset = fields.Selection([
        ('yes', 'Có'),
        ('no', 'Không')
    ], string='Kiểm tra với các Đơn vị QLTS', default='yes')

    manager_id = fields.Many2one('res.partner', string='Phê duyệt 1')
    president_id = fields.Many2one('res.partner', string='Phê duyệt 2')
    general_director_id = fields.Many2one('res.partner', string='Phê duyệt 3')

    state_manager = fields.Selection([
        ('draft_manager', 'MARK AS DRAFT'),
        ('waiting_approval_manager', 'CHỜ DUYỆT'),
        ('approved_manager', 'DUYỆT'),
        ('rejected_manager', 'TỪ CHỐI')
    ], string='Trạng thái 1', default='draft_manager', groups="dts_assets.group_dts_assets_manager")

    state_president = fields.Selection([
        ('draft_president', 'MARK AS DRAFT'),
        ('waiting_approval_president', 'CHỜ DUYỆT'),
        ('approved_president', 'DUYỆT'),
        ('rejected_president', 'TỪ CHỐI')
    ], string='Trạng thái 2', default='draft_president', groups="dts_assets.group_dts_assets_president")

    state_general_director = fields.Selection([
        ('draft', 'MARK AS DRAFT'),
        ('waiting_approval', 'CHỜ DUYỆT'),
        ('approved', 'DUYỆT'),
        ('rejected', 'TỪ CHỐI')
    ], string='Trạng thái 3', default='draft', groups="dts_assets.group_dts_assets_general_director")

    table_assets = fields.One2many("dts_assets_table", "id_asset")

    @api.depends('state_manager, state_president, state_general_director')
    def action_submit_approval(self):
        if self.env.user.has_group('dts_assets.group_dts_assets_manager'):
            self.write({'state_manager': 'waiting_approval_manager'})
        if self.env.user.has_group('dts_assets.group_dts_assets_president'):
            self.write({'state_president': 'waiting_approval_president'})
        if self.env.user.has_group('dts_assets.group_dts_assets_general_director'):
            self.write({'state_general_director': 'waiting_approval'})

    @api.depends('state_manager, state_president, state_general_director')
    def action_approve(self):
        if self.env.user.has_group('dts_assets.group_dts_assets_manager'):
            self.write({'state_manager': 'approved_manager'})
        if self.env.user.has_group('dts_assets.group_dts_assets_president'):
            self.write({'state_president': 'approved_president'})
        if self.env.user.has_group('dts_assets.group_dts_assets_general_director'):
            self.write({'state_general_director': 'approved'})

    @api.depends('state_manager, state_president, state_general_director')
    def action_reject(self):
        if self.env.user.has_group('dts_assets.group_dts_assets_manager'):
            self.write({'state_manager': 'rejected_manager'})
        if self.env.user.has_group('dts_assets.group_dts_assets_president'):
            self.write({'state_president': 'rejected_president'})
        if self.env.user.has_group('dts_assets.group_dts_assets_general_director'):
            self.write({'state_general_director': 'rejected'})

    compute_user = fields.Text(string='Trạng thái', compute='_compute_user', store=True, groups="dts_assets.group_dts_assets_user")

    @api.depends('state_manager', 'state_president', 'state_general_director')
    def _compute_user(self):
        for record in self:
            if (record.state_manager == 'approved_manager' and record.state_president == 'approved_president' and record.state_general_director == 'approved'):
                record.compute_user = 'DUYỆT'
            elif (record.state_manager == 'rejected_manager' or record.state_president == 'rejected_president' or record.state_general_director == 'rejected'):
                record.compute_user = 'TỪ CHỐI'
            else:
                record.compute_user = 'CHỜ DUYỆT'    
