import hashlib
import sys
import random

# list of hashes
hash_dict_A = {}
hash_dict_B = {}

# base
g = 2
# modulus/prime number (2048 bites)
p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF

# public secret
A = sys.argv[1]
B = sys.argv[2]

A = int(A, 16)
B = int(B, 16)

final_key_a = 0
final_key_b = 0

bigger = 0

range_r = 100000000


def hash_save_a(key, value):
    num_1 = hex(value).lstrip("0x")

    # to string
    num_1 = str(num_1)

    # to bytes
    en_a = num_1.encode()

    # hash
    h_a = hashlib.sha3_224(en_a)

    hash_dict_A[hex(key).lstrip("0x")] = h_a.hexdigest()


def hash_save_b(key, value):
    num_1 = hex(value).lstrip("0x")

    # to string
    num_1 = str(num_1)

    # to bytes
    en_b = num_1.encode()

    # hash
    h_b = hashlib.sha3_224(en_b)

    hash_dict_B[hex(key).lstrip("0x")] = h_b.hexdigest()


def compare(last_e):
    temp_comp = 0
    comp = 0
    key_a = 0
    key_b = 0

    for i in range(len(hash_dict_A)):
        h_a = list(hash_dict_B.values())[(-1 - last_e)]

        h_b = list(hash_dict_A.values())[i]

        for i_2 in range(len(h_a)):
            if h_a[i_2] is h_b[i_2]:
                temp_comp += 1
                if temp_comp > comp:
                    comp = temp_comp
                    key_a = list(hash_dict_B.keys())[(-1 - last_e)]
                    key_b = list(hash_dict_A.keys())[i]
                else:
                    pass
            else:
                temp_comp = 0
                break
    return comp, key_a, key_b


for i in range(2500):
    sec_1 = random.randrange(1, range_r)
    sec_2 = random.randrange(1, range_r)

    K_1 = pow(B, sec_1, p)
    K_2 = pow(A, sec_2, p)

    hash_save_b(sec_1, K_1)
    hash_save_a(sec_2, K_2)

for i in range(len(hash_dict_B)):

    coll, c_key_a, c_key_b = compare(i)

    if coll > bigger:
        bigger = coll
        final_key_a = c_key_a
        final_key_b = c_key_b

    else:
        pass

print(final_key_b)
print(final_key_a)
