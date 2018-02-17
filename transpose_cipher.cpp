#include <bits/stdc++.h>
using namespace std;

int main(){
	cout<<"\nEnter the message :";
	string plainText;
	cin>>plainText;
	cout<<"\nEnter number of rows and columns: ";
	int m,n;
	cin>>m>>n;
	if(plainText.length() > m*n){
		cout<<"\nMatrix size too small";
		return 0;
	}
	char encrypt[m][n];
	int e=0;
	for(int i = 0; i < m; i++){
	  for(int j = 0; j < n; j++){
	    if(e < plainText.length() && e < m*n){
	    encrypt[i][j] = plainText[e];
	    }
	    else
	      encrypt[i][j] = 'a';
	    e++;
	     
	  }
	}
	/*for(int i = 0; i < m; i++){
	  for(int j = 0; j < n; j++){
	    cout<<encrypt[i][j];
	  }
	}*/
	cout<<"\nEnter the permutation: ";
	int p[m];
	for(int i = 0; i < m; i++){
	  cin>>p[i];
	}
	char cipherText[m][n];
	for(int i = 0; i < m; i++){
	  for(int j = 0; j < n; j++){
	    cipherText[i][j] = encrypt[p[i]][j];
	  }
	}
	for(int i = 0; i < m; i++){
	  for(int j = 0; j < n; j++){
	    cout<<cipherText[i][j]<<" ";
	  }
	  cout<<endl;
	}
	cout<<"\nEnter the key to decrypt: ";
	int d[m];
	for(int i = 0; i < m; i++){
	  cin>>d[i];
	}
	char decipherText[m][n];
	for(int i = 0; i < m; i++){
	  for(int j = 0; j < n; j++){
	    decipherText[i][j] = cipherText[d[i]][j];
	  }
	}
	for(int i = 0; i < m; i++){
	  for(int j = 0; j < n; j++){
	    cout<<decipherText[i][j]<<" ";
	  }
	  cout<<endl;
	}

	return 0;
}