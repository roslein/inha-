#include<iostream>
using namespace std;

int main() {
	int count = 0;

	int line = 5;
	int half = line / 2 + 1;
	for (int row = 1; row <= half; row++) {
		for (int j = 1; j <= line; j++) {

			if (j <= half) {
				count++;
			}
			else {
				count--;
			}
			if (count >= 5 - row) {
				cout << " ";
				continue;
			}
			else {
				cout << count;
			}

		}
		cout << endl;
		count = 0;

	}
	return 0;
}