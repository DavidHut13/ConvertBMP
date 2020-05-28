from cv2 import cv2
from datetime import datetime
import glob
import os

# Create file path to desktop
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

def getImages():
    """ Finds the image folder then stores their location in an array"""
    # looks for a rawImages folder on desktop
    bmp_folder = glob.glob("{}/raw/*.bmp".format(desktop))
    cv_imgs = []
    # looks in folder and adds all files in folder to the cv_img array
    for img in bmp_folder:
        n = cv2.imread(img)
        cv_imgs.append(n)
    # Goes through all images in array and sends them to get converted, then saves them
    for img in cv_imgs:
        print('Converting Image...')
        createConvertedFolder()
        saveImages(img)
           
def createConvertedFolder():
    """checks to see if a converted folder exists. If not, creates a converted folder to store the converted images"""
    # create file path: C:\Users\DHutt\Desktop\converted-imgs
    convertFolder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'converted')
    if not os.path.exists(convertFolder):
        os.makedirs(convertFolder)


def saveImages(img):
    """Converts bmps to jpg then saves them in a converted folder on desktop"""
    # get user path to desktop
    # captures time of image conversion in local machine time
    now = datetime.now().strftime('%H-%M-%S.%f')[:-3]
    # converts a bmp image to a jpg image and keeps 50 percent quality
    cv2.imwrite('{}/converted/converted-{}.jpg'.format(desktop,now),img,[cv2.IMWRITE_JPEG_QUALITY,50])
    return True
    
# if this file is the main file to run, then call getImages function
if __name__ == '__main__':
    getImages()




        




