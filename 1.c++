#include <iostream>
using namespace std;
int main(){
    int a;
    cin>>a;
    char arr[a][5];
    for(int i = 0; i<a; i++){
        for(int j = 0; j < 5; j++){
            cin>>arr[i][j];
        }
    }
    bool r = false;
    for(int i = 0; i<a; i++){
        for(int j = 0; j < 5; j++){
            if((arr[i][j] == 'X') and arr[i][j+1] == 'X' and j != 6){
                cout<< "YES";
                r = true;
                arr[i][j] = '+';
                arr[i][j+1] = '+';
            }
        }
    } 
    if(r = false){
        cout<<"NO";
        return 0;
    } 
    for(int i = 0; i<a; i++){
        for(int j = 0; j < 5; j++){
            cout<<arr[i][j];
        } cout<<endl;
    }
    
}