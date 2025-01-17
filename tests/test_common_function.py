#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/29 1:37 PM
# @Author  : w8ay
# @File    : test_get_parent_paths.py
import unittest
from urllib.parse import urlparse
import requests
from lib.common import get_parent_paths, get_links


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_parent_paths(self):
        url = "https://github.com/w-digital-scanner/w9scan/blob/master/plugins/spider_file/bcrpscan.py"
        p = urlparse(url)
        r = get_parent_paths(p.path, False)
        d = ['/w-digital-scanner/w9scan/blob/master/plugins/spider_file/',
             '/w-digital-scanner/w9scan/blob/master/plugins/', '/w-digital-scanner/w9scan/blob/master/',
             '/w-digital-scanner/w9scan/blob/', '/w-digital-scanner/w9scan/', '/w-digital-scanner/', '/']
        self.assertTrue(r == d)
        r = get_parent_paths(url, True)
        d2 = ['https://github.com/w-digital-scanner/w9scan/blob/master/plugins/spider_file/',
              'https://github.com/w-digital-scanner/w9scan/blob/master/plugins/',
              'https://github.com/w-digital-scanner/w9scan/blob/master/',
              'https://github.com/w-digital-scanner/w9scan/blob/', 'https://github.com/w-digital-scanner/w9scan/',
              'https://github.com/w-digital-scanner/', 'https://github.com/']
        self.assertTrue(r == d2)

    def test_get_links(self):
        domain = "https://x.hacking8.com"
        r = requests.get(domain)
        links = get_links(r.text, domain)
        self.assertTrue(len(links) > 0)
