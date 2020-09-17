#include<iostream>
using namespace std;
#define start 3

int main() {
	int count = start - 1; // 초기값 -1 ,count는 출력값

	int line = 5;
	int half = line / 2 + start; // 중앙값
	
	int criterion;
	for (int row = 1; row <= line / 2 + 1; row++) { //row는 column/2+1개
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