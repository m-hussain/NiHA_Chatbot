from pyswip import Prolog

prolog = Prolog()

prolog.assertz("father(ali,hussain)")
prolog.assertz("father(ali,hassan)")
prolog.assertz("siblings(X,Y)")

result = prolog.query("father(X,Y)")

# result = list(prolog.query("father(ali,X)")) == [{'X':'hussain'},{'X','hussain'}]

for item in result:
    # print(item)
    # print(type(item))
    print(item['X']," is father of ",item['Y'])


prolog.consult("familyTreeKb.pl")

result = prolog.query("old(X)")
for item in result:
    # print(item)
    # print(type(item))
    print(item['X']," is old.")
