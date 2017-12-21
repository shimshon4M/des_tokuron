#coding:utf-8

def nLeftShift(target,n):
    tmp=target[:n]
    return target[n:]+tmp
    
def splitBinary(target):
    #前後に2分割するやつ
    1
    
def relocate(target,pattern,len):
    ret_bin=""
    for i in range(len):
        ret_bin+=target[pattern[i]-1]
    return ret_bin

def P4(target):
    pattern=[2,4,3,1]
    return relocate(target,pattern,4)

def P8(target):
    pattern=[6,3,7,4,8,5,10,9]
    return relocate(target,pattern,8)
    
def P10(target):
    pattern=[3,5,2,7,4,10,1,9,8,6]
    return relocate(target,pattern,10)

def EP(target):
    pattern=[4,1,2,3,2,3,4,1]
    return relocate(target,pattern,8)

def IP(target):
    pattern=[2,6,3,1,4,8,5,7]
    return relocate(target,pattern,8)

def IP-1(target):
    pattern=[4,1,3,5,7,2,8,6]
    return relocate(target,pattern,8)

def S0(target):
    1

def S1(target):
    1

def XOR(t1,t2):
    ret=""
    for i in range(len(t1)):
        if t1[i]==t2[i]:
            ret+="1"
        else:
            ret+="0"
    
def generateKeys(key):
    print("key :",key)
    p10=P10(key)
    ls1_head=nLeftShift(p10[:5],1)
    ls1_tail=nLeftShift(p10[5:],1)
    p8_1=P8(ls1_head+ls1_tail)
    ls2_head=nLeftShift(ls1_head,2)
    ls2_tail=nLeftShift(ls1_tail,2)
    p8_2=P8(ls2_head+ls2_tail)
    print("k1 :",k1)
    print("k2 :",k2)
    return p8_1,p8_2
    
def encryption(text):
    key="1010000010"
    k1,k2=generateKeys(key)
    ip_1=IP(text)
    ep_1=EP(ip)
    xor_1_1=XOR(ep,k1)
    s0_1=S0(xor_epk1[:4])
    s1_1=S1(xor_epk1[4:])
    p4_1=P4(s0+s1)
    xor_1_2=XOR(ip[:4]+p4)
    ep_2=EP(xor)
    xor_2_1=XOR(ep,k2)
    s0_2=S0(xor[:4])
    s1_2=S1(xor[4:])
    p4_2=P4(s0+s1)
    xor_2_2=XOR(ip_1[4:]+p4_2)
    ip1=IP1(xor_2_2+xor_1_2)
    return ip1
    
def decryption(text):
    1

def main():
    """
    授業での例
    Key:10100 00010
    k1 :1010 0100
    k2 :0100 0011
    plain :1000 0101
    cipher:0110 0110
    """
    plain_text="10000101"
    cipher_text=encryption(plain_text)
    decrypted_text=decryption(cipher_text)

    print("plain text     :",plain_text)
    print("cipher text    :",cipher_text)
    print("decrypted text :",decrypted_text)
    
    if plain_text==decrypted_text:
        print("succeed!")
    else:
        print("failed")
    
if __name__=="__main__":
    main()
