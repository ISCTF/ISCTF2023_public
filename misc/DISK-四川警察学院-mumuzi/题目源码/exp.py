import base64
import os
from libnum import s2n
import time

flag = 'ISCTF{U_r_G00d_NTFS_Manager}'
fake = 'ISCTF{This_is_Not_True_flag}'
flag_list = [flag[i:i+4] for i in range(0, len(flag), 4)]
fake_list = [fake[i:i+4] for i in range(0, len(fake), 4)]
base_list = [base64.b64encode(group.encode()).decode() for group in fake_list]
libnum_list = [s2n(group) for group in flag_list]
for i in range(len(libnum_list)):
    f = open(f'M:\{libnum_list[i]}.txt','w').write('flag not here!!!')
    time.sleep(0.5)
    os.rename(f'M:\{libnum_list[i]}.txt',f'M:\{base_list[i][::-1]}.txt')

