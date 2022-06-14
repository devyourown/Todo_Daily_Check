import unittest
from QnA import QnA

class TddTest(unittest.TestCase):
    def test(self):
        qna = QnA()
        qna.add_question("Did you solve programming problems?")
        self.assertEqual(qna.questions[0], "Did you solve the programming problems?")
        qna.execute()
        self.assertEqual(qna.answers[0], True)
        self.assertFalse(qna.answers[1])

unittest.main()