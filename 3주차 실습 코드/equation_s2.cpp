#include<iostream>
using namespace std;

int main() {
	int S2 = 0;
	for (int i = 10; i <= 30; i++) {

		for (int j = 0; j <= 5; j++) {
			S2 = S2 + i * j;
		}
	}


	cout << S2;
	return 0;
}