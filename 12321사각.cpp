#include<iostream>
using namespace std;

int main() {
	int count = 0;
	
	int line = 5;
	
	for (int row = 1; row <= line/2+1; row++) {
		for (int j = 1; j <= line; j++) {

			if (j <= line/2+1) {
				count++;
			}
			else {
				count--;
			}

			cout << count;


		}
		cout << endl;
		count = 0;
		
	}
	return 0;
}