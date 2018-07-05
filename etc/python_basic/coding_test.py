# -*- coding: utf-8 -*-
# Encoding: UTF-8

# from django.conf import settings
# settings.configure()

# import unittest
# from unittest import TestCase
# try:
#     import yourtest
# except ImportError:
#     raise Exception('Create a file named yourtest.py')
import unittest
from unittest import TestCase
try:
    import yourtest
except ImportError:
    raise Exception('Create a file named yourtest.py')

class SimpleStringManipulationTest(TestCase):
    def test_string_contains(self):
        self.assertEqual(True, yourtest.string_contains('hello', 'hello there'))
        self.assertEqual(False, yourtest.string_contains('not in there', ''))

    def test_split_string_remove_space(self):
        self.assertEqual(['a', 'b', 'c', 'd', 'e', 'f', 'g'],
                         yourtest.clean_split('a  b   c       d e f g'))

    def test_re_matching(self):
        self.assertEqual(True, yourtest.re_match(r'\d+', '012345'))
        self.assertEqual(False, yourtest.re_match(r'\d+', 'hello'))


class SimpleListTest(TestCase):
    def test_sum(self):
        self.assertEqual(6, yourtest.get_sum([1, 2, 3]))

    def test_average(self):
        self.assertEqual(10, yourtest.average([10, 10, 20, 0]))


class SimpleDataStructureTest(TestCase):
    def test_word_count(self):
        self.assertEqual(
            {'foot': 3, 'left': 2, 'right': 2},
            yourtest.wc('left foot left foot right foot right'))


xml = '''<?xml version="1.0" encoding="utf-8"?>
<whois>
    <query>115.95.211.199</query>
    <queryType>ipv4</queryType>
    <registry>krnic</registry>
    <countryCode>kr</countryCode>
    <korean>
        <user>
            <netInfo>
                <range>115.95.208.0~115.95.223.255</range>
                <prefix>/20</prefix>
                <netName>BORANET-INFRA</netName>
                <orgName>\xec\xa3\xbc\xec\x8b\x9d\xed\x9a\x8c\xec\x82\xac \xec\x97\x98\xec\xa7\x80\xec\x9c\xa0\xed\x94\x8c\xeb\x9f\xac\xec\x8a\xa4</orgName>
                <orgID>ORG572</orgID>
                <addr>\xec\x84\x9c\xec\x9a\xb8 \xec\xa4\x91\xea\xb5\xac \xeb\x82\xa8\xeb\x8c\x80\xeb\xac\xb8\xeb\xa1\x9c5\xea\xb0\x80    </addr>
                <zipCode>100-095</zipCode>
                <regDate>20110208</regDate>
                <publishes>N</publishes>
            </netInfo>
            <techContact>
                <orgName>BORANET</orgName>
                <addr>\xec\x84\x9c\xec\x9a\xb8 \xec\xa4\x91\xea\xb5\xac \xeb\x82\xa8\xeb\x8c\x80\xeb\xac\xb8\xeb\xa1\x9c5\xea\xb0\x80    </addr>
                <zipCode>100-095</zipCode>
                <email>ipadm@lguplus.co.kr</email>
            </techContact>
        </user>
    </korean>
</whois>
'''


class SimpleXMLParser(TestCase):
    def test_parse_xml(self):
        self.assertEqual(u'서울 중구 남대문로5가', yourtest.get_user_city(xml))


class SimpleJSONUsage(TestCase):
    def test_convert_from_json(self):
        self.assertEqual(yourtest.convert_from_json('{"hello": 123}'),
                         {'hello': 123})


# class SimpleDjangoHandler(TestCase):
#     def test_handler(self):
#         from django.test.client import RequestFactory
#         rf = RequestFactory()
#         response = yourtest.handler(rf.get('/', {'name': 'Bob'}))
#         self.assertEqual(response.content, 'Hello Bob')
#         response = yourtest.handler(rf.get('/', {'name': u'박근혜',
#                                                  'polite': 'True'}))
#         self.assertEqual(response.content, '안녕하십니까 박근혜')


class SimpleSortingTest(TestCase):
    def test_sorting(self):
        self.assertEqual([1, 2, 3, 4, 5], yourtest.sorter([5, 1, 2, 3, 4]))
        self.assertEqual(['Dan', 'Sooyeon', 'Haereen'],
                         yourtest.sortbyage(
                             [{'name': 'Dan', 'birthyear': 1979},
                              {'name': 'Sooyeon', 'birthyear': 1980},
                              {'name': 'Haereen', 'birthyear': 2011}]))


class SimpleOOTest(TestCase):
    def test_simple_inheritence_test(self):
        megaman = yourtest.Megaman()
        mario = yourtest.Mario()
        self.assertTrue(isinstance(megaman, yourtest.VideoGameCharacter))
        self.assertTrue(isinstance(mario, yourtest.VideoGameCharacter))
        self.assertEqual(mario.get_name(), 'Mario')
        self.assertEqual(megaman.get_name(), 'Megaman')
        self.assertEqual(mario.get_company(), 'Nintendo')
        self.assertEqual(megaman.get_company(), 'Capcom')


class SimpleDecoratorTest(TestCase):
    def test_memoize_decorator(self):

        @yourtest.memoize
        def square(x):
            square.count = square.count + 1
            return x * x
        square.count = 0

        self.assertEqual(square(2), 4)
        self.assertEqual(square(2), 4)
        self.assertEqual(square(3), 9)
        self.assertEqual(square.count, 2)


if __name__ == '__main__':
    unittest.main()
