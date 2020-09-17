#include<iostream>
using namespace std;

/*int main() {
	int count = 0;
	int j = 0;
	for (int i = 1; i <= 5; i++) {
		
		if (count < 3) {
			j++;
		}
		else {
			j--;
		}

		cout << j;
		count++;

	}
	return 0;
}
*/
int main() {
	int count = 0;
	
	for (int j = 1; j <= 5; j++) {

		if (j <= 3) {
			count++;
		}
		else {
			count--;
		}

		cout << count;
		

	}
	return 0;
}