#include<iostream>
using namespace std;
#define start 65 //시작값
#define line 13 // = column

int main() {
	char count = start - 1; // 초기값 -1 ,count는 출력값
	int half = line / 2 + start; // 중앙값
	int criterion;
	for (int row = 1; row <= line / 2 + 1; row++) { //row는 column/2+1개
		for (int j = start; j <= start+line-1; j++) { // count:12321 j:12345

			if (j <= half) {
				count++;
			}
			else {
				count--;
			}
			criterion = half + 2 - row;
			if (int(count) >= criterion) {
				cout << "  "; // 345 등과 달리 61 등 두자리니까 두칸 띄어야함. ABCD로 할때는 다시 한칸띄어야함. 글자 후 띄어 쓰기 할때는 다시 두칸 띄어야 함.
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