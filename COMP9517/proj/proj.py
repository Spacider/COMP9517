import pandas as pd
import cv2



def get_ground_truth(filepath):
    df = pd.read_json(filepath)
    return df

def get_hog_feature(img):
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    (rects, weights) = hog.detectMultiScale(img, winStride=(4,4), padding=(8,8), scale=1.25, useMeanshiftGrouping=False)

    for (x, y, w, h) in rects:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('hog-prople', img)


if __name__ == '__main__':
    # 获取 gt
    # ground_truth_path = './data/truth/annotation.json'
    # gt = get_ground_truth(ground_truth_path)
    # list = gt[gt['file_name'] == 'supp_img/0001.jpg']['bbox'].tolist()[0]
    # for car in list:
    #     print(car)
    img = cv2.imread('./data/images/0001.jpg')
    get_HOG(img)