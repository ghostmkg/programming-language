// Create a function for sorting an array using bubble sort

#include<bits/stdc++.h>

using namespace std;

// Swapping two numbers
int Swap(int &a, int &b){
    int temp;
    temp = a;
    a = b;
    b = temp;
    return (a,b);
}

void bubbleSort(int size, int arr[]){
    for(int i=size-1;i>0;i--){
        for(int j=0;j<=i-1;j++){
            if(arr[j]> arr[j+1]) Swap(arr[j],arr[j+1]);
        }
    }
}

int main(){
    int size;
    cout << "Enter the size of an array: " << endl; 
    cin >> size;
    int arr[size];
    cout << "Enter the elements of an array: "<< endl;
    for(int i=0;i<size;i++){
        cin >> arr[i];
    }
    bubbleSort(size,arr);
    cout << "Your output is: "<< endl;
    for(int i=0; i<size;i++){
        cout << arr[i] << ' ';
    }
    return 0;
}
