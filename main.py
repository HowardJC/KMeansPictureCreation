import argparse
import cv2
from kmeans import Clustering
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Image Loader")
    parser.add_argument("-i", "--input", help="Your input image.")
    parser.add_argument("-k", "--number",type=int, help="k-number")

    args = parser.parse_args()
    Image=cv2.imread(args.input)
    AdjustedImage=Clustering.NewImageMaker(Image,args.number)
    cv2.imshow("New Image",AdjustedImage)
    cv2.waitKey(0)