import cv2
import numpy as np

def color_quantization(image,k):
    data=np.float32(image).reshape((-1,3))
    criteria=(cv2.TERM_CRITERIA_EPS+cv2.TermCriteria_MAX_ITER,20,1.0)
    ret,label,center=cv2.kmeans(data,k,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
    center=np.uint8(center)
    result = center[label.flatten()]
    result=result.reshape(image.shape)
    return result