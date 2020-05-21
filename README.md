# BirdCLEF_2020

[Introduction here]

## Process Data

First of all we have the full train data downloaded from [LifeCLEF 2020 Bird](https://www.aicrowd.com/challenges/lifeclef-2020-bird-monophone). The data provides more than 70,000 recordings across 960 species. The data looks like:

    audio/
        |___specie1/
        |   ...   |___audio1.mp3
        |         |___audio2.mp3
        |          ...
        |   ...
        |___specie960/
   
So, we use __extractChunks.py__ to takes all the data recordings and transforms them into several small pieces of 5 seconds. Where recordings longer than 5 seconds are splited and recordings shorter than 5 seconds are increased(loop) until they complete 5 seconds. Then, we have more than 620.000 chunks across the 960 species arranged as follows:

    data_chunks/
              |___specie_code1/
              |       ...   |___0.mp3
              |             |___1.mp3
              |             ...
              |             |___30.mp3
              |      ...
              |___specie_code960/


For processing reasons we don't use all the chunks of audios. So, we select the data will use on train models.On  __selectChunks.py__ we take randomly 100(or less) examples of chunks for each specie. As output we have:

    train_chunks/
                  |___specie_code1/
                  |       ...   |___23.mp3
                  |             |___129.mp3
                  |             ...
                  |             |___651.mp3
                  |      ...
                  |___specie_code960/

And finally we process all the exemples of audio on train_chunks. For each chunk is generated a Melespectrograms and their harmonic and percussive components, according to [Dreidger, Mueller and Disch, 2014](http://www.terasoft.com.tw/conf/ismir2014/proceedings/T110_127_Paper.pdf). And they are saved as a compressed numpy array (.npz). Each numpy array has the shape 40x200x3 As output of __processDataTrain.py__ we have: 

     train/
          |___1.npz
          |___2.npz   
          |   ...
          |___93410.npz
    filenames.npy
    labels.npy
    
Where filenames.py and labels.py are used to pair filenames and labels, and it is used to generate the train batches once all the 93410 arrays don't fit on memory.    

## Models
