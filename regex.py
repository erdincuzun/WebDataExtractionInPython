import re

#extract one result
def extract(html, pattern):
    res = re.search(prepare_regex(pattern), html, re.DOTALL)
    if res:
        return res.group(1)
    else:
        return ''

#extract all result
def extract_all(html, pattern):
    return  re.findall(prepare_regex(pattern), html, re.DOTALL)

#prepare regex
def prepare_regex(pattern):
    return pattern.replace(" ", ".").replace("\"", ".").replace("'", ".").replace("=", ".") + "(.*?)" + "</" + parse_TagName(pattern) + ">"

#find tagName
def parse_TagName(element):
    return element[(element.find('<') + 1):(element.find(' '))]
