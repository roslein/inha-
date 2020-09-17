#include<iostream>
using namespace std;

int main() {
	
	int sum = 0;
	for (int i = 0; i <= 100;i++) {
		sum = sum + i;
		
	}
	cout << sum;

	return 0; // int main()은 return 0;을 해야하고 void main()은 안 해도 됨.
}