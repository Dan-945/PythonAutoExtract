import os, logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s, - %(levelname)s %(message)s')

#real destination
destinationPath = r'/home/thebox/SeagateDisk/MediaFolder/plexMediaFolder'
#test destination
#destinationPath = r'/home/thebox/SeagateDisk/MediaFolder/testfolder'

#sort file into folder based on beginning letter of filename.
#only filename expected as input
def fileSort(file):
    destinationFolder = ''
    destinationFolder = file[0].upper()
    finalDestination = destinationPath+'/'+destinationFolder
    #print(destinationPath +'/'+ destinationFolder)
    
    return finalDestination


