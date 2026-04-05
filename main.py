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
    
    block_size_h = 8
    block_size_w = 4
    h, w = bw_frame.shape

    num_row_blocks = h // block_size_h
    num_col_blocks = w // block_size_w
    
	# reshape into 3x3 blocks
    blocks = bw_frame.reshape(num_row_blocks, block_size_h, num_col_blocks, block_size_w)
    
	# take the average of each block and turn it into its own cell
    averages = blocks.mean(axis=(1, 3))
    
    for row in averages:
        for col in row:
          val = map_num_to_ascii(int(col))
          print(val, end="")
        print("")
            
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

cv2.destroyWindow("preview")
vc.release()