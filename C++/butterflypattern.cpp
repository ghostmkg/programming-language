#include<iostream>
using namespace std;
int main(){
    int r, c;
    for(r=1; r<=5; r++){
        for(c=1; c<=r; c++){
            cout<<"*";
        }
        for(c=1; c<=2*5-2*r; c++){
            cout<<" ";
        }
        for(c=1; c<=r; c++){
            cout<<"*";
        }
        
        cout<<endl;
    }
 for(r=5-1; r>=1; r--){
        for(c=1; c<=r; c++){
            cout<<"*";
        }
        for(c=1; c<=2*5-2*r; c++){
            cout<<" ";
        }
        for(c=1; c<=r; c++){
            cout<<"*";
        }
        
        cout<<endl;
    }
}