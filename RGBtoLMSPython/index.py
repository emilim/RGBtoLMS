import cv2

def rgb2lms(r, g, b):
    l = (17.8824 * r) + (43.5161 * g) + (4.1194 * b)
    m = (3.4557 * r) + (27.1554 * g) + (3.8671 * b)
    s = (0.0300 * r) + (0.1843 * g) + (1.4671 * b)
    return (l, m, s)

def lms2rgb(l, m, s):
    r = (0.0809 * l) + (-0.1305 * m) + (0.1167 * s)
    g = (-0.0102 * l) + (0.0540 * m) + (-0.1136 * s)
    b = (-0.0004 * l) + (-0.0041 * m) + (0.6935 * s)
    return (r, g, b)

def fast(img):
    height, width, depth = img.shape
    img[0:height, 0:width, 0:depth] = img[0:height, 0:width, 0:depth] / 2
    return img 

vid = cv2.VideoCapture(2, cv2.CAP_DSHOW)
r, g, b = 255, 45, 10
l, m, s = rgb2lms(r, g, b)
r, g, b = lms2rgb(l, m, s)
print(r, g, b)
while(True):
    ret, frame = vid.read()
    fast(frame)
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
vid.release()
cv2.destroyAllWindows()