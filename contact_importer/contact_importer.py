#!/usr/bin/env python

import os

     
indir = '/Users/RyanLucas/Desktop/Contacts/test'
for root, dirs, filenames in os.walk(indir):
    for f in filenames:
     if f == 'Contact.txt':
      with open(os.path.join(root, f),'r') as contactfile:
        dic = {}
        for line in contactfile:
         entry = line.replace("\t", "").replace("\n", "").split(':', 1)
         if entry: dic.update({entry[0]: entry[1:]})
        print dic