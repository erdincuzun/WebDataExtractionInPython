import os
import time
import regex
import bsoup
import lxml_ext
from collections import Counter

def test_lib(data, pattern, domain, webpage):
    #lxml
    tagname = parse_TagName(pattern)
    start_time = time.clock()
    sonuc = lxml_ext.extract_all(data, pattern)
    elapsed_time = time.clock() - start_time
    if(len(sonuc)>0):
        extration_r = 0
        if(sonuc[0].count(start_TagName(pattern)) == sonuc[0].count(end_TagName(pattern))):
            extration_r = 1
        f1.write(domain + ',' + webpage + ',' + str(len(data)) + ',' + pattern + ',' + tagname + ',' + str(len(pattern)) + ',' + str(elapsed_time * 1000) + ',' + str(extration_r)  + ',' + 'lxml_all\n')
    
    start_time = time.clock()
    sonuc = lxml_ext.extract(data, pattern)
    elapsed_time = time.clock() - start_time
    if(len(sonuc)>0):
        extration_r = 0
        if(sonuc.count(start_TagName(pattern)) == sonuc.count(end_TagName(pattern))):
            extration_r = 1
        f1.write(domain + ',' + webpage + ',' + str(len(data)) + ',' + pattern + ',' + tagname + ',' + str(len(pattern)) + ',' + str(elapsed_time * 1000) + ',' + str(extration_r)  + ',' + 'lxml\n')
    #regex all
    start_time = time.clock()
    sonuc = regex.extract_all(data, pattern)
    elapsed_time = time.clock() - start_time
    if(len(sonuc)>0):
        extration_r = 0
        if(sonuc[0].count(start_TagName(pattern)) == sonuc[0].count(end_TagName(pattern))):
            extration_r = 1
        f1.write(domain + ',' + webpage + ',' + str(len(data)) + ',' + pattern + ',' + tagname + ',' + str(len(pattern)) + ',' + str(elapsed_time * 1000) + ',' + str(extration_r) + ',regexall\n')
    #regex first
    start_time = time.clock()
    sonuc = regex.extract(data, pattern)
    elapsed_time = time.clock() - start_time
    if(len(sonuc)>0):
        extration_r = 0
        if(sonuc.count(start_TagName(pattern)) == sonuc.count(end_TagName(pattern))):
            extration_r = 1
        f1.write(domain + ',' + webpage + ',' + str(len(data)) + ',' + pattern + ',' + tagname + ',' + str(len(pattern)) + ',' + str(elapsed_time * 1000) + ',' + str(extration_r)  + ',regex\n')

    #beatifulsoup
    #parsers = ["html.parser", "lxml", "html5lib"] #others are too slow, so closed
    parsers = ["lxml"]
    for parser in parsers:
        start_time = time.clock()
        sonuc = bsoup.extract_all(data, pattern, parser)
        elapsed_time = time.clock() - start_time
        if(len(sonuc)>0):
            extration_r = 0
            if(sonuc[0].count(start_TagName(pattern)) == sonuc[0].count(end_TagName(pattern))):
                extration_r = 1
            f1.write(domain + ',' + webpage + ',' + str(len(data)) + ',' + pattern + ',' + tagname + ',' + str(len(pattern)) + ',' + str(elapsed_time * 1000) + ',' + str(extration_r)  + ',bs_' + parser + '_all\n')   
        
        start_time = time.clock()
        sonuc = bsoup.extract(data, pattern, parser)
        elapsed_time = time.clock() - start_time
        if(len(sonuc)>0):
            extration_r = 0
            if(sonuc.count(start_TagName(pattern)) == sonuc.count(end_TagName(pattern))):
                extration_r = 1
            f1.write(domain + ',' + webpage + ',' + str(len(data)) + ',' + pattern + ',' + tagname + ',' + str(len(pattern)) + ',' + str(elapsed_time * 1000) + ',' + str(extration_r)  + ',bs_' + parser + '\n')   

#find tagName
def parse_TagName(element):
    return element[(element.find('<') + 1):(element.find(' '))]

def start_TagName(element):
    return '<' + parse_TagName(element)

def end_TagName(element):
    return '</' + parse_TagName(element) + '>'


#main
f1 = open(os.getcwd()+ '\\Results\\results.txt','a+')


data_path = os.getcwd()+ '\\data\\'
rule_path = os.getcwd()+ '\\data\\Rules\\'
for filename in os.listdir(rule_path):
    lines = [line.rstrip('\n') for line in open(rule_path + filename)]
    for line in lines:
        data_dir = data_path + filename.replace(".txt", "") + '\\'
        for webpage in os.listdir(data_dir):
            with open(data_dir + webpage, 'r', encoding='utf-8', errors='ignore') as f:
                data = f.read() #read file
                pattern = line.split(',')[0] #extraction element
                test_lib(data, pattern, filename.replace(".txt", ""), webpage)
f1.close()

