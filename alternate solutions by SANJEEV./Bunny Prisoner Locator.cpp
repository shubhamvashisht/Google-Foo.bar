#include<iostream>
#include<math.h>

using namespace std;

int main(){
    int row ,col ,cnt = 0 ;
    long long int ans ;
    cin >> row >> col ;                 //Taking the coordinates of the prison from user
    while(col>1){
        col--;
        row++;                          //Moving diagonally towards right up to bottom
        cnt++;
    }
    ans = row*(row+1)/2 ;
    cout << ans-cnt ;                   //Prints out the prisoner ID on screen
    return 0;
}
