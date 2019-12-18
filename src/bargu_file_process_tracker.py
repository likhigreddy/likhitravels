
def file_processor(filename):

    return "processed"


files_list = ['file1.csv','file2.csv','file3.csv','file4.csv']
file_status_dict = {}

def main():
    for fname in files_list:
    #read list of files_list
    #Call function file_processor
        try:
            file_processor(fname)
            file_status_dict[fname] = 'Processed'
        except:
            file_status_dict[fname] = 'Failed'

    #if call fails or returns a status None then update the status as FAIL.
    #Update a Dictionary with file process status
    #print the final status for each file.
    for k,v in file_status_dict.items():
        print(f'{k} STATUS {v}')


if __name__ == "__main__":
    main()
