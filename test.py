# coding: utf-8

import unittest

import lxml.html


class LxmlTestCase(unittest.TestCase):

    def test_text_content(self):

        doc = lxml.html.fromstring('''
<html>
<body>B
<div>
<span>A</span>
</div>
</body>
</html>''')

        self.assertEquals(doc.xpath('//body')[0].text_content().strip(), '''B

A''')


if __name__ == '__main__':
    unittest.main()
