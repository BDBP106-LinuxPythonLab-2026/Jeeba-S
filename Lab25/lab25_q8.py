import re

text = input("Enter some text: ")

def mask(match):
    local = match.group(1)      # part before @
    domain = match.group(2)     # part after @
    if len(local) <= 2:
        masked = "*" * len(local)
    else:
        masked = local[0] + "*" * (len(local) - 2) + local[-1]
    return masked + "@" + domain

pattern = r"([\w.+-]+)@([\w-]+(?:\.[\w-]+)+)"
print(re.sub(pattern, mask, text))