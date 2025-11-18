# read data
f = open('test.txt','r')
content = f.read()
print(content)
f.close()

#write data 

f = open('text.txt','w')
f.write("Hello I am here")
f.close()

#read csv file

import csv

try:
    with open('book.csv','r') as file:
        reader = csv.Reader(file)
        header = next(reader)
        print(header)
        print("-"*50)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("File not found")


import json

try:
    with open('./movies.json','r') as file:
        data = json.load(file)
        for movies in data:
            print(movies)
except FileNotFoundError:
    print('not found')

    with open('./movies.json','w') as f:
        json.dump(data.f)
    data = {
        "movies" : [
        {
            "id": 2,
            "title": "Avengers: Endgame",
            "description": "After the devastating events of Infinity War, the Avengers assemble once more to reverse Thanos' actions and restore balance to the universe.",
            "type": "Movie",
            "studio": "Marvel Studios",
            "date": "2019-04-26",
            "genre": ["Action", "Sci-Fi"],
            "votes": 1500000,
            "rating": 8.6,
            "comments": 75,
            "views": 105241,
            "imageUrl": "images/movie/movie-1.jpg"
        }
    ]
    }
    with open('./movies.json','a') as f:
        json.dump(data.f)