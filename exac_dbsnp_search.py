import sys
import os
import json
import urllib2
import time
from Tkinter import *
from tkSimpleDialog import askstring

prozor = Tk()
prozor.withdraw()

#vreme = str(time.strftime("%d-%m-%Y %Hh%Mm%Ss"))


rs_brojevi = askstring("rsID | ExAC", "Unesi RS brojeve odvojene razmakom: ")


try:
    rs_brojevi = rs_brojevi.split()


except AttributeError:
        print "\nGreska 01"

else:
    for i in rs_brojevi:
        
        url = 'http://exac.hms.harvard.edu/rest/dbsnp/'+i 
        
        print 'Preuzimanje..', url
        
        html = urllib2.urlopen(url).read()
        
        info = json.loads(html)
        
        try:
            gene = str(info['variants_in_region'][0]['vep_annotations'][0]['Gene'])
            symbol = str(info['variants_in_region'][0]['vep_annotations'][0]['SYMBOL'])
            rsID = str(info['rsid'])
            variantID =  str(info['variants_in_region'][0]['variant_id'])
            mConseq = str(info['variants_in_region'][0]['major_consequence'])
            category = str(info['variants_in_region'][0]['category'])
            allele_freq = str(info['variants_in_region'][0]['allele_freq'])
        
        except IndexError:
            print "\nExAC ne sadrzi podatke za", i, '\n\n\n'
            time.sleep(5)
    
        else:
            print '\nrsID: ', rsID
            print '\ngen: ', gene
            print '\nsimbol: ', symbol
            print '\nvariantID: ', variantID
            print '\nucestalost alela: ', allele_freq
            print '\nkategorija: ', category
            print '\nposledica: ', mConseq, '\n\n\n'
            time.sleep(5)
        
        
