#17-2
import re


#Main

content = r'Arizona 479 ,501 , 870. California 209 , 213 , 650'
pattern = "[0-9]"

repatter = re.compile(pattern)
result = repatter.findall(content)
#result = re.match(pattern, content)

print(result)
print(result.groups())
