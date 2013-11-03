# coding: utf-8

import unittest

import lxml.html


class LxmlTestCase(unittest.TestCase):

    def setUp(self):
        self.doc = lxml.html.fromstring('''
<html>
<ul id="main">
<li>1. AAA</li>
<li>2. BBB</li>
<li>3. CCC<ul>
<li>3-1. DDD</li>
<li>3-2. EEE</li>
</ul></li>
</ul>
</html>''')

    def test_text_content(self):
        self.assertEquals(self.doc.xpath('//ul')[0].text_content().strip(), '''1. AAA
2. BBB
3. CCC
3-1. DDD
3-2. EEE''')

    def test_to_string(self):
        self.assertEquals(
            lxml.html.tostring(self.doc.xpath('//ul')[0]),
            '<ul id="main">\n<li>1. AAA</li>\n<li>2. BBB</li>\n<li>3. CCC<ul>\n<li>3-1. DDD</li>\n<li>3-2. EEE</li>\n</ul></li>\n</ul>\n')


if __name__ == '__main__':
    unittest.main()
