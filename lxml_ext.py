from lxml import etree
from io import StringIO

def extract_all(html, pattern):
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(html), parser)
    result = etree.tostring(tree.getroot())
    root = tree.getroot()
    my_list = []
    yol = prepare_XPath2(pattern)
    for elem in root.findall(yol):
        my_list.append(etree.tostring(elem, encoding='unicode'))
    return my_list

def extract(html, pattern):
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(html), parser)
    result = etree.tostring(tree.getroot())
    root = tree.getroot()
    elem = root.find(prepare_XPath2(pattern))
    return etree.tostring(elem, encoding='unicode')

#and problem
def prepare_XPath(pattern):
    root = etree.fromstring(pattern + '</' + parse_TagName(pattern) + '>')
    temp=''
    for att in root.keys():
        if temp == "":
            temp = '@'+ att + "='" + root.get(att) + "'"
        else:
            temp += ' and @'+ att + "='" + root.get(att) + "'"
    return ".//" + root.tag + "[" + temp + "]"

def prepare_XPath2(pattern):
    root = etree.fromstring(pattern + '</' + parse_TagName(pattern) + '>')
    temp=''
    for att in root.keys():
        temp += '[@'+ att + "='" + root.get(att) + "']"
    return ".//" + root.tag + temp

def parse_TagName(element):
    return element[(element.find('<') + 1):(element.find(' '))]
