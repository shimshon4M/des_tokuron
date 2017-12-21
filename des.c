#include <stdio.h>
#include <stdlib.h>

int* decimal2binaryArray(int decimal){
  /**
     10進数を2進数で表すためにint型の配列に変換
     例）59->111011
   **/
  int *binary=malloc(sizeof(int)*10);
  int i;
  for(i=0;i<10;i++){
    binary[i-1]=decimal%2;
    decimal/=2;
  }
  return binary;
}

void showBinaryArray(int *binary,int len){
  /**
     2進数を表現する配列の中身を出力
   **/
  int i;
  for(i=0;i<len;i++){
    printf("%d",binary[i]);
  }
  printf("\n");
}

void dump_binary(unsigned char* data,int size){
  int i;
  for(i=0;i<size;i++){
    if(i%16==0)
      printf("\n");
    printf("%02x ",data[i]);
  }
  printf("\n");
}

int P10(int target){
  int patterns[10]={3,5,2,7,4,10,1,9,8,6};
  
}

int P8(int target){
  int patterns[8]={6,3,7,4,8,5,10,9};
  
}

int leftShift_n(int target,int n){
  /**
     nビット左シフト
   **/
}

int binary_split(int target,int n){
  /**
     nビットずつ前後に分割
   **/
}

void generateKeys(int seed){
  /**
     seedは10bit鍵で
   **/
  int p10=P10(seed);
}

int encryption(int text){
  int seed=642; //=1010000010
  generateKeys(seed);

  return 0;
}

int decryption(int text){


  return 0;
}

int main(void){
  /**
     授業での例
     Key:10100 00010
     k1 :1010 0100
     k2 :0100 0011
     plain :1000 0101
     cipher:0110 0110
   **/
  int plain=0b10000101;
  //int cipher=encryption(plain);
  //int decrypted=decryption(cipher);

  printf("plain text     : ");showBinaryArray(decimal2binaryArray(plain),10);
  //printf("cipher text    : ");showBinariArray(decimal2binaryArray(cipher),10);
  //printf("decrypted text : ");showBinaryArray(decimal2binaryArray(decrypted),10);
  /*
  if(plain==decrypted)
    printf("succeed!\n");
  else
    printf("failed\n");
  */
  return 0;
}
