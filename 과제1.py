Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> rep1 = 11
>>> rep2 = 3
>>> rep3 = '서울시 부동산 매매 추이'
>>> rep4 = [2,4,7,8,10]
>>> rep5 = { 'grape':'포도','melon':'메론','apple':'사과','banana':'오렌지'}
>>> 
>>> type(rep1)
<class 'int'>
>>> type(rep2)
<class 'int'>
>>> type(rep3)
<class 'str'>
>>> type(rep4)
<class 'list'>
>>> type(rep5)
<class 'dict'>
>>> rep1 % rep2
2
>>> rep1 // rep2
3
>>>  rep2 **3
 
SyntaxError: unexpected indent
>>> rep2**3
27
>>> rep3.split()
['서울시', '부동산', '매매', '추이']
>>> rep4[2] = 6
>>> rep4
[2, 4, 6, 8, 10]
>>> len(rep4)
5
>>> sum(rep4)
30
>>> rep4.append(12)
>>> rep4
[2, 4, 6, 8, 10, 12]
>>> rep4.pop(4)
10
>>> rep4
[2, 4, 6, 8, 12]
>>> rep4.reverse()
>>> rep4
[12, 8, 6, 4, 2]
>>> rep5['banana'] = '바나나'; rep5['orange'] = '오렌지';
>>> rep5
{'grape': '포도', 'melon': '메론', 'apple': '사과', 'banana': '바나나', 'orange': '오렌지'}
>>> list(rep5.keys())
['grape', 'melon', 'apple', 'banana', 'orange']
>>> list(rep5.values())
['포도', '메론', '사과', '바나나', '오렌지']
>>> 