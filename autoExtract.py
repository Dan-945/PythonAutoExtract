import os, logging, rarfile, moveFiles
logger = logging.getLogger('autoExtracter')
fh = logging.FileHandler('/home/thebox/Scripts/autoExtractLog.txt')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s, - %(levelname)s %(message)s')
logger.addHandler(fh)
fh.setFormatter(formatter)
searchPath = r'/home/thebox/SeagateDisk/MediaFolder/testfolder'
logger.info('test')
filesToExtract = []

# Search through folders to find all rar files to be extracted.
def folderContainsRar(folder):
    dir_listing = os.listdir(folder)
    for file in dir_listing:
        if file.endswith('.rar'):
            logger.debug('rar file found')
            if os.path.exists(os.path.join(folder, 'unrared.txt')):
                logger.debug('%s file already extracted, will be skipped' % (file))
            else:
                filesToExtract.append(os.path.join(searchPath, folder, file))
                logger.info('%s added for extracting' % (file))
        if file.endswith('.mkv'):
            logger.debug('mkv file found')
            if os.path.exists(os.path.join(folder, 'copied.txt')):
                  logger.debug('file already copied, will be skipped')   
            else:
                #os.popen('cp '+(os.path.join(searchPath, folder, file))+' '+ moveFiles.fileSort(file)) #TODO missing filepath for skipped files
                logger.debug('file will be copied to %s' % (moveFiles.fileSort(file)))
                logger.info('%s file to be copied' % (file))
                os.mknod(os.path.join(searchPath,folder,'copied.txt'))
    return

# walk through all folders to check content.
def searchFolders(searchPath):
    logger.info('Searching through folder')
    for folderName, subFolders, fileNames in os.walk(searchPath):
        folderContainsRar(folderName)
    logger.info('Search complete')
    return

def unrar():
    for i in range(len(filesToExtract)):
        x = rarfile.RarFile(filesToExtract[i])
        #x.extractall(moveFiles.fileSort(os.path.basename(filesToExtract[i])))                        
        logger.debug('file will be extracted to %s' % (moveFiles.fileSort(os.path.basename(filesToExtract[i]))))
        os.mknod(os.path.join(os.path.dirname(filesToExtract[i]),'unrared.txt'))
        # x.close() #TODO do i need this?...
    return

searchFolders(searchPath)
logger.info('Files to be extracted: %s ' % (filesToExtract))

unrar()

