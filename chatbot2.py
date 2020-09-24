dic={'laptop','mobile','speaker','handsfree','camera','offer'}
tuple_cat=('do','first','second','price','buy')

#filename="comments.txt"
#f=open(filename,"r")
#print (f.read())
#pat="D:\chatbot\h.txt"
#f=open(pat)
#tex=f.readlines()
#print(tex)
#taking the input from the user


def calculate_conditional_probabilites(dic,comment):
    length=len(comment)
    #print(f"length {length}")
    dic_temp={}
    count1=0
    for x in dic:
         count =0
         for y in comment:
            if x in y:
                count +=1
         count=count/length
         count1=count1+count
         #print(f"pro {count1}")
         dic_temp[x]=count
         
    return count1,dic_temp


def comment_sentiment_calculator(string,dic_temporaray):
    total=1
    total2=0
    length=len(string)
    #list_string=string.split()
    for x,y in dic_temporaray.items():
        #print("sentiment2")
        #print(x)
        #print(y)
        if x in string:
            total=total+1
            total2=total2+total
            #print(x)
            #print(y)
            #print(total)
            #print("HBOOOO")
        else:
           total=total*y
           total2=total2+total

        #print(f"total2{total2}")
    total2=total2/length  
    return total2


i=0
file_open=0
file_rem_name=None
print("Jarvis:May I help you?")

while i<1:

 
  
  comment=input("Customer:")  
  comment=comment.split(" ")
  #print(comment)
  #print(dic)

  ccp,comment_key_value=calculate_conditional_probabilites(dic,comment)
  csc=comment_sentiment_calculator(comment,comment_key_value)
  ccp2,comment_key_value2=calculate_conditional_probabilites(tuple_cat,comment)
  csc2=comment_sentiment_calculator(comment,comment_key_value2)
  
  #print(comment_key_value)
  #print(f"sentiment {csc}")
  #print(ccp)
  if file_open<1:
    if ccp!=0:
        #print(ccp)
           if csc>0.1:
                 
                for k in dic:
                   for c in comment:
                     if k == c:
                        file_open=file_open+1
                        file_rem_name=k
                        filename=k+".txt"
                        pat="D:\chatbot\items\\"+filename
                        f=open(pat)
                        tex=f.read().split('\n')[0]
                        print("\nJarvis:",tex)
                        #print(file_open)
             
           else:
              print("\nJarvis:We can show you some discount packages")
    else:
         print("\nJarvis:May I help You?")
         file_open=0
         f.close()
  else:
     if ccp2!=0:
           if csc2>0.1:
               for idx,val in enumerate(tuple_cat):
                   #print(idx,val)
                  #print("1st lopp")
                   for b in comment:
                      #print(b)
                   #print("2nd lopp")
                      if val == b:
                        #print(file_rem_name)
                        filename=file_rem_name+".txt"
                        pat="D:\chatbot\items\\"+filename
                        f=open(pat)
                        line_number=idx
                        #print("idx:",idx)
                        tex=f.read().split('\n')[line_number]
                        print("\nJarvis:",tex)
           else:
              print("\nJarvis:We can show you some discount packages")
         
     else: 
         print("\nJarvis:May I help You?")
         file_open=0
         f.close()
    
         
      



