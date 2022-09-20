# function to check whether the string is palindrome or not 

def palin(string):
    if (string == string[::-1]):
        print(f'{string} is palindrome')
    
    else:
        print(f'{string} is not palindrome')
  
# driver code       
  
if __name__=="__main__":
    str= input("Enter a string to check: ")
    palin(str)
