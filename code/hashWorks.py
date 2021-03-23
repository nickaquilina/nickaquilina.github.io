import os
import base64
import hashlib


def generateSha256(filePath, bufferSize = 8192):
    """ Accepts a path for a file and returns a Base 64 encoded SHA256 Digest.
    """
    if os.path.isfile(filePath):
        hasher = hashlib.sha256()
        with open(filePath, "rb") as fl:
            readBuffer = fl.read(bufferSize)
            while len(readBuffer) > 0:
                hasher.update(readBuffer)
                readBuffer = fl.read(bufferSize)
            hashDigest = hasher.digest()
            
            return base64.encodebytes(hashDigest).decode().strip("\n")
            
    else:
        return None

# Test
testDir = "D:\Programming\Python\libraries\metricsLib"

for f in os.listdir(testDir):
    f = os.path.join(testDir, f)
    print("File: {}".format(f))
    print("{}Hash: {}".format("\t", generateSha256(f)))