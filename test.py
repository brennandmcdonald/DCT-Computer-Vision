import cv2
import apriltag

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    detector = apriltag.Detector()
    directory = "data/Track 10-22/"
    file = directory+"30_3.png"
    img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    size = (int(img.shape[0]*0.3), int(img.shape[1]*0.3))
    output = cv2.resize(img, size)
    test, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    detector.detect(thresh, return_image=True)
    cv2.imwrite("output_1.jpg", thresh)
    cap.release()
    cv2.destroyAllWindows()