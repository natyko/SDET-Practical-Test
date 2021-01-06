import unittest
from SDET_Practical_Test import get_response

api_test = 'http://api.open-notify.org/astros.json'


class RequestTest(unittest.TestCase):
    def setUp(self):
        self.res = get_response(api_test)

    def test_get_response(self):
        self.assertEqual(self.res, 200)


if __name__ == '__main__':
    unittest.main()


def test_answer(test):
    '''
    pytest
    '''
    assert get_response(api_test) == 200

print(test_answer(api_test))
