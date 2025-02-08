#User function Template for python3

def fizzBuzz(n):
    # Write your code here.
    if n%3==0 and n%5!=0:
        print("Fizz ")
    elif n%3!=0 and n%5==0:
        print("Buzz")
    elif n%3==0 and n%5==0:
        print("FizzBuzz")
    else:
        print(n)


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t=int(input())
    while(t>0):
        number = int(input())
        fizzBuzz(number)
        t-=1

        print("~")
if __name__ == "__main__": 
    main()


# } Driver Code Ends