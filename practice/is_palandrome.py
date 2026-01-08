import re 
def is_palendrome(string):
    string=string.lower()
    cleaned=re.sub(r'[^a-z0-9]',"",string)
    #re.sub(pattern, replacement, string)
    return cleaned==cleaned[::-1]

#regular expression (regex) is a powerful pattern-matching language used to 
# find, extract, validate, and manipulate text
my_input="A man , a plan a canal: panama"
print(is_palendrome(my_input))