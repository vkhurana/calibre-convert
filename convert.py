import time
import subprocess
import os
from os.path import exists
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:
    DIRECTORY_TO_WATCH = "/target"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        print("Watching: %s" %self.DIRECTORY_TO_WATCH)
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
            print("Error starting watcher. Does the folder exist?")

        self.observer.join()

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # we only really care about created events. 'modified' is another
            srcfile = event.src_path;
            filetype = ".epub";
            if srcfile.endswith(filetype):
                # pathinfo = os.path.split(srcfile)
                destfile = srcfile + ".mobi"
                print("Received created event - %s" % srcfile)
                dest_exists = exists(destfile)
                if not dest_exists:
                    print("Converting %s to %s" % (srcfile, destfile))
                    cmd = "ebook-convert" + " \"" + srcfile + "\" \"" + destfile + "\""
                    print("cmd: %s" % cmd)
                    ret = subprocess.call(cmd, shell=True)
                    print("ret: %d" % ret)
                else:
                    print("Skipping. File %s exists" % destfile)

if __name__ == '__main__':
    w = Watcher()
    w.run()