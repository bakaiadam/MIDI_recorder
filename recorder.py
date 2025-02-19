import time
import rtmidi
#import from parrentdir
import sys
import os
import inspect


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from CK_rec.setup import Setup
from CK_rec.rec_classes import CK_rec


# Start the Device
codeK = Setup()
myPort = codeK.perform_setup()
codeK.open_port(myPort)
on_id = codeK.get_device_id()
#print('your note on id is: ', on_id)

# record
midiRec = CK_rec(myPort, on_id, debug=False)
codeK.set_callback(midiRec)
midiRec.called=False
i=0

# Loop to program to keep listening for midi input
try:
    while True:
        time.sleep(1)
        sys.exit(0)
        print(i)
        if (midiRec.called==False):
          i=i+1
        if (midiRec.called==True):
          i=0
        print(i,midiRec.called)
        midiRec.called=False
        print(i,midiRec.called)

        
except KeyboardInterrupt:
    print('')
finally:
#    name = input('\nsave midi recording as? (leaving the name blank discards the recording): ')
#    if name != "":
#        midiRec.saveTrack(name)
    codeK.end()
