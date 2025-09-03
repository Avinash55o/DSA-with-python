class solution:
    def ispalindrom(self,x:int) -> bool:
        if x<0:
            return False
        
        s= str(x)
        return s == s[::-1]
    
a=solution()

print(a.ispalindrom(121)) #IS A PALINDROM
print(a.ispalindrom(123)) #IS NOT A PALINDROM
