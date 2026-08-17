from odoo.tests.common import TransactionCase


class TestCareNote(TransactionCase):
    def test_create_note(self):
        self.env["care.note"].create({"name": "Fixture"})
