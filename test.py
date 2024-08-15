import numpy as np
from util import *
from keygen import keygen
from enc import encrypt
from dec import decrypt
from g_inv import calcg_inv

keys = keygen(24)
 
for a,b in [(1,1), (17,19), (34,62)]:
    ca = encrypt(keys, a)
    cb = encrypt(keys, b)
    a_b = a + b
    ca_cb = (ca + cb) % keys.q
    d_ca_cb = decrypt(keys, ca_cb)
    print(" "*12 + "Expected %d" % a_b)
    print(" "*12 + "Received %d" % d_ca_cb)
    if a_b == d_ca_cb:
        print(" "*12 + "\x1B[32;1mPassed\x1B[0m")
    else:
        print(" "*12 + "\x1B[31;1mFailed\x1B[0m")


ca = encrypt(keys, a)
cb = encrypt(keys, b)

a_b = a + a + a + b + b + b
ca_cb = (ca + ca + ca + cb + cb + cb) % keys.q
d_ca_cb = decrypt(keys, ca_cb)
print(" "*12 + "Expected %d" % a_b)
print(" "*12 + "Received %d" % d_ca_cb)
if a_b == d_ca_cb:
    print(" "*12 + "\x1B[32;1mPassed\x1B[0m")
else:
    print(" "*12 + "\x1B[31;1mFailed\x1B[0m")

# print("l", keys.l)

print('For multiplication: ')
for a,b in [(1,1),(7,3), (11,12), (4,6)]:
    ca = np.array(encrypt(keys, a))
    cb = np.array(encrypt(keys, b))
    # print(ca)
    # print(cb)
    a_b = a * b
    # print(cb.shape)
    g_inv = []
    for i in range(cb.shape[1]):
        x = calcg_inv(cb[:,i], keys.l)
        # print(x)
        g_inv.append(x)
    print()
    g_inv = np.array(g_inv).T
    # G = buildGadget(keys.l, keys.n)
    # y = np.matmul(G, g_inv)
    # print((y == cb).all()) # g_inv is correct
    # print(g_inv.shape)
    # print(G)
    ca_cb = np.dot(ca, g_inv) % keys.q # ab G # ca -> 20, 380 and g_inv -> 380, 380
    # r_sum=ca_cb.sum(axis=1)
    # ca_cb=ca_cb/r_sum[:,np.newaxis]
    # print(ca_cb.shape)
    # d_ca_cb = ca_cb[0,0] / 1
    # print(ca_cb)
    d_ca_cb = decrypt(keys, ca_cb)
    
    print(" "*12 + "Expected %d" % a_b)
    print(" "*12 + "Received %d" % d_ca_cb)
    if a_b == d_ca_cb:
        print(" "*12 + "\x1B[32;1mPassed\x1B[0m")
    else:
        print(" "*12 + "\x1B[31;1mFailed\x1B[0m")

