import unittest
# from city_functions import city
#
#
# class NamesTestCase(unittest.TestCase):
#     """测试city_function.py"""
#     def test_city_country(self):
#         formatted_name = city('beijing', 'China')
#         self.assertEqual(formatted_name, 'Beijing,China')
#
#
# unittest.main()


from city_functions import cities


class NamesTestCase(unittest.TestCase):
    """测试city_function.py"""
    def test_city_country_population(self):

        formatted_name = cities('beijing', 'China')
        self.assertEqual(formatted_name, 'Beijing,China - Population 5000000')


unittest.main()

