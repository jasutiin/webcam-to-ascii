import cv2


asci = [' ', '.', "'", ',', ':', ';', 'i', 'l', '!', 'I', '>', '<', '+', '=', 'n', 'u', 'z', 'Z', 'X', '@']

def map_num_to_ascii(val: int):
    num_of_ascii_chars = len(asci)
    a =  num_of_ascii_chars * val // 255
    return asci[a] if a != num_of_ascii_chars else asci[a-1]
 

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
    bw_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
else:
    rval = False

while rval:
    cv2.imshow("preview", bw_frame)
    rval, frame = vc.read()
    bw_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    for row in bw_frame:
        for col in row:
            char = map_num_to_ascii(int(col))
            print(f"{char}", end="")
        print("")
            
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

cv2.destroyWindow("preview")
vc.release()