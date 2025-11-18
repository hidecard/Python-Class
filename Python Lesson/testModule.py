# import os

# print(os.getcwd)
# os.mkdir("TestFolder")

# import sys

# print(sys.version)

# import datetime

# now = datetime.datetime.now()
# print(now.strftime("%Y-%m-%d %H:%M:%S"))

# import json

# data = {"name": "Arkar", "age": 20}
# data_json = json.dumps(data)

# print(data_json)

# import calendar

# print(calendar.month(2025, 12))

# import random

# print(random.randint(1,10))

from collections import Counter
nums = [1, 2, 2, 3, 3, 3,4,5,6,3,4,5,6,7]
print(Counter(nums))