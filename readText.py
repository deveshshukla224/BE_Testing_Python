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
line_content = file.readlines()
for line in line_content:
    print(line)

#close whatever was opened
file.close()
# What is the output of the following code?
# Options