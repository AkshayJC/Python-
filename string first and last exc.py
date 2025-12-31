string=input("enter  the  string ")
n=len(string)
first=string[0]
last=string[n-1]
mod_str=last+string[1:n-1]+first
print("modifies  string:",mod_str)
