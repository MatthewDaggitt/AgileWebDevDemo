from unittest import TestCase

from app import create_app, db
from app.config import TestConfig
from app.controllers import GroupCreationError, create_group

class BasicUnitTests(TestCase):

    def setUp(self):
        testApp = create_app(TestConfig)
        self.app_context = testApp.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_group_missing_student(self):
        with self.assertRaisesRegex(GroupCreationError, "Not all students registered"):
            create_group(["00012334","00012335"])
        