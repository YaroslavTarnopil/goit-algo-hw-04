with open("get_cats_info.txt","w") as fh:
    fh.write("60b90c1c13067a15887e1ae1,Tayson,3\n60b90c2413067a15887e1ae2,Vika,1\n60b90c2e13067a15887e1ae3,Barsik,2\n60b90c3b13067a15887e1ae4,Simon,12\n60b90c4613067a15887e1ae5,Tessi,5")
       
def get_cats_info(patch):
    try:
        with open("get_cats_info.txt","r") as fh:
            lines = fh.readlines()
            lists = []
            dictionary = {}
        for line in lines:
            line = line.split(",")
            lists.append(line)
            cats_info = {}
            dictionary["id"] = line[0]
            dictionary["name"] = line[1]
            dictionary["age"] = int(line[2])  
    except:
        print("The file does not exist")
    return(lists)

cats_info = get_cats_info("path/to/get_cats_info.txt")
print(cats_info)
