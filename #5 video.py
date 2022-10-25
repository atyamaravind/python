Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
nums=[25,12,95,14]
nums
[25, 12, 95, 14]
nums[0]
25
nums[2:]
[95, 14]
nums[-1]
14
>>> names=['navin','kiran','jhon']
>>> names
['navin', 'kiran', 'jhon']
>>> values=[9.5,'Navin',25]
>>> values
[9.5, 'Navin', 25]
>>> mil=[nums,names]
>>> mil
[[25, 12, 95, 14], ['navin', 'kiran', 'jhon']]
>>> nums.append(45)
>>> mnums
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    mnums
NameError: name 'mnums' is not defined. Did you mean: 'nums'?
>>> nums
[25, 12, 95, 14, 45]
>>> nums.insert(2,77)
>>> nums
[25, 12, 77, 95, 14, 45]
>>> nums.remove(14)
>>> nums
[25, 12, 77, 95, 45]
>>> nums.pop(1)
12
>>> nums
[25, 77, 95, 45]
>>> nums.pop()
45
>>> del nums[2:]
>>> nums
[25, 77]
>>> nums.extend
<built-in method extend of list object at 0x000001EF0AEC8B40>
>>> nums.extend([29,12,14,36])
>>> nums
[25, 77, 29, 12, 14, 36]
>>> min(nums)
12
>>> max(nums)
77
>>> sum(nums)
193
>>> nums.sort()
>>> nums
[12, 14, 25, 29, 36, 77]
