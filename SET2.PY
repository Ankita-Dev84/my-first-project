a={1,3,5,7,9,11}
b={2,4,6,8,10,12}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(b.difference(a))
print(a.symmetric_difference(b))#elements that are in either a or b but not in both
print(a.issubset(b))
print(a.issuperset(b))
print(a.isdisjoint(b))
print(a.symmetric_difference_update(b))#updates a to be the symmetric difference of a and b
print(a.copy())
