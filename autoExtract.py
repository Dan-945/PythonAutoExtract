import os, logging, zipfile
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s, - %(levelname)s %(message)s')


#TODO sett opp logging til logfil når ferdig.
#for linux:
# searchPath = r'/home/thebox/SeagateDisk/MediaFolder/completed'

#for windows:
#searchPath = r'Y:\MediaFolder\completed'

#testfolder
searchPath = r'Y:\MediaFolder\testfolder'
filesToExtract = []

def folderContainsRar(folder):
    dir_listing = os.listdir(folder)
    for file in dir_listing:
        if file.endswith('.rar'):
            filesToExtract.append(file)
            print('rar file found, added to list')

def searchFolders(searchPath):
    logging.debug('Searching through folder')
    for folderName, subFolders, fileNames in os.walk(searchPath):
        folderContainsRar(folderName)

searchFolders(searchPath)
logging.debug('Files to be extracted: %s ' % (filesToExtract))



#TODO søk igjennom download folder



#TODO skill ut kilder med og uten .rar lag liste med rene .mkv downloads og kopier disse til plex mappe.


#TODO extract nye filmer.

#TODO legg inn ny fil med unrared for å unngå ny unraring. 