# Copyright 2026 CIT Services
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models


class IrUiView(models.Model):
    _inherit = "ir.ui.view"

    def _postprocess_access_rights(self, arch):
        """Restrict the 'Duplicate' action based on the user's model access rights."""
        target_model = arch.get("model_access_rights")
        arch = super()._postprocess_access_rights(arch)
        if not target_model or arch.tag not in ("list", "form") or self.env.su:
            return arch

        if not self.env["ir.model.access"].check_duplicate_access(
            target_model, raise_exception=False
        ):
            arch.set("duplicate", "0")
        return arch
