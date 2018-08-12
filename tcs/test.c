

// n = int(input())
// l = [2,3,5,7,11,13,17,19]
// p = n**0.5
// c = 0
// for i in l:
//     if n%i ==0:
//         c += 1
// print(2**c-1)
#include <stdio.h>
#include <math.h>


int main(){
    int list[]={2,3,5,7,11,13,17,19},i,c=0,number;
    double p;
    scanf("%d",&number);
    p=sqrt((double)number);
    for(i=0;i<8;++i){
        if(number%list[i]==0){
            c = c+1;
        }
    }
    printf("%d",(int)pow(2,c-1));
    return 0;
}

