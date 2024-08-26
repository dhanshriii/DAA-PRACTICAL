#include<iostream>
using namespace std;
int binarySearch(int arr[],int size,int key){

    int start = 0;
    int end =size-1;

    int mid=(start + end) /2;

    while(start<=end){
        if(arr[mid]==key){
            return mid;

        }
        if(key>arr[mid]){
            start=mid+1;

        }
        else{
            end=mid-1;
        }
        mid=(start+end)/2;

    }
    return -1;
}

int main(){
    int a[6]={3,6,8,23,25,28};
    int index= binarySearch(a,6,23);
     cout<<"index of 23 is at "<<index <<endl;
}
