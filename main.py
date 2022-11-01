from flask import Flask, render_template
import os
import extractFrame


staticFolder = './static'

# organise the video files in the static folder:
# put each file in a directory that's named the same as the file:
for file in os.listdir(staticFolder):
    if '.' in file:  # if it's a file with extension
        os.mkdir(os.path.join(staticFolder, file.split('.')[0]))
        # using a linux commands here, because that's what I'm familiar with. you can change it though.(obviously)
        os.system(f"mv \'{os.path.join(staticFolder, file)}\' \'{os.path.join(staticFolder, file.split('.')[0])}/\'")

# extract frame from the beginning of each video file for thumbnail:
for directory in os.listdir(staticFolder):
    if "thumbnail.jpg" not in os.listdir(os.path.join(staticFolder, directory)):  # if the thumbnail file is missing:
        #                                               (we can know for sure that "directory" is a directory and not a
        #                                               file because we moved all the files to directories earlier)
        # extract a frame and save it as "thumbnail.jpg":
        currentDir = os.path.join(staticFolder, directory)
        print(f"generating a thumbnail for {currentDir}...")
        extractFrame.getFrame(vidPath=os.path.join(currentDir, os.listdir(currentDir)[0]),
                              frameToCapture=30*60*3,
                              savePath=os.path.join(currentDir, 'thumbnail.jpg'))


app = Flask(__name__)


@app.route('/')
def main_gallery():
    filesList = os.listdir(staticFolder)
    filesList = sorted(filesList, key=lambda s: sum(map(ord, s)), reverse=True)  # sort by ascii value
    return render_template('mainGallery.html', files=filesList)


@app.route('/<file>')
def player(file):
    return render_template('vidPlayer.html', source=file)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
