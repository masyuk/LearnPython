import re

mytext = " kaflk 213 l k sadfs2@com.com maxom gfoof.com akfs: asfs "

'''
\d - any digit 0-9
\D - any non DIGIT
\w - any alphabet symbol [A-Z a-z]
\W - any non alphabet symbol
\s - breakspace (probel)
\S - non breakspase

[0-9] => \d
[0-9]{3} - 3 подряд стоящие цифры

'''

textlookfor = r"maxom"
allresoults = re.findall(textlookfor, mytext)

print(allresoults)