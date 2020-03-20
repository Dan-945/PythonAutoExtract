import os, logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s, - %(levelname)s - %(message)s')

libPath = '/home/thebox/SeagateDisk/MediaFolder/plexMediaFolder/'
alphabet = []

# Make list of A-Z
for x in range(ord('a'), ord('z') + 1):
    # print (str(chr(x)))
    # print((str(chr(x))).upper())
    alphabet.append(str(chr(x).upper()))

# print(alphabet[1])

list_len = len(alphabet)

# print(list_len)
# print(enumerate(alphabet))

# loop for generating directory inside libPath, with names of alphabet list
for letter in range(list_len):
    path = os.path.join(libPath, alphabet[letter])
    logging.debug('path to be created %s' % (path))
    os.mkdir(path)
    # print(alphabet[letter])