import cv2


def getFrame(vidPath, frameToCapture, savePath):
    vid = cv2.VideoCapture(vidPath)
    currentframe = 0
    while True:
        ret, frame = vid.read()
        if ret:
            if currentframe == frameToCapture:  # only save the required frame
                cv2.imwrite(savePath, frame)
                break
            currentframe += 1
        else:
            break


if __name__ == "__main__":
    getFrame('./movie.mp4', 5000)