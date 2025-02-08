### Regex findall

import re

text = "This is a brown fox"
pattern = "brown"

### Regex Findall Operations

search = re.search(pattern, text)
if search:
    print("Pattern found: ", search.group())
else:
    print("Pattern not found")

### Another solution of Findall operation
print("Pattern Found: ", re.search(pattern, text).group())

### Regex Match Operations

match = re.match(pattern, text)
if match:
    print("Match found: ", match.group())
else:
    print("Match Not found")


### ANother Solution
#print("Match Found: ", re.match(pattern, text).group())

### Regex replace operations
replacement = re.sub(pattern, "red", text)
print("Modified text: ", replacement)

pattern1 = " "
splitted_text = re.split(pattern1, text)
print("Splitted_text: ", splitted_text)

### Or can be done
print("Splitted_text: ", re.split(pattern1, text))