#!/usr/bin/env python

import os

     
indir = '/Users/RyanLucas/Desktop/Contacts/'
for root, dirs, filenames in os.walk(indir):
    for f in filenames:
        if f == 'Contact.txt':
            with open(os.path.join(root, f),'r') as contactfile:
                contact_dic = {}
                for line in contactfile:
                    entry = line.replace("\t", "").replace("\n", "").replace("\r", "").split(':', 1)
                    if entry: contact_dic.update({entry[0]: entry[1:]})
                display_name = contact_dic.get("Display name")
                first_name = contact_dic.get("Given name")
                last_name = contact_dic.get("Surname")
                company_name = contact_dic.get("Company name")
                home_number = contact_dic.get("Home phone number")
                bus_number1 = contact_dic.get("Business phone number 1")
                bus_number2 = contact_dic.get("Business phone number 2")
                mobile_number = contact_dic.get("Mobile phone number")
                address = contact_dic.get("Postal address")
                if address is not None:
                    for item in address:
                        full_address = item.replace(",", "")
                email_address1 = contact_dic.get("Email address 1")
                email_address2 = contact_dic.get("Email address 2")
                fullline = "%s,%s,,%s,,,,,,,,,,,,,,,,,,,,,,,,,Home,%s,Work,%s,Work,%s,Mobile,%s,Home,%s,,,,,,,,,,,,,,,,,,,,,," % (display_name, first_name, last_name, email_address1, email_address2, bus_number1, mobile_number, full_address)
                full_address = ""
            print fullline.replace("'", "").replace("[", "").replace("]", "")
                
            print contact_dic