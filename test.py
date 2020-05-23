#coding=utf-8
import langid                             #引入langid模块 

s1 = '你好'
s2 = 'hello'
s3 = 'Cours de développement professionnel pour les enseignants'

i = langid.classify(s1)
j = langid.classify(s2)
m = langid.classify(s3)

print (i,i[0],type(i))
print (j,j[0],type(j))
print (m,m[0],type(m))
