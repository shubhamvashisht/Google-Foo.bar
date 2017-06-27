 #include<stdio.h>
#include<string.h>
#include<math.h>

int convert(int number,int base){
    if(number == 0 || base==10)
        return number;

    return (number % base) + 10*convert(number / base, base);
}

int google (int k,long long int n,int b){
        int temp;
        int a[k],i,j;
        unsigned long long int x=0,y=0,z,m[k],z1;
        for(i=0;i<k;i++){
        a[k-1-i] = n%10;
        n=n/10;
    }
    for(i=0;i<k;i++)
    {
        for(j=i+1;j<k;j++)
        {
            if(a[j]<a[i])
            {
                temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
    }
    for(i=0;i<k;i++){
        x=x+a[i]*pow(b,i);
        y=y+a[i]*pow(b,k-1-i);
    }
    if(x>=y)
        z1=x-y;
    else
        z1=y-x;
    z = convert(z1,b);
    return z;
}

int main(){
    int l,c,key,i,j,ans;
    long long int o,answer[500],tenp;
    printf("Enter the length of integer : ");
    scanf("%d",&l);

    printf("\nEnter the Integer : ");
    scanf("%llu",&o);
    printf("\nEnter the base : ");
    scanf("%d",&c);
    for(key=0;key<=500;key++){
        if(key==0){
            answer[key]=google(l,o,c);
        }
        else
            answer[key]=google(l,answer[key-1],c);
    }
    tenp = answer[500];
    for(i=499;i>=1;i--){
        if(answer[i]==tenp){
            ans = 500-i;
            break;
        }
    }
    printf("\n\n%d\n\n",ans);
}
