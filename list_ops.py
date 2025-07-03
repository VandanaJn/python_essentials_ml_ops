items=["a","b","c","d","e"]
print(items[2:])
print(items[2:10])
print(items[2:2])
print(items[2:3])
print(items[2:4])
print(items[-1:])
print(items[-1:-4:-2])

list1=[1,3,6]
list1.extend(items)
print(list1)
submissions = ["armbar", "triangle", "kimura", "guillotine"]
combos=[f"{a} {b}"   for a in submissions for b in submissions if a!=b]
print (combos)