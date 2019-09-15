import h5py
import os
import struct
import random

#converts file to tokens list
def main(key, file_name, num_programs):
    os.system(f'rm master.txt master_master_{key}.tok')
    f = h5py.File(file_name,'r')
    rand_list = random.sample(range(len(f['functionSource'])), num_programs)

    for i in rand_list:
        program = f['functionSource'][i]
        file = open('place_holder.c', 'w')
        file.write(program)
        file.close()
        cmd = 'tokenizer place_holder.c >> master.txt'
        os.system(cmd)
    
    with open('master.txt', 'r') as m:
        master_text = m.read()
        master_list = master_text.splitlines()
        master_master = open(f'master_master_{key}.tok', 'ab')
        for i, line in enumerate(master_list):
            int_tokens = line.split()
            int_tokens = list(map(int, int_tokens))

            for j in range(len(int_tokens), 500):
                int_tokens.append(0)
            int_tokens = int_tokens[:500]
            print(len(int_tokens))
            t_value = 0
            if f['CWE-119'][i]:
                t_value = 1
            int_tokens.insert(0, t_value)
            
            master_master.write(b''.join([struct.pack('h', i_token) for i_token in int_tokens]) + b'\n')
        master_master.close()


main('train', f'VDISC_train.hdf5', 1000)
main('test', f'VDISC_train.hdf5', 100)
main('validate', f'VDISC_train.hdf5', 100)

print('done')
