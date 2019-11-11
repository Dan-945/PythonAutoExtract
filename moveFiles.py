import os, logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s, - %(levelname)s %(message)s')

#real destination
#destinationPath = r'/home/thebox/SeagateDisk/MediaFolder/PLEX MEDIA FOLDER'
#test destination
destinationPath = r'/home/thebox/SeagateDisk/MediaFolder/testfolder'

#sort file into folder based on beginning letter of filename.
#only filename expected as input
x = 'brooklyn.nine-nine.s06e01.multi.720p.web.h264-cielos.mkv'
def fileSort(file):
    destinationFolder = ''
    destinationFolder = file[0].upper()
    #print(destinationPath +'/'+ destinationFolder)
    return destinationPath +'/'+ destinationFolder
    
#fileSort(x)

#TODO flytt filer til ny folder for filmer brukt av plex


