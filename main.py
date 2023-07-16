import shutil
import os
import sys
import time
import threading

source = "C:/Users/stauc/Desktop/test/source"
replica = "C:/Users/stauc/Desktop/test/destination"

files = os.listdir(source)

class Syncronization():
    def syncFiles(self):
        shutil.rmtree(replica)
        os.mkdir(replica)
        for file_name in files:
            shutil.copy(source + "/" + file_name, replica + "/" + file_name)
        print("The sync has been succesfully done!")

    def createFile(self):
        f = open(source + '/' + 'new file', "w")
        self.syncFiles()
        print("A new file has been created!")

    def deleteFile(self):
        shutil.rmtree(replica)
        self.syncFiles()
        print("The file has been deleted!")

    def timedSync(self):
        threading.Timer(10, self.timedSync).start()
        time.sleep(10)
        self.syncFiles()


sync = Syncronization()
sync.syncFiles()



