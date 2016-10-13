#!/usr/bin/env python

import os

     
indir = '/Users/RyanLucas/Desktop/Contacts/'
for root, dirs, filenames in os.walk(indir):
    for f in filenames:
        if f == 'Contact.txt':
            with open(os.path.join(root, f),'r') as contactfile:
                # for line in contactfile:
                #     if ":" not in line: 
                #         print line
                lines = contactfile.readlines()
                print lines[24]
                