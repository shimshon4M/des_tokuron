#include <stdio.h>
#include <stdlib.h>

#define DEBUG 1
#define DEBUG_DETAIL 1

int  p10[10]={3,5,2,7,4,10,1,9,8,6};
int    p8[8]={6,3,7,4,8,5,10,9};
int    p4[4]={2,4,3,1};
int    ip[8]={2,6,3,1,4,8,5,7};
int  ip_1[8]={4,1,3,5,7,2,8,6};
int    ep[8]={4,1,2,3,2,3,4,1};
int s0[4][4]={
  {1,0,3,2},
  {3,2,1,0},
  {0,2,1,3},
  {3,1,3,2}
};
int s1[4][4]={
  {0,1,2,3},
  {2,0,1,3},
  {3,0,1,0},
  {2,1,0,3}
};

void dump_binary(unsigned char* data,int size){
  int i;
  for(i=0;i<size;i++){
    if(i%16==0 & i!=0)
      printf("\n");
    printf("%02X ",data[i]);
  }
  printf("\n");
}

void lShift(unsigned char *source,unsigned char *dest,int len,int n){
  /**
    nビット左シフト
    len:targetの長さ
    n:シフトビット数
  **/
  int i,j;
  for(i=0;i<len;i++){ //copy
    dest[i]=source[i];
  }
  unsigned char carry=source[0];
  for(i=0;i<n;i++){
    for(j=0;j<len-1;j++){  
      dest[j]=dest[j+1];
    }
    dest[j]=carry;
  }
}

void relocate(unsigned char *source,unsigned char *dest, int *pattern,int len){
  /**
     source  :並べ替え前
     dest    :並べ替え後
     pattern :並べ替え規則
     len     :patternの長さ(=並べ替え後の長さ)
  **/
  int i;
  for(i=0;i<len;i++){
    dest[i]=source[pattern[i]-1];
  }
}

void sbox(unsigned char *source,unsigned char *dest,int **pattern){
  
}

void split(unsigned char *source,unsigned char *dest1,unsigned char *dest2,int len){
  /**
     sourceを2分割してdest1とdest2に格納
     len:sourceの長さ
  **/
  int i,j;
  for(i=0;i<len/2;i++){
    dest1[i]=source[i];
  }
  for(j=0;i<len;i++,j++){
    dest2[j]=source[i];
  }
}

void merge(unsigned char *source1,unsigned char *source2,unsigned char *dest,int len){
  /**
    source1とsource2を結合してdestに格納
    len:sourceの長さ
  **/
  int i,j;
  for(i=0;i<len;i++){
    dest[i]=source1[i];
  }
  for(j=i,i=0;j<len*2;j++,i++){
    dest[j]=source2[i];
  }
}

void xor(unsigned char *source1,unsigned char *source2,unsigned char *dest,int len){
  int i;
  for(i=0;i<len;i++){
    if(source1[i]==source2[i]){
      dest[i]=0;
    }
    else{
      dest[i]=1;
    }
  }
}

void generateKeys(unsigned char *key,unsigned char *k1,unsigned char *k2){
  unsigned char p10ed[8],splited_h[4],splited_t[4],shifted_1h[4],shifted_1t[4],merged1[10],shifted_2h[5],shifted_2t[5],merged2[10]; //各工程後のものを保持しておくための
  
  relocate(key,p10ed,p10,10);             //P10
  split(p10ed,splited_h,splited_t,10);
  lShift(splited_h,shifted_1h,5,1);       //LS-1
  lShift(splited_t,shifted_1t,5,1);       //LS-1
  merge(shifted_1h,shifted_1t,merged1,5);
  relocate(merged1,k1,p8,8);              //P8 ->k1
  lShift(shifted_1h,shifted_2h,5,2);      //LS-2
  lShift(shifted_1t,shifted_2t,5,2);      //LS-2
  merge(shifted_2h,shifted_2t,merged2,5);
  relocate(merged2,k2,p8,8);              //P8 ->k2

#ifdef DEBUG_DETAIL
  printf("--- generate keys ---\n");
  printf(" P10   :");dump_binary(p10ed,10);
  printf(" LS-1  :");dump_binary(shifted_1h,5);
  printf("        ");dump_binary(shifted_1t,5);
  printf(" P8    :");dump_binary(k1,8);
  printf(" LS-2  :");dump_binary(shifted_2h,5);
  printf("        ");dump_binary(shifted_2t,5);
  printf(" P8    :");dump_binary(k2,8);
#endif
}

void encryption(unsigned char *plain,unsigned char *k1,unsigned char *k2,unsigned char *encrypted){
  unsigned char
    iped[8],
    splited_1h[4],splited_1t[4],
    eped[8],                     
    xored1[8],                    
    splited_2h[4],splited_2t[4],
    sbox0ed_1[4],sbox1ed_1[4],
    splited_2h[2],splited_2t[2],
    splited_3h[2],splited_3t[2],
    splited_4h[2],splited_4t[2],
    merged1[4],
    p4ed[4],
    xored2[4];
  unsigned char *eped2[8];//後半

  relocate(plain,iped,ip,8);               // 平文をIP処理
  split(iped,splited_1h,splited_2h,8);     // 2分割
  relocate(iped,eped,ep,8);                // E/P処理
  xor(iped,k1,xored1,8);                   // 上とk1をXOR処理
  split(xored1,splited_2h,splited_2t,8);   // 2分割
  sbox(splited_2h,sbox0ed_1,s0);           // 前半をS0処理
  sbox(splited_2t,sbox1ed_1,s1);           // 後半をS1処理
  split(sbox0ed_1,splited_3h,splited_3t,4);// S0後2分割
  split(sbox1ed_1,splited_4h,splited_4t,4);// S1後2分割
  merge(splited_3h,splited_4t,merged1,2);  // S0の前半とS1の後半を結合
  relocate(merged1,p4ed,p4,4);             // 上をP4処理
  xor(p4ed,xored2,4);                      // 上をXOR処理
#ifdef DEBUG_DETAIL
  
#endif
}

void decryption(unsigned char *encrypted,unsigned char *k1,unsigned char *k2,unsigned char *decrypted){
  

}

int main(int argc, char* argv[]){
  /**
     授業での例
     Key:10100 00010 10bit
     k1 :1010 0100 8bit
     k2 :0100 0011 8bit
     plain :1000 0101 8bit
     cipher:0110 0110 8bit
   **/
  unsigned char plain[8]="10000101";//"abcdefgh";  //平文
  unsigned char key[10]="1010000010";//"1a2b3c4d5e"; //鍵
  unsigned char encrypted[8];         //暗号文
  unsigned char decrypted[8];         //複合文
  unsigned char k1[8],k2[8];          //sub鍵1,2
  
  generateKeys(key,k1,k2);
  encryption(plain,k1,k2,encrypted);
  decryption(encrypted,k1,k2,decrypted);
  
#ifdef DEBUG
  printf("--- plain text ---\n");
  dump_binary(plain,8);
  printf("--- keys ---\n");
  printf("key      :");dump_binary(key,10);
  printf("sub key1 :");dump_binary(k1,8);
  printf("sub key2 :");dump_binary(k2,8);
  
#endif

  /*
  if(plain==decrypted)
    printf("succeed!\n");
  else
    printf("failed\n");
  */
  return 0;
}
