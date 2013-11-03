# coding: utf-8

import unittest

import lxml.html


class LxmlTestCase(unittest.TestCase):

    def setUp(self):
        self.doc = lxml.html.fromstring('''
<html>
<div>
<span>1st</span>
<span>2nd</span>
</div>
</html>''')

    def test_text_content(self):
        div = self.doc.xpath('//div')[0]
        self.assertEquals(div.text_content(), '\n1st\n2nd\n')

    def test_to_string(self):
        div = self.doc.xpath('//div')[0]
        self.assertEquals(
            lxml.html.tostring(div),
            '<div>\n<span>1st</span>\n<span>2nd</span>\n</div>\n')

    def test_text(self):
        div = self.doc.xpath('//div')[0]
        self.assertEquals(div.text, '\n')

    def test_tail(self):
        div = self.doc.xpath('//div')[0]
        self.assertEquals(div.tail, '\n')


if __name__ == '__main__':
    unittest.main()
