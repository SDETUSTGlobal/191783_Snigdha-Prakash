import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
    print("The pattern exists")
else:
    print("The pattern not exists")
