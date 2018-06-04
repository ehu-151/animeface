import cv2
import os

# 自作Haar-like特徴分類器の読み込み
ren_cascade = cv2.CascadeClassifier(r'cascade\ooo\cascade.xml')
# イメージファイルの読み込み
input_img_path = r'img/'
files = os.listdir(input_img_path)
for file in files:
    img = cv2.imread(input_img_path + file)

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = ren_cascade.detectMultiScale(gray)
    for (x, y, w, h) in faces:
        # 検知した顔を矩形で囲む
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 画像表示
    # cv2.imshow('img', img)
    cv2.imwrite(r'res_img/' + file, img)
