# f = open('lesson.txt','r')
# print(f.name)
# print(f.mode)
# content = f.read()
# print(content)
# f.close()

# with open('./lesson.txt','w') as file:
#     file.write("Hello Python Write test \n")
#     file.write("Second Test")
# print("Success")

# with open('lesson.txt','a') as file:
#     file.write("New Data Add")
#     print("Success")

# try:
#     file = open('./lesson.txt','r')
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print('done')

# import csv

# with open('test.csv','w',newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name","Age","Grade"])
#     writer.writerow(["MgMg",20,"A"])
#     writer.writerow(["MgZaw",19,"B"])
#     writer.writerow(["MgHla",20,"A"])

# with open('./test.csv','r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# import json

# data = {
#     "name" : "Arkar Yan",
#     "age" : 24,
#     "Skill" : ["Python","Java","Flutter"]
# }
# with open('data.json','w') as file:
#     json.dump(data,file,indent=4)

# with open('./data.json','r') as file:
#     data =json.load(file)
#     print(data["name"])


# with open('example.txt','r+') as file:
#     file.write("New text add")
#     print(file.read())
#     print("success")

name =input("Enter Your name : ")
mark =input("Enter your mark : ")

with open('exam.txt','a') as file:
    file.write(f"{name}-{mark}\n")
    print("Data add success")