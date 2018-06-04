import cv2
import sys
import os.path


def detect(filename, cascade_file=r"./lbpcascade_animeface.xml", name="output.jpg"):
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)

    cascade = cv2.CascadeClassifier(cascade_file)
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    faces = cascade.detectMultiScale(gray,
                                     # detector options
                                     scaleFactor=1.1,
                                     minNeighbors=5,
                                     minSize=(24, 24))
    if len(faces)==0 : return
    for (x, y, w, h) in faces:
        # 顔だけトリミング
        image = image[y:y + h, x:x + w]
    # 画像表示
    # cv2.imshow("AnimeFaceDetect", image)
    cv2.waitKey(0)
    cv2.imwrite(r'neg/' + name, image)


if __name__ == '__main__':
    path = r'whole_image_orignal/'
    # detect(r'C:\\Users/kaikoro/PycharmProjects/animeface/whole_image_orignal/1.jpg')
    files = os.listdir(path)
    for file in files:
        p=path+file
        detect(p,name=file)
