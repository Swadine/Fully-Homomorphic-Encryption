## Calculate G_inverse (A)

## A= 24 x 552, n=24, m=552
## l is given

import numpy as np

# def twos_comp(val, l):
    # """compute the 2's complement of int value val"""
    # val is bounded between -q/2 to +q/2
    # z_bin=bin(val) # 1010 0110 = -90 and 90 = 0101 1010
    # if val<0:
    #     val = val + (2**(l-1))        # compute negative value
    # # print(val)
    # z = bin(val)[2:].zfill(l)
    # # z = list(z)
    # # print(z)
    # # z = int(z)
    # # print(z)
    # if z[0] == '0':
    #     z = '-1'+z[1:] 
    # else:
    #     z='0'+z[1:] 
    # return z

def twos_comp(val, l):
    if val<0:
        val = -val
        z = bin(val)[2:].zfill(l)
        # print(z)
        i = len(z)-1
        ret = np.ones(len(z))
        while i>=0 and z[i] == '0':
            ret[i] = 0
            i-=1
        i-=1
        while i>=0:
            if z[i] == '1':
                ret[i] = 0
            else:
                ret[i] = 1
            i-=1
        # print(ret)
        ret[0] = -1 if ret[0] == 1 else 0

        return ret[::-1]

    else:
        z = bin(val)[2:].zfill(l)
        ret = np.ones(len(z))
        for i in range(len(z)):
            ret[i] = 1 if z[i] == '1' else 0
        return ret[::-1]   


    # if val<0:
    #     val = -val
    #     z = bin(val)[2:].zfill(l)
    #     print(z)
    #     for i in range(len(z)-1, 0, -1):



    

    # ###############################
    # if (val & (1 << (l - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
    #     val = val - (1 << l)        # compute negative value
    # val=str(val)
    # val=list(val)
    # return val[-1] # 0101010 -1 -> ``


def calcg_inv(z,l):
    #calculate g^-1(z) where z is a nX1 vector
    n=z.shape[0]
    output_vec=np.zeros(n*l)
    for idx in range(n):
        # print(z[idx])
        output_vec[idx*l:(idx+1)*l]=twos_comp(z[idx],l)

    return output_vec

# print(calcg_inv(np.array([1, 2, -3]), 4))



