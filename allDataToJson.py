import numpy as np 
import matplotlib.pyplot as plt
import os,json,warnings
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import librosa, librosa.display
import cv2

warnings.filterwarnings('ignore')

#Path to dir with chunks of 5s, done by extractChunks
path = '../data_chunks/'

#Importing functions used inside the loop bellow
os_path_join = os.path.join
os_listdir = os.listdir



def melToGreyImage(mel):
    fig = plt.figure(figsize=(6, 1))

    librosa.display.specshow(mel, y_axis='mel', x_axis='time')
    plt.axis('off')
    plt.tight_layout(pad=0)

    # convert it to an OpenCV image/numpy array
    canvas = FigureCanvas(fig)
    canvas.draw()

    # convert canvas to image
    image = np.array(fig.canvas.get_renderer()._renderer)

    # it still is rgb, convert to opencv's default bgr
    image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

    #resize and return the image matrix on grayScale
    image = cv2.resize(image, (200, 40)) 
    plt.close()
    return image

def main():
    #Getting all species chunks directories
    species = [sp for sp in os_listdir(path)]
    nspecies = len(species)

    #Dictionary to allocate all data
    train = []

    cont = 1
    for sp in species:
        print("{} from {}".format(cont,nspecies))
        cont+=1

        #if(cont == 3):
        #   break

        #Getting all records from a Specie
        path_sp = os_path_join(path,sp)
        records = [sp for sp in os_listdir(path_sp)]

        for rec in records:
            audio_input = []

            path_chunk = os_path_join(path_sp,rec)

            #Loading chunk
            data, sr = librosa.load(path_chunk)

            #Checking if all chunks have 5s
            if(librosa.get_duration(y=data, sr=sr) < 5):
                print("It was not to enter here!!")
                continue

            #separating harmonic and percussive
            data_h, data_p = librosa.effects.hpss(data,margin=8)

            #Make the melspectrums
            mel_spec = librosa.feature.melspectrogram(data, sr=sr)
            mel_spec_h = librosa.feature.melspectrogram(data_h, sr=sr)
            mel_spec_p = librosa.feature.melspectrogram(data_p, sr=sr)
            db_mel_spec = librosa.power_to_db(mel_spec,ref=np.max)
            db_mel_spec_h = librosa.power_to_db(mel_spec_h,ref=np.max)
            db_mel_spec_p = librosa.power_to_db(mel_spec_p,ref=np.max)   

            #Transforming the melsSpectrums on GreyScale
            audio_input.append(melToGreyImage(db_mel_spec).tolist())
            audio_input.append(melToGreyImage(db_mel_spec_h).tolist())
            audio_input.append(melToGreyImage(db_mel_spec_p).tolist())

            train.append({ 'input' : audio_input, 'class' : sp})

    #Everyone to json
    with open('train.json', 'w') as jsonfile:
        json.dump(train, jsonfile)

main()        








