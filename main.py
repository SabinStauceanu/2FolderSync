import shutil
import os
import sys
import time
import threading

if sys.argv[2] == "-s":
    source = sys.argv[3]
if sys.argv[4] == "-r":
    replica = sys.argv[5]

class Syncronization():
    def syncFiles(self):
        shutil.rmtree(replica)
        os.mkdir(replica)
        files = os.listdir(source)
        for file_name in files:
            shutil.copy(source + "/" + file_name, replica + "/" + file_name)
        print("The sync has been succesfully done!")

    def createFile(self):
        f = open(source + '/' + sys.argv[6], "w")
        print("A new file has been created!")
        self.syncFiles()


    def deleteFile(self):
        if os.path.exists(source + '/' + sys.argv[6]):
            os.remove(source + '/' + sys.argv[6])
            print("The file has been deleted!")
            self.syncFiles()
        else:
            print("The specified file doesnt exist!")


    def timedSync(self):
        threading.Timer(int(sys.argv[6]), self.timedSync).start()
        time.sleep(int(sys.argv[6]))
        self.syncFiles()


sync = Syncronization()

if sys.argv[1] == "--s":
    sync.syncFiles()
elif sys.argv[1] == "--c":
    sync.createFile()
elif sys.argv[1] == "--d":
    sync.deleteFile()
elif sys.argv[1] == "--t":
    sync.timedSync()




