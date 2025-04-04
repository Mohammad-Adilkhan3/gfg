#{ 
 # Driver Code Starts
#Initial Template for Python 3


# } Driver Code Ends

#User function Template for python3


def utility(number):
    #Write your if statement below
    if number>100:
        print("Big")

    #Write your if statement above
    print("Number")



#{ 
 # Driver Code Starts.

def main():
    t=int(input())
    while(t>0):
        number=int(input())
        utility(number)
        t-=1

        print("~")
if __name__ == "__main__": 
    main()
# } Driver Code Ends