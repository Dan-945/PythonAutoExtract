import os, logging, rarfile, moveFiles

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s, - %(levelname)s %(message)s')
#logging.disable(logging.DEBUG)
# TODO log to txt file when done.
searchPath = r'/home/thebox/SeagateDisk/MediaFolder/testfolder'

filesToExtract = []
#os.chdir(searchPath) #Not necessary as all paths used are absolute?

# Search through folders to find all rar files to be extracted.
def folderContainsRar(folder):
    dir_listing = os.listdir(folder)
    for file in dir_listing:
        if file.endswith('.rar'):
            logging.debug('rar file found')
            if os.path.exists(os.path.join(folder, 'unrared.txt')):
                logging.debug('%s file already extracted, will be skipped' % (file))
            else:
                filesToExtract.append(os.path.join(searchPath, folder, file))
                logging.info('%s added for extracting' % (file))
        if file.endswith('.mkv'):
            logging.debug('mkv file found')
            if os.path.exists(os.path.join(folder, 'copied.txt')):
                  logging.debug('file already copied, will be skipped')   
            else:
                #os.popen('cp'+(os.path.join(searchPath, folder, file))+ moveFiles.fileSort(file)) #TODO sorting function needed
                logging.debug('file will be copied to %s' % (moveFiles.fileSort(file)))
                logging.info('%s file to be copied' % (file))
    return

# walk through all folders to check content.
def searchFolders(searchPath):
    logging.info('Searching through folder')
    for folderName, subFolders, fileNames in os.walk(searchPath):
        folderContainsRar(folderName)
    logging.info('Search complete')
    return

def unrar():
    for i in range(len(filesToExtract)):
        x = rarfile.RarFile(filesToExtract[i])
        #x.extractall(moveFiles.fileSort(filesToExtract[i]))                          #TODO sorting function needed
        logging.debug('file will be extracted to %s' % (moveFiles.fileSort(filesToExtract[i])))
        os.mknod(os.path.join(os.path.dirname(filesToExtract[i]),'unrared.txt'))
        # x.close() #TODO do i need this?...
    return

searchFolders(searchPath)
logging.info('Files to be extracted: %s ' % (filesToExtract))

unrar()

#TODO sorting function needed