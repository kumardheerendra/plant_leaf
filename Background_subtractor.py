import numpy as np
import cv2

class Background_subtractor:
    def backgroundSubtractor(self,img):
        #background subtraction
        #cv2.namedWindow("image", cv2.WINDOW_NORMAL)
        #Load the Image

        mask = np.zeros(img.shape[:2],np.uint8)
        bgdModel = np.zeros((1,65),np.float64)
        fgdModel = np.zeros((1,65),np.float64)
        height,width=img.shape[:2]
        rect = (0,0,height+110,width+110)
        cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
        mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
        imgb = img*mask2[:,:,np.newaxis]
        #cv2.imshow("image",imgb)
        #plt.imshow(imgb)
        #plt.colorbar()
        #plt.show()
        return imgb
