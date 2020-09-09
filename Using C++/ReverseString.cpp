// Reverse String

#include<bits/stdc++.h>
using namespace std;

int main(){
	string s;
	getline(cin,s);
	int start, end;
	start = 0;
	end = s.size()-1;
	while(start!=end){
		swap(s[start],s[end]);
		++start;
		--end;
	}
	cout<<"Op: "<<s;
}
