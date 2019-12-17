import csv

file_dir="/Users/siddharthabommireddy/Desktop/Python/"
with open(file_dir+'test.csv','r') as fname:
    print("Reading csv file method1")
    data = fname.read()
    print(data)


with open(file_dir+'test.csv','r') as filename:
    print("Reading csv file method2")
    data = csv.reader(filename)
    with open(file_dir+'out.csv','w') as fw:
        for line in data:
            fw.write(f'{line[0]} is of age {int(line[3])-10} \n')
            print(f'{line[0]} is of age {int(line[3])-10}')
            #print(type(line))
            try:
                age=int(line[3])-10
                print(f'{line[0]} new age {age}')
            except TypeError as err:
                print("Likhi and Bargu got the error", err)


#with open(file_dir+'out.csv','w') as filename:
    #employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL


with open(file_dir+'test.csv','r') as fr:
    with open(file_dir+'out1.csv','w') as fw:
        for line in fr:
            fw.write(line)
