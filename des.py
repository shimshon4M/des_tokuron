#!/usr/bin/env/python
#coding:utf-8

import sys
import os

def bin2str(source):
    ret=""
    for i in range(0,len(source),8):
        ret+=chr(int(source[i:i+8],2))
    return ret

def char2bin(source):
    h=ord(source)
    ret=""
    for i in range(7,-1,-1):
        if h>=pow(2,i):
            ret+=str(h//pow(2,i))
            h-=pow(2,i)
        else:
            ret+="0"
    return ret

def str2bin(source):
    return "".join([char2bin(c) for c in source])

def int2bin(source,bitNum):
    ret=""
    for i in range(bitNum-1,-1,-1):
        if source-pow(2,i)>=0:
            ret+="1"
            source-=pow(2,i)
        else:
            ret+="0"
    return ret

def nLeftShift(target,n):
    tmp=target[:n]
    return target[n:]+tmp
        
def permutate(source,table):
    """
    permutate the bits of the input block following the permutation table
    """
    return "".join([source[table[i]-1] for i in range(len(table))])

def IP(source):
    table=[58,50,42,34,26,18,10,2,
           60,52,44,36,28,20,12,4,
           62,54,46,38,30,22,14,6,
           64,56,48,40,32,24,16,8,
           57,49,41,33,25,17,9,1,
           59,51,43,35,27,19,11,3,
           61,53,45,37,29,21,13,5,
           63,55,47,39,31,23,15,7]
    return permutate(source,table)

def FP(source):
    table=[40,8,48,16,56,24,64,32,
           39,7,47,15,55,23,63,31,
           38,6,46,14,54,22,62,30,
           37,5,45,13,53,21,61,29,
           36,4,44,12,52,20,60,28,
           35,3,43,11,51,19,59,27,
           34,2,42,10,50,18,58,26,
           33,1,41,9,49,17,57,25]
    return permutate(source,table)

def E(source):
    table=[32,1,2,3,4,5,
           4,5,6,7,8,9,
           8,9,10,11,12,13,
           12,13,14,15,16,17,
           16,17,18,19,20,21,
           20,21,22,23,24,25,
           24,25,26,27,28,29,
           28,29,30,31,32,1]
    return permutate(source,table)

def P(source):
    table=[16,7,20,21,
           29,12,28,17,
           1,15,23,26,
           5,18,31,10,
           2,8,24,14,
           32,27,3,9,
           19,13,30,6,
           22,11,4,25]
    return permutate(source,table)

def SBOX(source):
    substituted=[]
    table=[[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7,
            0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8,
            4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0,
            15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13],
           [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10,
            3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5,
            0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15,
            13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9],
           [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8,
            13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1,
            13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7,
            1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12],
           [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15,
            13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9,
            10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4,
            3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14],
           [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9,
            14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6,
            4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14,
            11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3],
           [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11,
            10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8,
            9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6,
            4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13],
           [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1,
            13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6,
            1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2,
            6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12],
           [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7,
            1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2,
            7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8,
            2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]
    s_pos=0
    for i in range(0,len(source),6):
        start=source[i]
        end=source[i+5]
        row=int(start+end,2)
        col=int(source[i+1:i+5],2)
        substituted.append(int2bin(table[s_pos][16*row+col],4))
        s_pos+=1
    return "".join(substituted)
        
def PC1(source):
    table=[57,49,41,33,25,17,9,
           1,58,50,42,34,26,18,
           10,2,59,51,43,35,27,
           19,11,3,60,52,44,36,
           63,55,47,39,31,23,15,
           7,62,54,46,38,30,22,
           14,6,61,53,45,37,29,
           21,13,5,28,20,12,4]
    return permutate(source,table)

def PC2(source):
    table=[14,17,11,24,1,5,
           3,28,15,6,21,10,
           23,19,12,4,26,8,
           16,7,27,20,13,2,
           41,52,31,37,47,55,
           30,40,51,45,33,48,
           44,49,39,56,34,53,
           46,42,50,36,29,32]
    return permutate(source,table)

def XOR(t1,t2):
    ret=""
    for i in range(len(t1)):
        if t1[i]==t2[i]:
            ret+="0"
        else:
            ret+="1"
    return ret

def divide2blocks(source):
    """
    divide the data into blocks (64bit per 1block)
    """
    blocks=[]
    fillNum=0
    if len(source)%64>0:
        fillNum=64-len(source)%64
    for i in range(fillNum): # fill "0" to convert length of text to multiples of 64
        source+="0"
    for i in range(0,len(source),64):
        blocks.append(source[i:i+64])
    return blocks

def remove0(source):
    ret=""
    for i in range(0,len(source),8):
        if source[i:i+8]!="00000000":
            ret+=source[i:i+8]
    return "".join(ret)
        
def generateKeys(key):
    """
    generate 16 subkeys.
    return a list of keys.
    """
    keys=[]
    pc1=PC1(key)                     # Permuted choice 1 (PC1)
    c=pc1[:28]                       # (the first half)
    d=pc1[28:]                       # (the second half)
    for i in range(16):              # (for 16 rounds)
        if i+1 in [1,2,9,16]:        # (amounts of shift)
            n=1
        else:
            n=2
        c=nLeftShift(c,n)            # (left shift the first half)
        d=nLeftShift(d,n)            # (left shift the second half)
        keys.append(PC2(c+d))        # Permuted choice 2 (PC2)
    return keys

def encrypt(text,subKeys):
    encryptedBlocks=[]
    for block in divide2blocks(text):
        ip=IP(block)                 # Initial permutation (IP)
        l=ip[:32]                    # (the first half)
        r=ip[32:]                    # (the second half)
        for i in range(16):          # (for 16 rounds)
            e=E(r)                   # Expansion function (E)
            xor=XOR(e,subKeys[i])    # xor
            sbox=SBOX(xor)           # Substitute boxes (S-BOX)
            p=P(sbox)                # Permutation (P)
            xor=XOR(p,l)             # xor
            if i<15:                 # (swap the left and right)
                l=r
                r=xor 
        fp=FP(xor+r)                 # Final permutation (IP-1)
        encryptedBlocks.append(fp)
    return "".join(encryptedBlocks)
        
def decrypt(text,subKeys):
    decryptedBlocks=[]
    for block in divide2blocks(text):
        ip=IP(block)                 # Initial permutation (IP)
        l=ip[:32]                    # (the first half)
        r=ip[32:]                    # (the second half)
        for i in range(16):          # (for 16 rounds)
            e=E(r)                   # Expansion function (E)
            xor=XOR(e,subKeys[-i-1]) # xor
            sbox=SBOX(xor)           # Substitute box (S-BOX)
            p=P(sbox)                # Permutation (P)
            xor=XOR(p,l)             # xor
            if i<15:                 # (swap the left and right)
                l=r
                r=xor
        fp=FP(xor+r)                 # Final permutation (IP-1)
        decryptedBlocks.append(fp)
    return bin2str(remove0("".join(decryptedBlocks)))
    

def readFile(filename):
    if os.path.exists(filename):
        with open(sys.argv[1],"r")as f:
            return f.read()
    return ""

def dumpBinary(source):
    for i,b in enumerate(source):
        if i%48==0 and i!=0:
            print()
        print(b,end="")
    print()

def main():
    plaintext="I am a plain text, encrypt me!"
    key="abcdefgh"
    if len(str2bin(key))!=64:                     # key needs to be 64bit
        print("length of key is wrong")
        sys.exit()
    subKeys=generateKeys(str2bin(key))            # generate subkeys
    encrypted=encrypt(str2bin(plaintext),subKeys) # encryption
    decrypted=decrypt(encrypted,subKeys)          # decryption

    print("## plain text ######################################")
    print("-- text --")
    dumpBinary(plaintext)
    print("-- bit string --")
    dumpBinary(str2bin(plaintext))
    print()
    print("## encrypted text ##################################")
    print("-- bit string --")
    dumpBinary(encrypted)
    print()
    print("## decrypted text ##################################")
    print("-- text --")
    dumpBinary(decrypted)
    print("-- bit string --")
    dumpBinary(str2bin(decrypted))
    print()
    if(plaintext==decrypted):
        print("encryption succeed")
    else:
        print("encryption failed")
        
if __name__=="__main__":
    main()
