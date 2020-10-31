import cv2
import apriltag

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    detector = apriltag.Detector()
    directory = "data/Track 10-22/"
    file = directory+"30_3.png"
    img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    size = (int(img.shape[1]*0.5), int(img.shape[0]*0.5))
    output = cv2.resize(img, size)
    thresh = cv2.adaptiveThreshold(output, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    #test, thresh = cv2.threshold(output, 75, 255, cv2.ADAPTIVE_THRESH_MEAN_C)
    cv2.imwrite("output_1.png", thresh)
    detector.detect(thresh, return_image=True)
    cap.release()
    cv2.destroyAllWindows()