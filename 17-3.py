#17-3
import re

#Main
contents = r"The ghost that says boo hounts the loo"
pattern = ".?oo"

repatter = re.compile(pattern)
result = repatter.findall(contents)

print(result)
