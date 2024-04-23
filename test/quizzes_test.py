import unittest

from app.controllers.quizzes_controller import QuizzesController
from app.controllers.activities_controller import ActivitiesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.activites = ActivitiesController()
        
    def test_expose_failure_01(self):
        # None is not a value that is handled within _save_data() method, which tries to loop over None 
        self.activites.activities = None
        self.activites._save_data()
        # This assert is not expected to be reached
        self.assertEqual(self.activites.activities, None)

if __name__ == '__main__':
    unittest.main()