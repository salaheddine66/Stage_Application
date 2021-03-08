import cv2
import numpy as np

def canny(image):
    gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
    kernel = 5
    blur = cv2.GaussianBlur(gray,(kernel, kernel),0)
    canny = cv2.Canny(gray, 50, 150)
    return canny


def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image,(x1,y1),(x2,y2),(0,255,0),8)
    return line_image


def region_of_interest(image):
    height = image.shape[0]

    polygons = np.array([[ (200, height), (401, 300), (650, height),]], np.int32)
    mask = np.zeros_like(image)

    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image



image = cv2.imread('pic.PNG')
lane_image = np.copy(image)
canny = canny(lane_image)
cropped_canny = region_of_interest(canny)
lines = cv2.HoughLinesP(cropped_canny, 2, np.pi/180, 100, np.array([]), minLineLength=40,maxLineGap=5)
line_image = display_lines(lane_image, lines)
combo_image = cv2.addWeighted(lane_image, 0.8, line_image, 1, 0)

cv2.imshow('result', combo_image)
cv2.waitKey(0)
