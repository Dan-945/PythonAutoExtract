import logging
import os
import sched
from datetime import time

import rarfile
from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=['settings.json'],
)
if not os.path.exists(os.path.join(os.getcwd(), "settings.json")):
    f = open("settings.json", "w")
    f.writelines("{")
    f.writelines("\"Source\":\"/Volumes/Downloads/Transmission/Completed/\",")
    f.writelines("\"Destination\":\"/Volumes/Downloads/Transmission/Temp/\"")
    f.writelines("}")
    f.close()
settings = Dynaconf(
    settings_files=['settings.json'],
)

#################### SETTINGS ########################################
source = settings.source
destination = settings.destination
#################### SETTINGS #######################################
logger = logging.getLogger('autoExtracter')
fh = logging.FileHandler('/Users/danhelgeland/PycharmProjects/PythonAutoExtract/autoExtractLog.txt')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s, - %(levelname)s %(message)s')
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s, - %(levelname)s %(message)s')
logger.addHandler(fh)
fh.setFormatter(formatter)

search_path = source
destination = destination

logging.disable(logging.DEBUG)
# Search through folders to find all rar files to be extracted.

tvShowEpisodeList = []
class Tvshowepisode():
    #setup all necessary info for extract / move a tvshowepisode
    file_path = ""
    file_type = ""
    file_name = ""
    destination = ""
    full_file_name = ""

    #method to handle file after init
    #when called, checks filetype and handles accordingly, also checks if already unrared / moved, to avoid duplicated
    def handle_file(self):
        #set fullname for use in functions further down.
        self.full_file_name = os.path.join(self.file_path, self.file_name)
        if self.file_type == "rar":
            x = rarfile.RarFile(self.full_file_name)
            x.extractall(self.destination)
            logger.debug('file will be extracted to %s' % (destination))
            try:
                #create file to avoid unraring again
                with open(os.path.join(self.file_path, 'unrared'), "a"):
                    logger.info("file created " + "unrared " + "at " + self.file_path)
            except Exception as e:
                logger.info(e)
        elif self.file_type == "mkv":
            #copy file to destination
            os.popen('cp ' + self.full_file_name + ' ' + destination + self.file_name)
            try:
                #create file to avoid copying again
                with open(os.path.join(self.file_path, self.file_name + 'copied'), "a"):
                    logger.info("file created " + "unrared " + "at " + self.file_path)
            except Exception as e:
                logger.info(e)
        else:
            logger.debug("filetype not detected")

def check_files_in_folder(folder):
    dir_listing = os.listdir(folder)
    #loop through files in folder, create tvShowEpisode class instance if not already unrared / copied
    for file in dir_listing:
        if file.endswith('.rar'):
            if os.path.exists(os.path.join(folder, 'unrared')):
                logger.debug('%s file already extracted, will be skipped' % (file))
            else:
                tmp = Tvshowepisode()
                tmp.file_name = file
                tmp.file_path = folder
                tmp.file_type = "rar"
                tmp.destination = destination
                tvShowEpisodeList.append(tmp)
        if file.endswith('.mkv'):
            if os.path.exists(os.path.join(folder,file+'copied')):
                  logger.debug('%s already copied, will be skipped' % (file))
            else:
                tmp = Tvshowepisode()
                tmp.file_name = file
                tmp.file_path = folder
                tmp.file_type = "mkv"
                tmp.destination = destination
                tvShowEpisodeList.append(tmp)
    return

# walk through all folders to check content.
def search_folders(searchPath):
    logger.info('Searching through folder')
    for folderName, subFolders, fileNames in os.walk(searchPath):
        check_files_in_folder(folderName)
    return

def do_something(scheduler):
    scheduler.enter(3600,1, do_something, (scheduler,))
    logger.info("Scheduler running")
    search_folders(search_path)
    logger.info('Search complete')
    logger.info('Starting unrar / copying files')
    for i in tvShowEpisodeList:
        i.handle_file()
    logger.info('Finished handling files')


my_scheduler = sched.scheduler(time.time, time.sleep)
my_scheduler.enter(5, 1, do_something, (my_scheduler,))
my_scheduler.run()