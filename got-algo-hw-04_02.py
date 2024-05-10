def get_cats_info(path):
    try:
        with open(path, "r") as fh:  
            lines = fh.readlines()
            cats_info = []  
            for line in lines:
                line = line.strip().split(",")  
                cat_info = {"id": line[0], "name": line[1], "age": int(line[2])}
                cats_info.append(cat_info)  
    except FileNotFoundError:
        print("The file does not exist")
        return None 
    return cats_info


relative_path = "get_cats_info.txt"

cats_info = get_cats_info(relative_path)
if cats_info:
    print(cats_info)
