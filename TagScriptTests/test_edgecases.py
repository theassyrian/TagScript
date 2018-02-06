import TagScriptEngine
from unittest import TestCase

class test_edgecase_functionality(TestCase):

    def setUp(self):
        """ Sets up engine and other variables that might be needed between tests """
        self.engine = TagScriptEngine.Engine()
    def tearDown(self):
        """ Cleans the plate to make tests consistent """
        self.engine.Clear_Variables()
        self.engine = None

    # Actual tests below
    # ======
    def test_edgecase_missing_var_in_math(self):

        self.engine.Add_Variable("1", "30")
        self.engine.Add_Variable("2", "2")
        #self.engine.Add_Variable("3", "0")
        trouble = self.engine.Process("m{($1+1+0$3;)*$2}")

        self.assertEqual("62", trouble)
        