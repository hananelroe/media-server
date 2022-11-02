from flask import Flask, render_template
import os
import extractFrame


staticFolder = './static'

# generate thumbnails if needed:
existingThumbnails = os.listdir(f'{staticFolder}/thumbnails')

for file in os.listdir(staticFolder):
    fileNameWithoutExtension = file.split('.')[0]
    if '.' in file:  # if it's a file with an extension
        if f"{fileNameWithoutExtension}_thumbnail.jpg" in existingThumbnails:
            continue  # skip if the thumbnail already exists
        else:
            imagePath = os.path.join(staticFolder, 'thumbnails', f"{fileNameWithoutExtension}_thumbnail.jpg")
            print(f"generating thumbnail for {file}...")
            extractFrame.getFrame(os.path.join('./static', file), imagePath)


app = Flask(__name__)


@app.route('/')
def main_gallery():
    filesList = [i for i in os.listdir(staticFolder) if '.' in i]  # filter files/folders without a dot in them
    #                                                                (a lazy way to filter the folders out)
    fileNamesWithoutExtesion = [i.split('.')[0] for i in filesList]  # coverts "image.jpg" to "image"
    return render_template('mainGallery.html', files=filesList, fileNames=fileNamesWithoutExtesion)


@app.route('/<file>')
def player(file):
    return render_template('vidPlayer.html', source=file)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
