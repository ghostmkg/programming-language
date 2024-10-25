// Create a function to sort an array using insertion sort

#include<bits/stdc++.h>

using namespace std;

// swapping two numbers
int Swap(int &a, int &b){
    int temp;
    temp =a;
    a = b;
    b =  temp;
    return (a,b);
}

// Insertion Sort
void insertionSort(int size, int arr[]){
    for(int i=0;i<=size-1;i++){
        int j=i;
        while(j>0 && arr[j-1]>arr[j]){
            Swap(arr[j-1],arr[j]);
            j--;
        }
    }
}

int main(){
    int size;
    cout << "Enter the size of an array: "<< endl;
    cin >> size;
    int arr[size];
    cout << "Enter the elements of an array: "<<endl;
    for(int i=0;i<size;i++){
        cin >> arr[i];
    }
    insertionSort(size,arr);
    cout << "Your output is: " << endl;
    for(int i=0;i<size;i++){
        cout << arr[i] << " ";
    }
    return 0;
}