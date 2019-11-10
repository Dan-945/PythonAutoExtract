import os, logging, rarfile
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s, - %(levelname)s %(message)s')

#Try to get working on windows, unsuccesful
#rarfile.UNRAR_TOOL = 'C:\\Program Files\\WinRAR\\UnRAR.exe'

#TODO log to txt file when done.
#for linux:
searchPath = r'/home/thebox/SeagateDisk/MediaFolder/testfolder'

#testfolder
#searchPath = 'Y:\\MediaFolder\\testfolder\\'
filesToExtract = []
os.chdir(searchPath)


#Search through folders to find all rar files to be extracted.
def folderContainsRar(folder):
    dir_listing = os.listdir(folder)
    for file in dir_listing:
        if file.endswith('.rar'):
            logging.info('rar file found')          
            if os.path.exists(os.path.join(folder,'unrared.txt')):
                logging.info('file already extracted, will be skipped')
            else:
                filesToExtract.append(os.path.join(searchPath, folder, file))
                logging.info('added for extracting')
    return

#walk through all folders to check content.
def searchFolders(searchPath):
    logging.debug('Searching through folder')
    for folderName, subFolders, fileNames in os.walk(searchPath):
        folderContainsRar(folderName)
    logging.info('Search complete')
    return

def unrar():
    for i in range (len(filesToExtract)):
        x = rarfile.RarFile(filesToExtract[i])
        x.extractall()
        os.mknod('unrared.txt')
        #x.close()
    return

searchFolders(searchPath)
logging.debug('Files to be extracted: %s ' % (filesToExtract))    
unrar()


#TODO skill ut kilder med og uten .rar lag liste med rene .mkv downloads og kopier disse til plex mappe.

#TODO legg inn ny fil med unrared for å unngå ny unraring.
