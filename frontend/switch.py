import filecmp

class switch:

    global filename
    global onfile
    global offfile

    def __init__(self):
        self.filename = "switch.txt"
        self.onfile = "on.txt"
        self.offfile = "off.txt"
        with open(self.filename,"wr+") as opfile:
            opfile.truncate()

    def startService(self):
        with open(self.filename,"w") as opfile:
            opfile.write("on")

    def stopService(self):
        with open(self.filename,"w") as opfile:
            opfile.write("off")

    def retStatus(self):
        with open(self.filename,'r') as opfile:
            return opfile.read()

    def isOn(self):

        if(filecmp.cmp(self.filename, self.onfile)):
            return True
        else:
            return False
