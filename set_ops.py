set1={
    'a','b','c'
}
set2={
    'a','c','d'
}
print(set1.intersection(set2))
print(set1.difference(set2))#in set1 but not in set2
print(set1.symmetric_difference(set2))#in set1 but not in set2, in set2 not in set1
print(set1)
print(set1.difference_update(set2))#update set1 with items found in other, does not return
print(set1)
set1={
    'a','b','c'
}
set2={
    'a','c','d'
}
print(set1.symmetric_difference_update(set2))#update set1 found with iems found in either not in both
print(set1)
print(set2)

list1 =['1','2','2','1']
set3=set(list1)
print(set3)
