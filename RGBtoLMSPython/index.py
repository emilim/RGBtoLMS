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

def framergb2lms(frame):
    frame[:,:,0], frame[:,:,1], frame[:,:,2] = rgb2lms(frame[:,:,0], frame[:,:,1], frame[:,:,2])
    return frame

def framelms2rgb(frame):
    frame[:,:,0], frame[:,:,1], frame[:,:,2] = lms2rgb(frame[:,:,0], frame[:,:,1], frame[:,:,2])
    return frame

def fast(img):
    height, width, depth = img.shape
    img[0:height, 0:width, 0:depth] = framelms2rgb(framergb2lms(img[0:height, 0:width, 0:depth]))
    return img 

vid = cv2.VideoCapture(2, cv2.CAP_DSHOW)

while(True):
    ret, frame = vid.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    fast(frame)
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
vid.release()
cv2.destroyAllWindows()