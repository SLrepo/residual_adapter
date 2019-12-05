input = "home_office_categories.txt"

with open(input, 'r') as file:
    data = file.read().replace("\n", "").split(', ')

file1 = open("home_office_cate.txt", "w")
id = 110000001
for a in data:
    file1.writelines(["{\"id\":" + str(id) + ",\"name\":\"" + str(a) + "\",\"supercategory\":\"homeoffice\"},\n"])
    id = id+1
file1.close()
print(len(data))