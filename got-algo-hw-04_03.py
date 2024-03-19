def show_phone(args):
    [name] = args
    with open('name_phone.txt', "r", encoding = "utf-8") as fh:
        lines = fh.readlines()
    lists = {}
    for line in lines:
        list_line = line.split(",")
        lists.update({list_line[0]: list_line[1].strip()})
    if name in lists:
        return(f"{name},{lists[name]}")
    else:
        return("Contact does not exist. Will you write it down?")         
        print("There is no such name") 
        