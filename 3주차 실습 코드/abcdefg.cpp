#include<iostream>
using namespace std;
#define start 65 //���۰�
#define line 13 // = column

int main() {
	char count = start - 1; // �ʱⰪ -1 ,count�� ��°�
	int half = line / 2 + start; // �߾Ӱ�
	int criterion;
	for (int row = 1; row <= line / 2 + 1; row++) { //row�� column/2+1��
		for (int j = start; j <= start+line-1; j++) { // count:12321 j:12345

			if (j <= half) {
				count++;
			}
			else {
				count--;
			}
			criterion = half + 2 - row;
			if (int(count) >= criterion) {
				cout << "  "; // 345 ��� �޸� 61 �� ���ڸ��ϱ� ��ĭ ������. ABCD�� �Ҷ��� �ٽ� ��ĭ������. ���� �� ��� ���� �Ҷ��� �ٽ� ��ĭ ���� ��.
				continue;
			}
			else {
				cout << count<<" ";
			}
			
			
		}
		cout << endl;
		count = start - 1;

	}
	return 0;
}