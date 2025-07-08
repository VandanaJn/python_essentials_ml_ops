def linear_search(data, items):
    items_dict={i:[] for i in items} 
    for idx,element in enumerate(data):
        if element in items_dict:
            items_dict[element].append(idx)
    return items_dict 
import sys
if __name__=="__main__":
    list=["one","two","five","eleven","eleven"]  
    if len(sys.argv)>=2:
        print(linear_search(list,sys.argv[1:]))




    

