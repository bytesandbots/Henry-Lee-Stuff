import os
def sortFiles(directory):
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        extension = filename[filename.index(".")+1:]
        if(os.path.exists(directory+"/"+extension)):
            #Moving file to folder
            os.rename(directory+"/"+filename, directory+"/"+extension+"/"+filename)
        else:
            os.makedirs(directory+"/"+extension)
            os.rename(directory+"/"+filename, directory+"/"+extension+"/"+filename)
def unsortFiles(directory):
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if not "." in filename:
            for subfolder in os.listdir(directory+"/"+filename):
                os.rename(directory+"/"+filename+"/"+subfolder,  directory+"/"+subfolder)
            os.rmdir(directory+"/"+filename)
sortorunsort = input("Sort or unsort file: ")
directoryask = input("What directory would you like to sort or unsort: ")
directory = "./"+directoryask
if sortorunsort == "sort":
    sortFiles(directory)
if sortorunsort == "unsort":
    unsortFiles(directory)
    



            
        
        
