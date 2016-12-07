from scipy import misc
import matplotlib.pyplot as pl
import numpy as np
import random

class Image:
    """
    One object of this class contains an image file, its path, and its resolution
    """
    def __init__(self, path, res):
        """
        Initialize image object with path and resize value, calls methods to open file and resize
        :param path: path to image
        :param res: resolution for resizing, square res x res
        """
        self.path = path
        self.res = res
        self.shuffled = []
        self.read()
        self.resize()

    def read(self):
        """
        Reads the image at self.path and writes it to variable self.image
        :return: nothing
        """
        self.image = misc.imread(self.path)

    def resize(self):
        """
        Resizes image to self.res x self.res
        :return: nothing
        """
        self.image = misc.imresize(self.image, (self.res, self.res))

    def shuffle(self, divider):
        """
        Separates picture in a number of tiles and shuffles them around
        :param divider: square root of number to tiles to separate into, i.e. divider = 3 -> 9 tiles
        :return: nothing
        """
        lst = [(self.res//divider) * x for x in range(0, divider+1)]
        img = [[] for i in range(0, divider)]
        rand_list = list(range(0, divider ** 2))
        random.shuffle(rand_list)
        imageArr = []
        count = 0

        for x in range(0, len(lst) - 1):
            for y in range(0, len(lst) - 1):
                imageArr.append(self.image[lst[x]:lst[x + 1], lst[y]:lst[y + 1]])

        for x in img:
            x = np.concatenate((imageArr[rand_list[count]], imageArr[rand_list[count + 1]]))
            count += 2
            for y in range(0, (divider - 2)):
                x = np.concatenate((x, imageArr[rand_list[count]]))
                count += 1
            img[(count // divider) - 1] = x

        for x in range(0, divider):
            if x == 1:
                self.shuffled = np.concatenate((img[x - 1], img[x]), axis=1)
            elif x > 1:
                self.shuffled = np.concatenate((self.shuffled, img[x]), axis=1)

    def display(self):
        """
        Displays shuffled picture
        :return:
        """
        pl.imshow(self.shuffled)
        pl.axis('off')
        pl.show()

    def savepic(self):
        misc.imsave("alex2.jpg", self.shuffled)

    def __str__(self):
        """
        String representing file name
        :return: a string representing file name
        """
        return "Photo is named {}".format(self.path)

if __name__ == "__main__":
    x = Image('alex.jpg', 1000)
    print(x)
    x.shuffle(10)
    x.savepic()
    x.display()
