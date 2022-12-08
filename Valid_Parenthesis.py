def isValid(s):
        my_list = []
        for x in s:
            if(x== '(' or x=='{' or x=='['):
                my_list.append(x)

            if(x== ')' or x=='}' or x==']'):
                  if (len(my_list) == 0):
                      return False
                  if(len(my_list) > 0):
                       if(x== ')' and my_list[-1] =="(" ):
                               my_list.pop()
                       elif(x== '}' and my_list[-1] =="{" ):
                               my_list.pop()

                       elif(x== ']' and my_list[-1] =="[" ):
                               my_list.pop()
                       else:
                           my_list.append(x)

        if(len(my_list)==0):
            return True
        else:
            return False
print(isValid("(]("))