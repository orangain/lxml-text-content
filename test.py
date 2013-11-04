# coding: utf-8

import unittest

import lxml.html


class UlLiTestCase(unittest.TestCase):

    def setUp(self):
        parser = lxml.html.HTMLParser(remove_blank_text=True)
        self.doc = lxml.html.fromstring('''
<html>
<ul>
<li>1st</li>
<li>2nd</li>
</ul>
</html>''', parser=parser)

    def test_text_content(self):
        ul = self.doc.xpath('//ul')[0]
        self.assertEquals(ul.text_content(), '1st\n2nd\n')

    def test_to_string(self):
        ul = self.doc.xpath('//ul')[0]
        self.assertEquals(
            lxml.html.tostring(ul),
            '<ul><li>1st</li>\n<li>2nd</li>\n</ul>')

    def test_text(self):
        ul = self.doc.xpath('//ul')[0]
        self.assertEquals(ul.text, None)

    def test_tail(self):
        ul = self.doc.xpath('//ul')[0]
        self.assertEquals(ul.tail, None)


class UlLiSpaceTestCase(unittest.TestCase):

    def setUp(self):
        parser = lxml.html.HTMLParser(remove_blank_text=True)
        self.doc = lxml.html.fromstring('''
<html>
<ul>
 <li>1st</li>
<li>2nd</li>
</ul>
</html>''', parser=parser)

    def test_text_content(self):
        ul = self.doc.xpath('//ul')[0]
        self.assertEquals(ul.text_content(), '1st\n2nd\n')

    def test_to_string(self):
        ul = self.doc.xpath('//ul')[0]
        self.assertEquals(
            lxml.html.tostring(ul),
            '<ul><li>1st</li>\n<li>2nd</li>\n</ul>')

    def test_text(self):
        ul = self.doc.xpath('//ul')[0]
        self.assertEquals(ul.text, None)

    def test_tail(self):
        ul = self.doc.xpath('//ul')[0]
        self.assertEquals(ul.tail, None)


class InvalidUlLiTestCase(unittest.TestCase):

    def setUp(self):
        parser = lxml.html.HTMLParser(remove_blank_text=True)
        self.doc = lxml.html.fromstring('''
<html>
<ul>X
<li>1st</li>
<li>2nd</li>
</ul>
</html>''', parser=parser)

    def test_text_content(self):
        ul = self.doc.xpath('//ul')[0]
        self.assertEquals(ul.text_content(), 'X\n1st\n2nd\n')

    def test_to_string(self):
        ul = self.doc.xpath('//ul')[0]
        self.assertEquals(
            lxml.html.tostring(ul),
            '<ul>X\n<li>1st</li>\n<li>2nd</li>\n</ul>')

    def test_text(self):
        ul = self.doc.xpath('//ul')[0]
        self.assertEquals(ul.text, 'X\n')

    def test_tail(self):
        ul = self.doc.xpath('//ul')[0]
        self.assertEquals(ul.tail, None)


class DivSpanTestCase(unittest.TestCase):

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
