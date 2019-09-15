import h5py
import os
import struct
import random
import cvulnlexer

#converts file to tokens list
def main(key, file_name, num_programs):
    f = h5py.File(file_name,'r')
    rand_list = random.sample(range(len(f['functionSource'])), num_programs)
    #now we have tokenizer 
    os.system(f"rm master_master_{key}.tok")
    for ran in rand_list:
        label = f['CWE-119'][ran] or f['CWE-120'][ran] or f['CWE-469'][ran] or f['CWE-476'][ran] or f['CWE-other'][ran]
        cvulnlexer.TOKfile(label,f['functionSource'][ran],f'master_master_{key}.tok')
        

t_size = 1e5
main('train', f'VDISC_train.hdf5', int(t_size * .8))
main('test', f'VDISC_test.hdf5', int(t_size * .1))
main('validate', f'VDISC_validate.hdf5', int(t_size * .1))

print('done')
