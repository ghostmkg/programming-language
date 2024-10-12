git #include<bits/stdc++.h>
using namespace std;
#define v vector<int>
#define pb push_back
#define ll long long int
#define pp pair<int, int>
vector<int> find_prime(int n)
{
    vector<int> p(n+1, 1);
    for(int i=2;i*i<=n;i++)
    {	
        if(p[i]==1){
            for(int j=i*i;j<=n;j+=i){
                p[j]=0;
            }
        }
    }
    v prime;
    for(int i=2;i<n;i++){
        if(p[i]==1)
        prime.push_back(i);
    }
    return prime;
}

int main()
{

    vector<int>prime = find_prime(1e6);
    for(auto x : prime )cout<<x<<" ";
    return 0;
}