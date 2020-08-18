#Imports
from pydub import AudioSegment
import os,csv
import shutil
import math

#Paths to files with specie codes downloaded from https://www.aicrowd.com/challenges/lifeclef-2020-bird-monophone
path_codes = '../BirdCLEF2020_Train_Additional_Data/species_names_to_codes.txt'
path_audios = '../dataBase/audio/'


#mapping specienames and codes
mapa = {}

with open(path_codes) as sp_cod:
    csv_sp = csv.reader(sp_cod, delimiter=',')
    for sp in csv_sp:
        mapa[sp[0]] = sp[1]


def main():
    #Getting all species records directories
    species = [ sp for sp in os.listdir(path_audios)]
    
    #Creating dir to allocate the chunks of 5s
    try: 
        os.mkdir('../data_chunks')
    except:
        shutil.rmtree('../data_chunks')
        os.mkdir('../data_chunks')
        
    cont2 = 1 
    nfinal = 0

    #Importing functions used inside the loop bellow
    nspecies = len(species)
    os_path_join = os.path.join
    os_listdir = os.listdir
    AudioSegment_from_mp3 = AudioSegment.from_mp3

    #For each Specie
    for sp in species:
        print('{} from {}'.format(cont2,nspecies))

        cont3 = 0
        cont2 += 1
        cont = 0
        rec_name = mapa[sp]

        #Creating dir to allocate the chunks for each specie
        try:
            os.mkdir(os.path.join('../data_chunks',rec_name))
        except:
            continue

        #Getting all records from a Specie
        path_sp = os_path_join(path_audios,sp)
        records = [sp for sp in os_listdir(path_sp)]

        for rec in records:
            cont3 +=1

            #Reading the file of audio, some of them are corrupted
            try:
                record = AudioSegment_from_mp3(os_path_join(path_sp,rec))
            except:
                continue    
            
            #If the length of audio is >= then they are cutted in chuncks of 5s, otherwise
            #they are repeated until it reach 5s
            if(len(record) >= (5*1000)):
                
                ini,fim = 0,5

                while(fim <= len(record)/1000):
                    chunk = record[ini*1000:fim*1000]
                    ini += 5
                    fim += 5
                    path_c = "../data_chunks/{}/{}.mp3".format(rec_name,str(cont))
                    chunk.export(path_c, format="mp3")
                    cont+=1
                    nfinal += 1
            else:
                nrecord = record*10
                nrecord = nrecord[:5000]
                path_c = "../data_chunks/{}/{}.mp3".format(rec_name,str(cont))
                nrecord.export(path_c, format="mp3")
                cont+= 1
                nfinal += 1

        print('Read {} from {} - until now {}'.format(cont3,len(records),nfinal))
                              
    print(nfinal,"Records of Audio was created")           

main()    
