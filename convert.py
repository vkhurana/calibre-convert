import time
import subprocess
import os
import sys
import pyinotify
from os.path import exists
from pyinotify import WatchManager, Notifier, ProcessEvent, EventsCodes

def Monitor(path):
    class PClose(ProcessEvent):
        temp_folder = "temp"
        def process_IN_CLOSE(self, event):
            src_folder = event.path
            dest_folder = os.path.join(src_folder, self.temp_folder)
            src_file = event.name and os.path.join(event.path, event.name) or event.path
            dest_file_temp = os.path.join(dest_folder, event.name + ".mobi")
            print ("IN_CLOSE_WRITE event: " + src_file)
            print ("src_folder: " + src_folder)
            print ("dest_folder: " + dest_folder)
            print ("src_file: " + src_file)
            print ("dest_file_temp: " + dest_file_temp)

            if not exists(dest_folder):
                print("creating temp folder: " + dest_folder)
                os.mkdir(dest_folder)

            # we only really care about created events. 'modified' is another
            file_type = ".epub";
            if src_file.endswith(file_type):
                # pathinfo = os.path.split(src_file)
                dest_file = src_file + ".mobi"
                dest_exists = exists(dest_file)
                if not dest_exists:
                    print("Converting %s to %s" % (src_file, dest_file_temp))
                    cmd = "ebook-convert" + " \"" + src_file + "\" \"" + dest_file_temp + "\""
                    print("cmd: %s" % cmd)
                    ret = subprocess.call(cmd, shell=True)
                    print("ret: %d" % ret)
                    if ret == 0:
                        print("success converting. moving.")
                        os.rename(dest_file_temp, dest_file)
                    else:
                        print("error converting " + src_file)
                else:
                    print("Skipping. File %s exists" % dest_file)

    wm = WatchManager()
    notifier = Notifier(wm, PClose())
    wm.add_watch(path, pyinotify.IN_CLOSE_WRITE)

    try:
        while 1:
            notifier.process_events()
            if notifier.check_events():
                notifier.read_events()
    except KeyboardInterrupt:
        notifier.stop()
        return


if __name__ == '__main__':
    try:
        path = "/target"
    except IndexError:
        print ("error")
    else:
        print("Watching: %s" % path)
        Monitor(path)