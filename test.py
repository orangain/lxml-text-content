# coding: utf-8

import unittest

import lxml.html


class LxmlTestCase(unittest.TestCase):

    def test_text_content(self):

        doc = lxml.html.fromstring('''
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

        self.assertEquals(doc.xpath('id("main")')[0].text_content().strip(), '''1. AAA
2. BBB
3. CCC
3-1. DDD
3-2. EEE''')


if __name__ == '__main__':
    unittest.main()
