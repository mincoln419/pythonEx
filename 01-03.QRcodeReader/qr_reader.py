import cv2

def read_qrcode_cv2(opencv_image):
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(opencv_image);
    if data:
        print("QRCDE 데이터: {}".format(data))
        print("QRCDE 위치: {}".format(bbox))
        lefttop = (int(bbox[0][0][0]), int(bbox[0][0][1]))
        rightbottom = (int(bbox[0][2][0]), int(bbox[0][2][1]))
        cv2.rectangle(opencv_image, lefttop, rightbottom, (0, 0, 255), 5)
        cv2.imshow("aaaa", opencv_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else: print("파일이 없습니다")

filepath = "../01-02.QRcode/vcard.png"
cv_image1 = cv2.imread(filepath)
read_qrcode_cv2(cv_image1)