int maxMeetings(int start[], int end[], int n)
    {
        // Your code here
          vector<pair<int,int>>pa;
        for(int i=0;i<n;i++)
        {
            pa.push_back(make_pair(end[i], i));
        }
        
        sort(pa.begin(), pa.end());
        int cnt=1;
        int last=pa[0].first;
        for(int i=1;i<n;i++)
        {
            if(start[pa[i].second]>last)
            {
                cnt++;
                last=pa[i].first;
            }
            
        }
        
        return cnt;
    }
