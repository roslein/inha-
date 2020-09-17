#include<iostream>
using namespace std;

int main() {
	int i = 1;
	int sum = 0;
	do 
	{
		sum = sum + i;
		i++;
	} while (i <= 100);
	cout << sum;

	return 0; // int main()은 return 0;을 해야하고 void main()은 안 해도 됨.
}