from bs4 import BeautifulSoup
#parsers: html.parser, lxml, html5lib
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser

#extract one result
def extract(html, pattern, parser):
    soup = BeautifulSoup(html, parser)
    return  soup.find(parse_TagName(pattern), attrs=parse_Attributes(pattern, parser)).decode_contents(formatter="html")
#for html format: .decode_contents(formatter="html")

#extract all results
def extract_all(html, pattern, parser):
    soup = BeautifulSoup(html, parser)
    temp_res = soup.find_all(parse_TagName(pattern), attrs=parse_Attributes(pattern, parser))
    html_res = []
    for res in temp_res:
        html_res.append(res.decode_contents(formatter="html"))
    return  html_res

#find tagName
def parse_TagName(element):
    return element[(element.find('<') + 1):(element.find(' '))]

#attributes
def parse_Attributes(element, parser):    
    soup = BeautifulSoup(element, parser)
    e = soup.find(parse_TagName(element))
    return e.attrs;

