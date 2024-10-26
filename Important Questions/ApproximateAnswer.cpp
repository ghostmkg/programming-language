#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int win, draw, loss;
	float x=1.0, y=0.5 , z=0.0;
	float team_points,opp_points;
	cin>>win >>draw >>loss;
	int remain_games = 4-(win+draw+loss);
	team_points= (win*x) + (draw*y);
    opp_points = (loss*x) +(draw*y);
    
    while((win+loss+draw)<=4){

	    if (remain_games+team_points>opp_points){
	        cout<<"Yes";
	    }
	    //will lose
	    else if(remain_games+team_points<=opp_points){
	        cout<<"No";
	    }
        else if(remain_games=0){
	        cout<<"No";
	    }
	    else{
	        cout<<"No";
	    }
	    break;

	}

}
