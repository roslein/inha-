#include<iostream>
using namespace std;

int main() {

	int S1 = 0;
	for (int i = 1; i <= 30; i++) {
		S1 = S1 + i * i + 1;
			
	}
	cout << S1;

	return 0; // int main()은 return 0;을 해야하고 void main()은 안 해도 됨.
}