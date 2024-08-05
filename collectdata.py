import cv2
import os

directory = 'Data/'
print(os.getcwd())

# if not os.path.exists(directory):
#     os.mkdir(directory)
# if not os.path.exists(f'{directory}/blank'):
#     os.mkdir(f'{directory}/blank')

for i in range(5):
    letter = i
    if not os.path.exists(f'{directory}/{letter}'):
        os.mkdir(f'{directory}/{letter}')


cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    count = {
             '0': len(os.listdir(directory+"/0")),
             '1': len(os.listdir(directory+"/1")),
             '2': len(os.listdir(directory+"/2")),
             '3': len(os.listdir(directory+"/3")),
             '4': len(os.listdir(directory+"/4")),
    }

    row = frame.shape[1]
    col = frame.shape[0]
    cv2.rectangle(frame, (0, 40), (300, 300), (255, 255, 255), 2)
    cv2.imshow("data", frame)
    frame = frame[40:300, 0:300]
    cv2.imshow("ROI", frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame, (48, 48))
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == ord('0'):
        cv2.imwrite(directory + '0/' + str(count['0']) + '.png', frame)
    if interrupt & 0xFF == ord('1'):
        cv2.imwrite(directory + '1/' + str(count['1']) + '.png', frame)
    if interrupt & 0xFF == ord('2'):
        cv2.imwrite(directory + '2/' + str(count['2']) + '.png', frame)
    if interrupt & 0xFF == ord('3'):
        cv2.imwrite(directory + '3/' + str(count['3']) + '.png', frame)
    if interrupt & 0xFF == ord('4'):
        cv2.imwrite(directory + '4/' + str(count['4']) + '.png', frame)



