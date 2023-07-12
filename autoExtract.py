import logging
import os
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
fh = logging.FileHandler('autoExtractLog.txt')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s, - %(levelname)s %(message)s')
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s, - %(levelname)s %(message)s')
logger.addHandler(fh)
fh.setFormatter(formatter)

searchPath = source
destination = destination

filesToExtract = []
logging.disable(logging.DEBUG)
# Search through folders to find all rar files to be extracted.

tvShowEpisodeList = []
class tvShowEpisode():
    #setup all necessary info for extract / move a tvshowepisode
    filePath = ""
    fileType = ""
    fileName = ""
    destination = ""
    fullFileName = ""

    #method to handle file after init
    #when called, checks filetype and handles accordingly, also checks if already unrared / moved, to avoid duplicated
    def handleFile(self):
        #set fullname for use in functions further down.
        self.fullFileName = os.path.join(self.filePath , self.fileName)
        if self.fileType == "rar":
            x = rarfile.RarFile(self.fullFileName)
            x.extractall(self.destination)
            logger.debug('file will be extracted to %s' % (destination))
            try:
                #create file to avoid unraring again
                with open(os.path.join(self.filePath,'unrared'),"a"):
                    logger.info("file created " + "unrared " + "at " + self.filePath)
            except Exception as e:
                logger.info(e)
        elif self.fileType == "mkv":
            #copy file to destination
            os.popen('cp ' + self.fullFileName + ' ' + destination + self.fileName)
            try:
                #create file to avoid copying again
                with open(os.path.join(self.filePath, self.fileName+ 'copied'), "a"):
                    logger.info("file created " + "unrared " + "at " + self.filePath)
            except Exception as e:
                logger.info(e)
        else:
            logger.debug("filetype not detected")

def checkFilesInFolder(folder):
    dir_listing = os.listdir(folder)
    #loop through files in folder, create tvShowEpisode class instance if not already unrared / copied
    for file in dir_listing:
        if file.endswith('.rar'):
            if os.path.exists(os.path.join(folder, 'unrared')):
                logger.debug('%s file already extracted, will be skipped' % (file))
            else:
                tmp = tvShowEpisode()
                tmp.fileName = file
                tmp.filePath = folder
                tmp.fileType = "rar"
                tmp.destination = destination
                tvShowEpisodeList.append(tmp)
        if file.endswith('.mkv'):
            if os.path.exists(os.path.join(folder,file+'copied')):
                  logger.debug('%s already copied, will be skipped' % (file))
            else:
                tmp = tvShowEpisode()
                tmp.fileName = file
                tmp.filePath = folder
                tmp.fileType = "mkv"
                tmp.destination = destination
                tvShowEpisodeList.append(tmp)
    return

# walk through all folders to check content.
def searchFolders(searchPath):
    logger.info('Searching through folder')
    for folderName, subFolders, fileNames in os.walk(searchPath):
        checkFilesInFolder(folderName)
    return

searchFolders(searchPath)
logger.info('Search complete')
logger.info('Starting unrar / copying files')
for i in tvShowEpisodeList:
    i.handleFile()
logger.info('Finished handling files')
#unrar()

