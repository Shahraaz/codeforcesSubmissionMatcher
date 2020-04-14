# codeforcesSubmissionMatcher
This program scrapes the solutions from codeforces and matches with user template

This code checks if code written in [toMatch.txt](https://github.com/Shahraaz/codeforcesSubmissionMatcher/blob/master/toMatch.txt) is a prefix of submission on codeforces status page(Contest Id is to be provided by you in main.py) upto a page limit that is to be set by you.

Keep in mind Codeforces has a different format for code. All new line, tabs, spaces are converted to space itself.

Original

```cpp
#include<iostream>
#include<bits/stdc++.h> 
using namespace std;
int main()
{
   long int t;
    cin>>t;
    while(t--)
    {

```
Codeforces Format

```cpp
#include&lt;iostream&gt;
#include&lt;bits/stdc++.h&gt; 
using namespace std;
int main()
{
   long int t;
    cin&gt;&gt;t;
    while(t--)
    {
```

