import cv2
import numpy as np
from os import listdir
from ctypes import windll
from PIL import Image


def loadTemplates():
        img_path = './UI-Templates/'
        imgList = [["acceptQuestButton","claimRewardButton","collectAllButton","continueButton","mailboxMainButton","okButton","skipTutorialButton","dialogueSkip","inventoryConsumablesButton",
                    "dailyActivitiesIcon","inventoryIcon","inventoryNotificationIcon","menuNotificationIcon","questsNotificationIcon","questsIcon","shopIcon","arrowIndicatorIcon","autoQuestingMsg"],
                   [],[],[]]
        for img in listdir(img_path):
            imgList.append(img)
            for x in imgList:
                if x == "Buttons":
                    buttonsPath = x + '/'
                    for img in listdir(img_path+buttonsPath):
                        templateBgrData = cv2.imread(img_path+buttonsPath+img)
                        w, h = templateBgrData.shape[::-1]
                        templateGrayData = cv2.cvtColor(templateBgrData, cv2.COLOR_BGR2GRAY)
                        imgList[1].append(templateGrayData)
                        imgList[2].append(w)
                        imgList[3].append(h)
                if x == "Icons":
                    iconsPath = x + '/'
                    for img in listdir(img_path+iconsPath):
                        templateBgrData = cv2.imread(img_path+iconsPath+img)
                        w, h = templateBgrData.shape[::-1]
                        templateGrayData = cv2.cvtColor(templateBgrData, cv2.COLOR_BGR2GRAY)
                        imgList[1].append(templateGrayData)
                        imgList[2].append(w)
                        imgList[3].append(h)
        return imgList


def compareImages(img_bgr, template, width, height):

        img_bgr = cv2.imread(img_bgr)
        img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
        w = width
        h = height

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.90
        loc = np.where(res >= threshold)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        center = (int((top_left[0] + bottom_right[0]) / 2), int((top_left[1] + bottom_right[1]) / 2))
        print(top_left)
        print(bottom_right)
        print(center)

        for pt in zip(*loc[::-1]):
                cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (0, 255, 255), 1)
                cv2.circle(img_bgr, center, 5, (0, 255, 255), -1)

        imageInfo = [loc,center,top_left,bottom_right]
        return imageInfo

templates = loadTemplates()
for x in templates[0]:
    for t in templates[1]:
        if t == "inventoryIcon":
            for w in templates[2]:
                for h in templates[3]:
                    imageInfo = compareImages('Template-Matching-Tests/image-to-check-1.png',t,w,h)
            print(imageInfo)
#cv2.imshow('detected', img_bgr)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
