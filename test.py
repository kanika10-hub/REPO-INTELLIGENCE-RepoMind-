from tools.file_tools import *

print(list_files("./test_repo"))

print("\n-----------------\n")

print(read_file("./test_repo/main.py"))

print("\n-----------------\n")

print(search_text("./test_repo", "login"))