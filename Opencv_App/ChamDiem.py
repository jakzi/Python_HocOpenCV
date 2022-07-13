import cv2
import numpy as np
import utlis
###########
path="1.jpg"
widthImg=700
heightImg=700
questions=20
choices=4
ans=[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
ans1=[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
ans2=[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
#########
print("So cau hoi can kiem tra:")
q=int(input())
for i in range(0,q):
    int(i)
    print("Ket qua cau thu "+str(i+1))
    a=input()
    if a.lower()=="a":
        b=0
    if a.lower() == "b":
        b=1
    if a.lower()=="c":
        b=2
    if a.lower() == "d":
        b=3
    if i<20:
        ans[i]=b
    if i>=20 and i<40:
        ans1[i-20]=b
    if i>=40:
        ans2[i-40]=b
while True:
    print("Duong dan")
    path=input()
    img = cv2.imread(path)

    #
    img = cv2.resize(img, (widthImg, heightImg))
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 10, 50)
    imgBlank = np.zeros_like(img)
    imgFinal=img.copy()
    try:
        # tim cac doi tuong
        imgContours = img.copy()
        imgBigContour = img.copy()
        contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 10)
        rectCon = utlis.rectContour(contours)
        firPoints = utlis.getCornerPoints(rectCon[0])
        secPoints = utlis.getCornerPoints(rectCon[1])
        thiPoints = utlis.getCornerPoints(rectCon[2])
        mdPoints = utlis.getCornerPoints(rectCon[3])


        def cham(imag, dapan, pt1, pt2, img=imgFinal):
            imgWarpGray = cv2.cvtColor(imag, cv2.COLOR_BGR2GRAY)
            imgThresh = cv2.threshold(imgWarpGray, 180, 255, cv2.THRESH_BINARY_INV)[1]
            #chia nho anh de lay cac lua chon A,B,C,D
            boxes = utlis.splitBoxes(imgThresh)
            countR = 0
            countC = 0
            myPixelVal = np.zeros((questions, choices))
            for image in boxes:
                totalPixels = cv2.countNonZero(image)
                myPixelVal[countR][countC] = totalPixels
                countC += 1
                if (countC == choices): countC = 0;countR += 1
            # tim cau tra loi cua thi sinh
            myIndex = []
            for x in range(0, questions):
                arr = myPixelVal[x]
                dem=0
                myIndexVal = np.where(arr == np.amax(arr))
                if np.amax(arr) > 800:
                    myIndex.append(myIndexVal[0][0])
                else:
                    myIndex.append(5)

            # tim cau tra loi dung
            grading = []
            for x in range(0, questions):
                if dapan[x] == myIndex[x]:
                    grading.append(1)
                else:
                    grading.append(0)
            dem = sum(grading)
            #ve
            utlis.showAnswers(imag, myIndex, grading, dapan)
            utlis.drawGrid(imag)
            return dem


        # tim khung trac nghiem va ma de
        if firPoints.size != 0 and secPoints.size != 0 and thiPoints.size != 0 and mdPoints.size != 0:
            # 1-20
            cv2.drawContours(imgBigContour, firPoints, -1, (0, 0, 255), 20)  # mau do
            firPoints = utlis.reorder(firPoints)
            ptsx1 = np.float32(firPoints)
            ptsx2 = np.float32([[0, 0], [300, 0], [0, 700], [300, 700]])
            matrixG = cv2.getPerspectiveTransform(ptsx1, ptsx2)
            img1 = cv2.warpPerspective(img, matrixG, (300, 700))
            # 21-40
            cv2.drawContours(imgBigContour, secPoints, -1, (255, 0, 0), 20)  # mau xanh
            secPoints = utlis.reorder(secPoints)
            ptsy1 = np.float32(secPoints)
            ptsy2 = np.float32([[0, 0], [300, 0], [0, 700], [300, 700]])
            matrixG = cv2.getPerspectiveTransform(ptsy1, ptsy2)
            img2 = cv2.warpPerspective(img, matrixG, (300, 700))
            # 41-60
            cv2.drawContours(imgBigContour, thiPoints, -1, (0, 255, 0), 20)  # mau xanh la
            thiPoints = utlis.reorder(thiPoints)
            ptsz1 = np.float32(thiPoints)
            ptsz2 = np.float32([[0, 0], [300, 0], [0, 700], [300, 700]])
            matrixX = cv2.getPerspectiveTransform(ptsz1, ptsz2)
            img3 = cv2.warpPerspective(img, matrixX, (300, 700))
            # ma de
            cv2.drawContours(imgBigContour, mdPoints, -1, (0, 0, 0), 20)  # mau den
            mdPoints = utlis.reorder(mdPoints)
            pts1 = np.float32(mdPoints)
            pts2 = np.float32([[0, 0], [325, 0], [0, 150], [325, 150]])
            matrixZ = cv2.getPerspectiveTransform(pts1, pts2)
            img4 = cv2.warpPerspective(img, matrixZ, (325, 150))
            ###########################
            dem1 = cham(img3, ans, ptsz1, ptsz2)
            dem2 = cham(img2, ans1, ptsy1, ptsy2)
            dem3 = cham(img1, ans2, ptsx1,ptsx2)
            print("So cau dung:" + str(dem1 + dem2 + dem3))
            diem = (dem1 + dem2 + dem3) * (10 / q)
            print("Diem:", diem)
            imageArray = ([img3,img2,img1])
    except:
        imageArray = ([img, imgGray, imgCanny, imgContours])
    imageStacked = utlis.stackImages(imageArray, 0.5)
    cv2.imshow("Bailam", imageStacked)
    cv2.waitKey(0)
