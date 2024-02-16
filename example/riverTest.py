from maskCanvas import canvas, point, showImage, line_seg
from buildingGenerator import angled_roof_integrated as integrated
from riverGenerator import river
from math import pi
import cv2

def main():
    c = canvas()

    r = river(pi/4, [[30,30],[300,30],[300,300],[30,300]])



    I = integrated(point(200,200), pi/4, pi/3, 7, 3, 3, scale=2)
    r = I.draw(r)

    c=I.draw(c)

    image = r.draw(10)
    image2 = c.draw(10)
    cv2.imwrite("./angled_roof.jpg", image)
    showImage(image)



if __name__ == "__main__":
    main()

