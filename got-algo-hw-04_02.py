with open("get_cats_info.txt","w") as fh:
    fh.write("60b90c1c13067a15887e1ae1,Tayson,3\n60b90c2413067a15887e1ae2,Vika,1\n60b90c2e13067a15887e1ae3,Barsik,2\n60b90c3b13067a15887e1ae4,Simon,12\n60b90c4613067a15887e1ae5,Tessi,5")
   
with open("get_cats_info.txt","r") as fh:
    lines = fh.readlines()
    dictionary = []
    for line in lines:
        line = line.split(",")
        dictionary.append(line)
        cats_info = {}
        for cats in dictionary:
            cats_info.update({"id":cats[0]})
            cats_info.update({"name":cats[1]})
            cats_info.update({"age":int(cats[2])}) 
            
            
print(cats_info)             
                       