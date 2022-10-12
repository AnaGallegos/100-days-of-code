def filereader(file):
  """Read file and remove newline tag"""
  with open(file, "r") as file:
    f_read = file.readlines()
    f = [int(i.replace("\n", "")) for i in f_read]
    return f

file1 = filereader("file1.txt")
file2 = filereader("file2.txt")

common_numbers = [number for number in file1 if number in file2]

print(common_numbers)