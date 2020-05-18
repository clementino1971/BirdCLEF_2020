import os,random
import shutil

chunks_dir = '../data_chunks'
chunks_train_dir = 'train_chunks'

#os.mkdir(chunks_train_dir)
cont =0

species = [sp for sp in os.listdir(chunks_dir)]
for sp in species:
    dest_path = os.path.join(chunks_train_dir, sp)
    #os.mkdir(full_path)

    other_path = os.path.join(chunks_dir, sp)
    chunks = [rec for rec in os.listdir(other_path)]
    nc =  min(len(chunks),100)
    choices = random.sample(range(0, len(chunks)), nc) 

    for rec in choices:
        orig_path = os.path.join(other_path,str(rec)+".mp3")
        shutil.copy(orig_path, dest_path)

print(cont)

