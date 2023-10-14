import pyzbar.pyzbar as pyzbar

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

def read_qrcode_zbar(opencv_image):
    gray = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)
    decoded = pyzbar.decode(gray)
    for d in decoded:
        x, y, w, h = d.rect
        qrcode_data = d.data.decode('utf-8')
        qrcode_type = d.type
        cv2.rectangle(opencv_image, (x,y), (x + w, y + h), (0, 0, 255), 3)
        text = "{} {}".format(qrcode_data, qrcode_type)
        cv2.putText(opencv_image, text, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 1, cv2.LINE_AA)

        cv2.imshow("aaaa", opencv_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


filepath = "../01-02.QRcode/vcard.png"
cv_image1 = cv2.imread(filepath)
read_qrcode_zbar(cv_image1)