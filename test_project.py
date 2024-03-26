import unittest
import os

# Import the functions to be tested
from project import newNote, deleteNote, editNote, readFile, writeFile

class TestNoteFunctions(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.test_file = "test_notes.txt"
        with open(self.test_file, 'w') as f:
            f.write("Note 1\nNote 2\nNote 3\n")

    def tearDown(self):
        # Remove the temporary file after testing
        os.remove(self.test_file)

    def test_newNote(self):
        noteList = []
        newNote(noteList, "New Note")
        self.assertEqual(noteList, ["New Note"])

    def test_deleteNote(self):
        noteList = ["Note 1", "Note 2", "Note 3"]
        deleteNote(noteList, 1)
        self.assertEqual(noteList, ["Note 1", "Note 3"])

    def test_editNote(self):
        noteList = ["Note 1", "Note 2", "Note 3"]
        editNote(noteList, 1, "Updated Note")
        self.assertEqual(noteList, ["Note 1", "Updated Note", "Note 3"])

    def test_readFile(self):
        noteList = []
        readFile(self.test_file, noteList)
        self.assertEqual(noteList, ["Note 1", "Note 2", "Note 3"])

    def test_writeFile(self):
        noteList = ["Note 1", "Note 2", "Note 3"]
        writeFile(self.test_file, noteList)
        with open(self.test_file, 'r') as f:
            lines = f.readlines()
        self.assertEqual(lines, ["Note 1\n", "Note 2\n", "Note 3\n"])

if __name__ == '__main__':
    unittest.main()
