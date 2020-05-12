# BirdCLEF_2020

[Introduction here]

#### extractChunks.py
It takes all the data recordings and transforms them into several small pieces of 5 seconds. Where recordings longer than 5 seconds are split and recordings shorter than 5 seconds are increased until they complete 5 seconds.

#### allDataToJson.py
Melespectrograms and their harmonic and percussive components are created for each 5-second chunks created by __extrect.py__ , according to [Dreidger, Mueller and Disch, 2014](http://www.terasoft.com.tw/conf/ismir2014/proceedings/T110_127_Paper.pdf). And they are saved in a json file (like __train.json__ ) to be prepared for the models to be tested.
