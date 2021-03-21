'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

goodies = dict()                                                                          
no = open('sample_input.txt','r')                                                  

for m in no:                                                             
    if m != '\n':                                                               
        arr = m.split(":")                                                         
        arr[1] = arr[1][1:]                                                             
        if arr[1] != "":                                                              
            if arr[1][-1] == "\n":                                                    
                arr[1] = arr[1][:-1]
            goodies[arr[0]] = int(arr[1])                                                                 
no.close()                                                                  
m = int(input("The number of employees :  "))                                                 
s = sorted(goodies.values())                                                            
l=len(s)                                                                          
min = s[-1] - s[0]                                                              
f=0                                                                                 
for i in range((l-m)+1):                                                         
    k = s[i+(m-1)] - s[i]                                                       
    if k<min:                                                                      
        min=k                                                                      
        f=i                                                                                 
out= open('sample_output.txt','w')                                                 
out.write("The goodies selected for distribution are:\n")                   
out.write("\n")
for i in range(f,f+m):                                                              
    for j in goodies.keys():                                                                                                                       
        if goodies[j] == s[i]:                                                          
            out.write(j+": ")                                               
            out.write(str(goodies[j]))                                           
            out.write("\n")
            break
out.write("\n")
out.write("And the difference between the chosen goodie with highest price and the lowest price is ")
out.write(str(min))
print("\ndifference is "+str(min))
out.close()
