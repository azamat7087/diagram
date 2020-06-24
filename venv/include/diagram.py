from matplotlib import pyplot
import numpy as np

import cv2
import datetime
#create diagramm
country = ['China', 'Russia', 'USA', 'Kazakhstan']

#visitors =[20,18,13,12]
visitors = []


i = 0

while(i < len(country)):

    try:
        print("Input count of users from :", country[i])
        visitors.append(float(input()))
        i+=1
    except Exception:
        print("Your data is wrong!Error,try again")



if len(visitors) > 0:
    pyplot.barh(['C', 'U', 'R', 'K'],visitors)

    #save diagramm
    time_save = datetime.datetime.now()

    time_now = str(time_save.year)+"-"+str(time_save.month)+"-" + str(time_save.day)+"_"+ str(time_save.hour) + "." + str(time_save.minute) + "." + str(time_save.second)
    #time_now =  str(time_save.strftime("%d-%m-%Y %H:%M"))

    pyplot.savefig('/home/azamat/PycharmProjects/diagram/venv/rez/{}.png'.format("Pyplot"+ time_now))
    #function,which inserts image on image
    def imageOnImage(largeImg , smallImg,x_offset, y_offset ):
        y1, y2 = y_offset, y_offset + smallImg.shape[0]
        x1, x2 = x_offset, x_offset + smallImg.shape[1]

        alpha_s =1
        print(alpha_s)
        alpha_l = 0

        for c in range(0, 3):
            largeImg[y1:y2, x1:x2, c] = (alpha_s * smallImg[:, :, c] + alpha_l * largeImg[y1:y2, x1:x2, c])
    #create window size
    height = 500
    width = 800
    #create layer or void image
    layer = np.zeros((height,width,3))
    background = layer[:]
    cv2.imwrite('/home/azamat/PycharmProjects/diagram/venv/static/res.png', background)
    #call saved diagram
    background =cv2.imread('/home/azamat/PycharmProjects/diagram/venv/static/res.png')
    img =cv2.imread('/home/azamat/PycharmProjects/diagram/venv/rez/{}.png'.format("Pyplot"+ time_now))
    #change size diagram
    reImg = cv2.resize(img,(background.shape[1], background.shape[0]))
    #backroung on void image
    imageOnImage(background,reImg,0,0)
    s1 = cv2.resize(cv2.imread('/home/azamat/PycharmProjects/diagram/venv/static/kazakhstan-flag.jpg'), (100, 77))
    s2 = cv2.resize(cv2.imread('/home/azamat/PycharmProjects/diagram/venv/static/russia.png'), (100, 77))
    s3 = cv2.resize(cv2.imread('/home/azamat/PycharmProjects/diagram/venv/static/USA.png'), (100, 77))
    s4 = cv2.resize(cv2.imread('/home/azamat/PycharmProjects/diagram/venv/static/china.png'), (100, 77))

    #array = [s1,s2,s3,s4]

    imageOnImage(background,s1,0,75)
    imageOnImage(background,s2,0,165)
    imageOnImage(background,s3,0,260)
    imageOnImage(background,s4,0,355)
    cv2.imwrite('/home/azamat/PycharmProjects/diagram/venv/rez/{}.png'.format(time_now),background)
    cv2.imshow("final",background)
    cv2.waitKey(0)
    cv2.destroyAllWindows()