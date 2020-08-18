#imports
import os,random
import shutil

#Dir with data_chunks splitted by extractChunks.py
chunks_dir = '../data_chunks'
#Dir that will be host the data train
chunks_train_dir = 'train_chunks'

#Create dir
os.mkdir(chunks_train_dir)

species = [sp for sp in os.listdir(chunks_dir)]
for sp in species:
    #Create a subdir for each specie
    dest_path = os.path.join(chunks_train_dir, sp)
    os.mkdir(dest_path)
    
    #Getting records from chunks_dir
    other_path = os.path.join(chunks_dir, sp)
    chunks = [rec for rec in os.listdir(other_path)]

    nc =  min(len(chunks),100)

    #Getting nc random samples from each specie
    choices = random.sample(range(0, len(chunks)), nc) 

    for rec in choices:
        orig_path = os.path.join(other_path,str(rec)+".mp3")
        shutil.copy(orig_path, dest_path)

