#include <iostream>
using namespace std;

void moveZerosToEnd(int arr[], int left, int right) {
    if (left >= right) return;

    int mid = left + (right - left) / 2;

    // Recur for the left and right halves
    moveZerosToEnd(arr, left, mid);
    moveZerosToEnd(arr, mid + 1, right);

    // Merge the results: move all zeros in the range [left, right] to the end
    int temp[right - left + 1];
    int index = 0;

    // Collect non-zero elements
    for (int i = left; i <= right; i++) {
        if (arr[i] != 0) {
            temp[index++] = arr[i];
        }
    }

    // Fill the remaining positions with zeros
    while (index < (right - left + 1)) {
        temp[index++] = 0;
    }

    // Copy the result back to the original array
    for (int i = left; i <= right; i++) {
        arr[i] = temp[i - left];
    }
}

int main() {
    int A[] = {5, 6, 0, 4, 6, 0, 9, 0, 8, 7};
    int n = sizeof(A) / sizeof(A[0]);

    moveZerosToEnd(A, 0, n - 1);

    for (int i = 0; i < n; i++) {
        cout << A[i] << " ";
    }

    return 0;
}