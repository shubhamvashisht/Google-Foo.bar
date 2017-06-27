#include<iostream>

using namespace std ;

int ans = 0;

int func (long long int);

int func (long long int x){
    if(x==1)
        return ans;
    if(x%2 == 0){
        x=x/2;
        ans++;
        func (x);
    }
    else{
        x++;
        ans++;
        func (x);
    }
    return ans ;

}

int main(){
    long long int n;
    int m = 0;
    cin >>n ;
    m = func (n);
    cout << m << endl;
    return 0;
}
