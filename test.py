# coding: utf-8

import unittest

import lxml.html


class LxmlTestCase(unittest.TestCase):

    def setUp(self):
        self.doc = lxml.html.fromstring('''
<html>
<ul>
<li>1st</li>
<li>2nd</li>
</ul>
</html>''')

    def test_text_content(self):
        ul = self.doc.xpath('//ul')[0]
        self.assertEquals(ul.text_content(), '\n1st\n2nd\n')

    def test_to_string(self):
        ul = self.doc.xpath('//ul')[0]
        self.assertEquals(
            lxml.html.tostring(ul),
            '<ul>\n<li>1st</li>\n<li>2nd</li>\n</ul>\n')

    def test_text(self):
        ul = self.doc.xpath('//ul')[0]
        self.assertEquals(ul.text, '\n')

    def test_tail(self):
        ul = self.doc.xpath('//ul')[0]
        self.assertEquals(ul.tail, '\n')


if __name__ == '__main__':
    unittest.main()
