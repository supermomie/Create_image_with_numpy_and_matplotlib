import numpy as np
import matplotlib.pyplot as plt

NAME = "drapeau"
H = 2000
W = 2000

BLUE   = [0, 0, 255]
GREEN  = [0, 255, 0]
RED    = [255, 0, 0]
YELLOW = [255, 255, 0]
WHITE = [255, 255, 255]



def change_values(newImage, h):
    for i in range(int(h)//2):
        newImage[0+i,1+i: -i-1: ] = 3 #CHANGE TOP SIDE VALUES
        newImage[i,0 : i : 1] = 4     #CHANGE TOPLEFT SIDE VALUES
        newImage[-i-1,0 : i : 1] = 4  #CHANGE BOTTOMLEFT SIDE VALUES
        newImage[-i,i: -i: ] = 5      #CHANGE BOTTOM SIDE VALUES


def create_img(name, h, w):
    image = np.zeros((h, w, 3))
    diag = np.eye(w, h, dtype=int)
    newImage = diag + np.flipud(diag)

    change_values(newImage, h)
    image[np.where(newImage == 0)] = RED
    image[np.where(newImage == 1)] = WHITE
    image[np.where(newImage == 3)] = BLUE
    image[np.where(newImage == 4)] = YELLOW
    image[np.where(newImage == 5)] = GREEN
    #print(newImage)
    plt.title(name)
    plt.imshow(image)
    plt.savefig(name)
    plt.show()


if __name__ == "__main__":
    create_img(NAME, H, W)
