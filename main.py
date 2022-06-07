def replace():
  with open('C:/Users/shalu/Desktop/example.txt', 'r') as file :
    filedata = file.read()

# Replace the target string
  filedata = filedata.replace('placement', 'screening')

# Write the file out again
  with open('C:/Users/shalu/Desktop/example.txt', 'w') as file:
    file.write(filedata)