#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

from xml.dom import minidom
xmldoc = minidom.parse('karenina.xml')

with open('answer.txt', 'w') as f:
    for i,word in enumerate(xmldoc.getElementsByTagName('w')):
        for childTag in word.childNodes:
            if childTag.nodeName == u'ana':
                if u'твор' in childTag.getAttribute('gr'):
                    if i-3 >= 0:
                        f.write(cleanhtml(xmldoc.getElementsByTagName('w')[i-3].toxml()).encode('utf-8') + " ")
                    if i-2 >= 0:
                        f.write(cleanhtml(xmldoc.getElementsByTagName('w')[i-2].toxml()).encode('utf-8') + " ")
                    if i-1 >= 0:
                        f.write(cleanhtml(xmldoc.getElementsByTagName('w')[i-1].toxml()).encode('utf-8') + " ")

                    f.write(cleanhtml(word.toxml()).encode('utf-8')+" ")

                    if i+1 < len(xmldoc.getElementsByTagName('w')):
                        f.write(cleanhtml(xmldoc.getElementsByTagName('w')[i+1].toxml()).encode('utf-8') + " ")
                    if i+2 < len(xmldoc.getElementsByTagName('w')):
                        f.write(cleanhtml(xmldoc.getElementsByTagName('w')[i+2].toxml()).encode('utf-8') + " ")
                    if i+3 < len(xmldoc.getElementsByTagName('w')):
                        f.write(cleanhtml(xmldoc.getElementsByTagName('w')[i+3].toxml()).encode('utf-8') + " ")
                    f.write('\n')
                    break
