from angi import angi
from gpa import gpa
from ner import ner
i = int(input())
a = angi[i]
g = gpa[i]
n = ner[i]
print("ner: "+ n)
print("angi: " + a)
print("gpa: "+ g)