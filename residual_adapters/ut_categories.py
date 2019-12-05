input = "ut_categories.txt"

with open(input, 'r') as file:
    data = file.read().split('\n')
data1 = [s.strip('\t') for s in data]
file1 = open("ut_cate.txt", "w")
id = 120000001
for a in data1:
    file1.writelines(["{\"id\":" + str(id) + ",\"name\":\"" + str(a) + "\",\"supercategory\":\"utensils\"},\n"])
    id = id+1
file1.close()
print(len(data1))