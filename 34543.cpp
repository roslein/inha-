#include<iostream>
using namespace std;
#define start 3

int main() {
	int count = start - 1; // �ʱⰪ -1 ,count�� ��°�

	int line = 5;
	int half = line / 2 + start; // �߾Ӱ�
	
	int criterion;
	for (int row = 1; row <= line / 2 + 1; row++) { //row�� column/2+1��
		for (int j = 3; j <= 7; j++) {

			if (j <= half) {
				count++;
			}
			else {
				count--;
			}
			
			
			cout << count;
		}
		cout << endl;
		count = start - 1;
		
	}
	
	return 0;
}