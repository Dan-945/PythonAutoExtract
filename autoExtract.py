import os, logging, rarfile

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s, - %(levelname)s %(message)s')

# TODO log to txt file when done.
searchPath = r'/home/thebox/SeagateDisk/MediaFolder/completed'

filesToExtract = []
os.chdir(searchPath)

# Search through folders to find all rar files to be extracted.
def folderContainsRar(folder):
    dir_listing = os.listdir(folder)
    for file in dir_listing:
        if file.endswith('.rar'):
            logging.info('rar file found')
            if os.path.exists(os.path.join(folder, 'unrared.txt')):
                logging.info('file already extracted, will be skipped') #TODO legg til kort beskrivelse av sti.
            else:
                filesToExtract.append(os.path.join(searchPath, folder, file))
                logging.info('added for extracting') #TODO legg til kort beskrivelse av sti.
    return

# walk through all folders to check content.
def searchFolders(searchPath):
    logging.debug('Searching through folder')
    for folderName, subFolders, fileNames in os.walk(searchPath):
        folderContainsRar(folderName)
    logging.info('Search complete')
    return

def unrar():
    for i in range(len(filesToExtract)):
        x = rarfile.RarFile(filesToExtract[i])
        x.extractall()                          #TODO make handling for placement of extracted files.
        os.mknod(os.path.join(os.path.dirname(filesToExtract[i]),'unrared.txt'))
        # x.close() #TODO do i need this?...
    return

searchFolders(searchPath)
logging.debug('Files to be extracted: %s ' % (filesToExtract))

#unrar()

# TODO skill ut kilder med og uten .rar lag liste med rene .mkv downloads og kopier disse til plex mappe.

#Dette er en test for å se at endringer skjer på server2