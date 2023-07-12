import logging
import moveFiles
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
logger.addHandler(fh)
fh.setFormatter(formatter)

searchPath = source
destination = destination

filesToExtract = []
logging.disable(logging.DEBUG)
# Search through folders to find all rar files to be extracted.

tvShowEpisodeList = []
class tvShowEpisode():
    filePath = ""
    fileType = ""
    fileName = ""
    destination = ""
    handled = False
    fullFileName = ""
    def handleFile(self):
        self.fullFileName = self.filePath + "/" +  self.fileName
        if self.fileType == "rar":
            if os.path.exists(os.path.join(self.filePath, 'unrared')):
                logger.debug('%s file already extracted, will be skipped' % (self.fileName))
            else:
                x = rarfile.RarFile(self.fullFileName)
                x.extractall(self.destination)
                logger.info('file will be extracted to %s' % (destination))
                try:
                    with open(os.path.join(self.filePath,'unrared'),"a"):
                        logger.info("file created " + "unrared" + "at " + self.filePath)
                    #os.mknod(os.path.join(self.filePath,'unrared'))
                except Exception as e:
                    logger.info(e)
        elif self.fileType == "mkv":
            os.popen('cp ' + self.fullFileName + ' ' + destination + self.fileName)
        else:
            logger.debug("filetype not detected")

def folderContainsRar(folder):
    dir_listing = os.listdir(folder)
    fileToBeCopied = ''
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
                """filesToExtract.append(os.path.join(searchPath, folder, file))
                logger.info('%s added for extracting' % (file))"""

        if file.endswith('.mkv'):
            if os.path.exists(os.path.join(folder,file+'copied')):
                  logger.debug('%s already copied, will be skipped' % (file))   
            else:
                tmp = tvShowEpisode()
                tmp.fileName = file
                tmp.filePath = searchPath + folder
                tmp.fileType = "mkv"
                tmp.destination = destination
                tvShowEpisodeList.append(tmp)
                fileToBeCopied = (os.path.join(searchPath, folder, file))
                """if os.path.exists(fileToBeCopied):
                    os.popen('cp '+(os.path.join(searchPath, folder, file))+' '+ moveFiles.fileSort(file))
                    os.popen()
                    logger.debug('%s file will be copied to %s' % ( (os.path.join(searchPath, folder, file)), moveFiles.fileSort(file)))
                    logger.info('%s file to be copied' % (file))
                    #os.mknod(os.path.join(searchPath,folder,file+'copied.txt'))
                else:
                    logger.error('file does not exist')"""
    return

# walk through all folders to check content.
def searchFolders(searchPath):
    logger.info('Searching through folder')
    for folderName, subFolders, fileNames in os.walk(searchPath):
        folderContainsRar(folderName)
    return

def unrar():
    for i in range(len(filesToExtract)):
        x = rarfile.RarFile(filesToExtract[i])
        x.extractall(moveFiles.fileSort(os.path.basename(filesToExtract[i])))
        logger.debug('file will be extracted to %s' % (moveFiles.fileSort(os.path.basename(filesToExtract[i]))))
        try:
            os.mknod(os.path.join(os.path.dirname(filesToExtract[i]),'unrared.txt'))
        except:
            logger.debug('file already exists, multiple rar files')
        #x.close() #TODO do i need this?...
    return

searchFolders(searchPath)
logger.info('Search complete')
logger.info('Starting unrar / copying files')
for i in tvShowEpisodeList:
    i.handleFile()
logger.info('Finished handling files')
#unrar()

