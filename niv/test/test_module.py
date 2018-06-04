class TestModules(object):

    def test_1_plus_1(self):
        assert 2 == 1 + 1

    def test_load_data(self):
        """" test that you're able to load training data and perform sanity test """
        pass

    def test_predict(self):
        """ test that you're able to load data and  predict on it"""

    def test_fail(self):
        """ demonstrate what happens if a test fails"""
        assert (5 == 0)
