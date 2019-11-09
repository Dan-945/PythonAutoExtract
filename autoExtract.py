import os, logging, rarfile

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s, - %(levelname)s %(message)s')
rarfile.UNRAR_TOOL = 'C:\\Program Files\\WinRAR\\UnRAR.exe'


#TODO sett opp logging til logfil når ferdig.
#for linux:
# searchPath = r'/home/thebox/SeagateDisk/MediaFolder/completed'

#for windows:
#searchPath = r'Y:\MediaFolder\completed'

#testfolder
searchPath = 'Y:\\MediaFolder\\testfolder\\'
filesToExtract = []
os.chdir(searchPath)

def folderContainsRar(folder):
    dir_listing = os.listdir(folder)
    for file in dir_listing:
        if file.endswith('.rar'):

            filesToExtract.append(os.path.join(searchPath, folder, file))
            print('rar file found, added to list')
    return

def searchFolders(searchPath):
    logging.debug('Searching through folder')
    for folderName, subFolders, fileNames in os.walk(searchPath):
        folderContainsRar(folderName)
    return
searchFolders(searchPath)
logging.debug('Files to be extracted: %s ' % (filesToExtract))

def unrar():
    for i in range (len(filesToExtract)):
        x = rarfile.RarFile(filesToExtract[i])
        x.extractall()
        #x.close()
    return
unrar()
#TODO skill ut kilder med og uten .rar lag liste med rene .mkv downloads og kopier disse til plex mappe.

#TODO extract nye filmer.

#TODO legg inn ny fil med unrared for å unngå ny unraring.
