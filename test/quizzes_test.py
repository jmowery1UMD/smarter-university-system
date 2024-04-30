from datetime import datetime
import unittest

from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('assignments.json')
        
    def test_expose_failure_01(self):
        """
        Test adding a new quiz without a title.
        The code should raise an exception in quizzes_controller.py at line 63, in 'add_quiz'
        """
        self.ctrl.clear_data()
        # add a new quiz with empty title.
        quiz1_id = self.ctrl.add_quiz(None, "Quiz 1", datetime.now(), datetime.now())
        # The quiz should still exist even though it is added without a title.
        # Expecting `quiz1_id` to be Not `None`.
        self.assertIsNotNone(quiz1_id, "The quiz is NotNone")
        
    def test_expose_failure_02(self):
        """
        Should add question and retrieve question
        Testing quizzes_controller.py on line 129
        """
        self.ctrl.clear_data()
        quiz_id  = self.ctrl.add_quiz("Quiz on Chickens!", "Behavior of Chickens",datetime.time, datetime.today)
        question_id = self.ctrl.add_question(quiz_id,"Question 1", "Did the chicken cross the road?")
        self.ctrl.quizzes = True
        question = self.ctrl.get_question_by_id(question_id)
        self.assertIsNotNone(question, "Question id should exist")
        
    def test_expose_faliure_03(self):
        """
        JSON Load method does not handle improperly formatted JSON.
        """
        QuizzesController('broken.json')
        self.assertGreater(self.ctrl.quizzes.count, 0)

if __name__ == '__main__':
    unittest.main()