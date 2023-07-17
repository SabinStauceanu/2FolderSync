import shutil
import os
import sys
import time
import threading
import logging

logging.basicConfig(filename='logging.log',level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

# The source folder and replica folder are stored in in "source" and "replica" variables from console
if sys.argv[2] == "-s":
    source = sys.argv[3]
if sys.argv[4] == "-r":
    replica = sys.argv[5]


class Syncronization():
    #Copying files method
    def syncFiles(self):
        # First we delete the replica folder
        shutil.rmtree(replica)
        # Then we recreate the replica folder
        os.mkdir(replica)
        #We store all the files from the source folder in "files" variable
        files = os.listdir(source)
        #Then we will copy all the files from the source to the replica folder
        for file_name in files:
            shutil.copy(source + "/" + file_name, replica + "/" + file_name)
        print("The sync has been succesfully done!")
        logging.info("The sync has been succesfully done!")

    #Create file method
    def createFile(self):
        #The file name we will get from console input and we will check if the file exist
        if os.path.exists(source + '/' + sys.argv[6]):
            print("The "+ " " + sys.argv[6] + " " + " file already exist!")
        else:
            f = open(source + '/' + sys.argv[6], "w")
            print("The "+ " " + sys.argv[6] + " " + " file has been created!")
            logging.info("The "+ " " + sys.argv[6] + " " + " file has been created!")
            self.syncFiles()


    #Delete file method
    def deleteFile(self):
        #If the file exists we delete it otherwise we will display an error message
        if os.path.exists(source + '/' + sys.argv[6]):
            os.remove(source + '/' + sys.argv[6])
            print("The "+ " " + sys.argv[6] + " " + " file has been deleted!")
            logging.info("The "+ " " + sys.argv[6] + " " + " file has been deleted!")
            self.syncFiles()
        else:
            print("The specified file doesnt exist!")


    #Periodical syncronisation method
    def timedSync(self):
        # From console input we will get how many second the syncronisation will occur in a loop
        threading.Timer(int(sys.argv[6]), self.timedSync).start()
        time.sleep(int(sys.argv[6]))
        self.syncFiles()


sync = Syncronization()

# Depending on the second argument in console we will decide if we copy,create,delete or time our syncronisation
if sys.argv[1] == "--s":
    sync.syncFiles()
elif sys.argv[1] == "--c":
    sync.createFile()
elif sys.argv[1] == "--d":
    sync.deleteFile()
elif sys.argv[1] == "--t":
    sync.timedSync()
else:
    print("You introduced an invalid command!")




