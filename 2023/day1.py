import os

file_path = os.path.dirname(os.path.abspath(__file__))
level_file_path = os.path.join(file_path, "input.txt")


with open(level_file_path) as f:
      data = f.read().strip()

print(data)
