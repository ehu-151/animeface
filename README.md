# 概要
2次元画像の顔検出と顔識別(キャラ識別)ができます。
https://qiita.com/ehu/items/12457d77705a52d63fd5
# 顔検出の使い方
2次元画像の顔検出には、[nagadomiさんのlbpcascade_animeface](https://github.com/nagadomi/lbpcascade_animeface)を使います。lbpcascade_animeface.xml(カスケード分類器)をcv2に読み込まさせてください。
```python
# 分類器の読み込み
anime_cascade = cv2.CascadeClassifier(r'lbpcascade_animeface.xml')
# イメージファイルをフォルダーごと読み込み
input_img_path = r'img/'
files = os.listdir(input_img_path)
for file in files:
    img = cv2.imread(input_img_path + file)

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = anime_cascade.detectMultiScale(gray)
    for (x, y, w, h) in faces:
        # 検知した顔を矩形で囲む
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # 画像表示と保存
    # cv2.imshow('img', img)
    cv2.imwrite(r'res_img/' + file, img)
```

# 顔識別の使い方
カスケード分類器を作成します。まず以下のディレクトリ構造を用意してください。
```commandline
/
    cascade/
        ooo/    (作成したカスケード分類器を格納するディレクトリ)
        opencv_createsamples.exe
        opencv_traincascade.exe
    pos/    (正解画像)
        *.jpg
        *.jpeg
        .
        .
    vec/
    
    neg/    (非正解画像)
        *.jpg
        *.jpeg
        .
        .
```

1. コマンドラインで正解画像からベクター画像を作成します。(例)
- 一つのみの正解画像から作成する場合
```commandline
$ cd cascade
$ opencv_createsamples -data ..pos/*.jpg -vec ../vec/output.vec -num 30 -w 40 -h 40 -bgcolor 255 -maxidev 40 -maxxangle 0.8 -maxyangle 0.8 -maxzangle 0.5 -show
```
- 複数の正解画像から作成する場合
```commandline
$ cd cascade
$ opencv_createsamples -info ../positives.txt -vec ../vec/output.vec -num 30 -w 40 -h 40 -bgcolor 255 -maxidev 40 -maxxangle 0.8 -maxyangle 0.8 -maxzangle 0.5 -show
```
[positives.txtの記法](https://docs.opencv.org/3.0-last-rst/doc/user_guide/ug_traincascade.html)

2. nglist.txtの作成

Windowsの場合、
```commandline
dir *.jpg /b > nglist.txt
```

3. 学習(例)
```commandline
opencv_traincascade.exe -data ./ooo/ -vec ../vec/output.vec -bg ../neg/nglist.txt -numPos 30 -numNeg 60 -w 40 -h 40
```

4. 実行
```python
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

    # 画像表示と保存
    # cv2.imshow('img', img)
    cv2.imwrite(r'res_img/' + file, img)
```