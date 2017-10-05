import thread
import time
from .models import *
import threading
import subprocess
import filecmp


class service:

    global switch

    def __init__(self, switch):
        self.switch = switch

    def runThreads(self):
        print('[+] Service Started')
        backups = backupFolder.objects.all()
        while(self.switch.isOn()):
            results = backupFolder.objects.all()
            for i in results:
                thread = backupThread(i.id, i.name, i.path, i.backupPath)
                thread.start()
            time.sleep(20)

    def runThread(self):
        thread.start_new_thread(self.runThreads,())
        return 0

class backupThread(threading.Thread):

    def __init__(self, id, name, path, backupPath):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name
        self.path = path
        self.backupPath = backupPath

    def run(self):
        #backup script
        #/Desktop/Study Material/5th sem/Operating Systems/Project/Test/source/source-3
        templist = subprocess.Popen(['ls -l ' + self.path + ' >> '+ self.path +'/.new_state.txt'], stdout=subprocess.PIPE, shell=True)

        tempchange = subprocess.Popen(['cmp '+self.path+'/.new_state.txt '+self.path+'/.old_state.txt'], stdout=subprocess.PIPE, shell=True)
        output, err = tempchange.communicate()

        if(output):
            self.change = True
        else:
            self.change = False

        print("[+] "+ str(self.backup(self.change)))

        subprocess.Popen(['mv '+self.path+'/.new_state.txt '+self.path+'/.old_state.txt'],stdout=subprocess.PIPE, shell=True)

    def backup(self, change):

        if(change):
            tempdel = subprocess.Popen(['rm -rvf '+self.backupPath+'/'],stdout=subprocess.PIPE, shell=True)
            tempback = subprocess.Popen(['cp -a '+self.path+'/. '+self.backupPath+'/'],stdout=subprocess.PIPE, shell=True)
            return "Backup done"
        else:
            return 0
