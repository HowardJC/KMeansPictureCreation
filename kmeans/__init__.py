from .clustering import *
class Clustering:
    @staticmethod
    def NewImageMaker(image,k):
        NewImage=color_quantization(image,k)
        return NewImage

