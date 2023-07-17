import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()
        self.model.save()
        self.storage.new(self.model)
        self.storage.save()

    def tearDown(self):
        self.storage.reload()
        self.storage = None

    def test_all(self):
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(len(all_objects), 1)
        self.assertIn(
            f"{self.model.__class__.__name__}./" f"{self.model.id}", all_objects
        )

    def test_new(self):
        new_model = BaseModel()
        self.storage.new(new_model)
        self.assertEqual(len(self.storage.all()), 2)
        key = f"{new_model.__class__.__name__}.{new_model.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], new_model)

    def test_save(self):
        # Create a temporary file
        file_path = "test_file.json"

        # Save objects to the temporary file
        self.storage._FileStorage__file_path = file_path
        self.storage.save()

        # Verify that the temporary file exists
        with open(file_path) as fd:
            saved_data = json.load(fd)
        self.assertIsInstance(saved_data, dict)
        self.assertEqual(len(saved_data), 1)
        self.assertIn(
            f"{self.model.__class__.__name__}./" f"{self.model.id}", saved_data
        )

        # Clean up the temporary file

        os.remove(file_path)

    def test_reload(self):
        # Save objects to a file
        self.storage.save()

        # Modify the saved objects
        for key in self.storage.all():
            obj = self.storage.all()[key]
            obj.name = "Modified"
            obj.save()

        # Reload the objects from the file
        self.storage.reload()

        # Verify that the modifications were discarded
        for key in self.storage.all():
            obj = self.storage.all()[key]
            self.assertNotEqual(obj.name, "Modified")


if __name__ == "__main__":
    unittest.main()
