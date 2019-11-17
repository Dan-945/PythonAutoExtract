import os, logging, rarfile, moveFiles, shutil
logger = logging.getLogger('autoExtracter')
fh = logging.FileHandler('/home/thebox/Scripts/Logs/autoExtractLog.txt')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s, - %(levelname)s %(message)s')
logger.addHandler(fh)
fh.setFormatter(formatter)

logging.disable(logging.DEBUG)

searchPath = r'/home/thebox/SeagateDisk/MediaFolder/completed'
filesToExtract = []

# Search through folders to find all rar files to be extracted.
def folderContainsRar(folder):
    dir_listing = os.listdir(folder)
    fileToBeCopied = ''
    for file in dir_listing:
        if file.endswith('.rar'):
            if os.path.exists(os.path.join(folder, 'unrared.txt')):
                logger.debug('%s file already extracted, will be skipped' % (file))
            else:
                filesToExtract.append(os.path.join(searchPath, folder, file))
                logger.info('%s added for extracting' % (file))
        if file.endswith('.mkv'):
            if os.path.exists(os.path.join(searchPath,folder,file+'copied.txt')):
                  logger.debug('%s already copied, will be skipped' % (file))   
            else:
                fileToBeCopied = (os.path.join(searchPath, folder, file))
                if os.path.exists(fileToBeCopied):
                    #os.popen('cp '+(os.path.join(searchPath, folder, file))+' '+ moveFiles.fileSort(file))
                    logger.debug('%s file will be copied to %s' % ( (os.path.join(searchPath, folder, file)), moveFiles.fileSort(file)))
                    logger.info('%s file to be copied' % (file))
                    os.mknod(os.path.join(searchPath,folder,file+'copied.txt'))
                else:
                    logger.error('file does not exist')
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
        os.mknod(os.path.join(os.path.dirname(filesToExtract[i]),'unrared.txt'))
        x.close() #TODO do i need this?...
    return

searchFolders(searchPath)
logger.info('Search complete')
unrar()

