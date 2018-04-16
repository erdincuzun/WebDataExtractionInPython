# Web Data Extraction In Python
This project examine web content extraction libraries including beautifulsoup, lxml and regex. You give only element information and extraction pattern is prepared with functions. 

# lxml
Some web sites introduced BeautifulSoup recommend to install and use lxml for speed. But also, it can be used stand-alone and it is more efficient.
```python
import lxml_ext

result_list = lxml_ext.extract_all(data, pattern)
result = lxml_ext.extract(data, pattern)
```
data: web page
pattern: html element, <h1 class="test">

extract_all method returns all extractions for a pattern in a web page, as a list of strings. extract method returns the first extraction result in a web page, as string.

# BeautifulSoup
The different parsers including html.parser, lxml, and html5lib can be used in BeautifulSoup. For example:

```python
import bsoup
parser = html.parser
result_list = bsoup.extract_all(data, pattern, parser)
result = bsoup.extract(data, pattern, parser)
```

#Regex
Regular expressions are well-known and efficient technique that can be used in extraction process. However, it can cause problems when the number of inner tags is ambiguous.
```python
import regex
result_list = regex.extract_all(data, pattern, parser)
result = regex.extract(data, pattern, parser)
```

