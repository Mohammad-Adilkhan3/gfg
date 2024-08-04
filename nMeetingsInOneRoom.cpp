int maxMeetings(int n, int start[], int end[]) {
        // CodeGenius
        vector<pair<int,int>>meetings;
        for(int i=0;i<n;i++){
            meetings.push_back({end[i],start[i]});
        }
        sort(meetings.begin(),meetings.end());
        int count=0;
        int endtime=-1;
        for(int i=0;i<n;i++){
            if(meetings[i].second>endtime){
                count++;
                endtime=meetings[i].first;
            }
        }
        return count;
    }
