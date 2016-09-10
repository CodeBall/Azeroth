from azeroth.controllers.tag_controller import TagController
from azeroth.app_runner import app, mysql_db as db
from azeroth.models.tag import Tag

import unittest


class TestTagController(unittest.TestCase):
    def setUp(self):
        self.tag_controller = TagController()
        self.data_success = {
            "name": "嘲讽",
            "nickname": "cf",
            "use_group": False,
            "about": "嘲讽技能,敌人必须先攻击该随从"
        }
        self.data_error = {
            "name": "冲锋",
        }

    def tearDown(self):
        with app.app_context():
            Tag.query.delete()
            db.session.commit()

    def test_add_tag_error(self):
        with app.app_context():

            result2 = self.tag_controller.add_tag(self.data_error)
            self.assertEqual(result2.get("status"), "failure")

    def test_add_tag_success(self):
        with app.app_context():
            result1 = self.tag_controller.add_tag(self.data_success)
            self.assertEqual(result1.get("status"), "success")

    def test_show_tags(self):
        with app.app_context():
            results = self.tag_controller.get_all_tags()
            for result in results:
                print(result)


if __name__ == "__main__":
    unittest.main()