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

	return 0; // int main()�� return 0;�� �ؾ��ϰ� void main()�� �� �ص� ��.
}