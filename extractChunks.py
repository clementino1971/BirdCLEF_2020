from pydub import AudioSegment
import os,csv
import shutil
import math

mapa = {}
mapa_dur = {}
with open('../BirdCLEF2020_Train_Additional_Data/species_names_to_codes.txt') as sp_cod:
    csv_sp = csv.reader(sp_cod, delimiter=',')
    for sp in csv_sp:
        mapa[sp[0]] = sp[1]


with open('../audio_dur.csv') as audio_dur:
    csv_dur = csv.reader(audio_dur, delimiter=',')
    for au in csv_dur:
        mapa_dur[au[0]] = au[1]        

def main():
    path = '../dataBase/audio/'
    species = [ sp for sp in os.listdir(path)]

   
    #try: 
    #    os.mkdir('../data_chunks')
    #except:
    #    shutil.rmtree('../data_chunks')
    #    os.mkdir('../data_chunks')
        
    cont2 = 1 
    nfinal = 0

    nspecies = len(species)
    os_path_join = os.path.join
    os_listdir = os.listdir
    AudioSegment_from_mp3 = AudioSegment.from_mp3
    math_ceil = math.ceil


    for sp in species:
        print('{} from {}'.format(cont2,nspecies))
        cont3 = 0
        cont2 += 1
        cont = 0
        rec_name = mapa[sp]
        #try:
        #    os.mkdir(os.path.join('../data_chunks',rec_name))
        #except:
        #    continue    
        path_sp = os_path_join(path,sp)
        records = [sp for sp in os_listdir(path_sp)]
        for rec in records:
            #try:
                cont3 +=1
                
                if (rec in mapa_dur.keys() and int(mapa_dur[rec]) >= 6):
                    cont+=1
                
                else:
                    try:
                        record = AudioSegment_from_mp3(os_path_join(path_sp,rec))
                    except:
                        continue    

                    if(len(record) >= (5*1000)):
                        cont+=1

                        
                        #ini,fim = 0,5

                        #while(fim <= len(record)/1000):
                        #    chunk = record[ini*1000:fim*1000]
                        #    ini += 5
                        #    fim += 5
                        #    path_c = "../data_chunks/{}/{}.mp3".format(rec_name,str(cont))
                        #    chunk.export(path_c, format="mp3")
                        #    nfinal += 1

                    else:
                        #c = int(math_ceil((5000 - len(record))/len(record)))
                        nrecord = record*10
                        nrecord = nrecord[:5000]
                        path_c = "../data_chunks/{}/{}.mp3".format(rec_name,str(cont))
                        nrecord.export(path_c, format="mp3")
                        cont+= 1
                        nfinal += 1
            #except:
            #    print("Bad")
        print('Read {} from {} - untli now {}'.format(cont3,len(records),nfinal))
                
                
    print("Foram criados ",nfinal," Gravações de audio")           

main()    
