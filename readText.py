file = open('/home/devslane-75/Devesh/be_python_automation_testing/abc.text')
#open the file

#read all the content of the file
#print(file.read())


#read the first 10 characters of the file
#print(file.read(10))


#read the first line of the file
#print(file.readline())
#continue reading the next line
#print(file.readline())

#read all the lines of the file
#readlines() method returns a list of all the lines in the file
line_content = file.readlines()
print(line_content)
for line in line_content:
    print(line)

#close whatever was opened
file.close()
# What is the output of the following code?
# Options




#if one does not want to close the file explicitly, one can use the with statement
#with statement automatically closes the file when the block of code is exited
# with open('/home/devslane-75/Devesh/be_python_automation_testing/abc.text') as file:
#     print(file.read())
#     print(file.readline())
#     print(file.readlines())
#     print(file.read(10))