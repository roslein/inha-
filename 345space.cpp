/* #include<iostream>
using namespace std;

int main() {
	int start = 65;
	int count = 64;

	int line = 13;
	int half = line / 2 +start +1;
	for (int row = 1; row <= line/2+1; row++) {
		for (int j = 1; j <= line; j++) {

			if (j <= half) {
				count++;
			}
			else {
				count--;
			}
			if (count >= half + 2 - row) {
				cout << " ";
				continue;
			}
			else {
				cout << count;
			}

		}
		cout << endl;
		count = 64;

	}
	return 0;
}
*/
#include<iostream>
using namespace std;
#define start 3

int main() {
	int count = start -1; // �ʱⰪ -1 ,count�� ��°�

	int line = 5;
	int half = line / 2 + start; // �߾Ӱ�
	int criterion;
	for (int row = 1; row <= line/2+1; row++) { //row�� column/2+1��
		for (int j = 3; j <= 7; j++) {

			if (j <= half) {
				count++;
			}
			else {
				count--;
			}
			criterion = half + 2 - row;
			if (count >= criterion) {
				cout << " ";
				continue;
			}
			else {
				cout << count;
			}

		}
		cout << endl;
		count = start-1;

	}
	return 0;
}