#s=input()
#ca=0
#cd=0
#for char in s:
    #if char.isalpha():
     #   ca+=1
    #if char.isdigit():
     #   cd+=1
#print(ca,cd)
  
#check vowels in a string
#s=input()
#c=0
#v='aeiouAEIOU'
#for char in s:
    #if char in v:
        #c+=1
#print(c)
  
# consonants
#s = input()
#c = 0
#v = 'aeiouAEIOU'
#for char in s:
    #if char not in v:
        #c += 1
#print(c)

#replacing string with hyphen
#s=input()
#s=s.replace(" ","_")
#print(s)

#without replacement
#s=input("enter string")
#s1=""
#for c in s:
    #if c.isspace():
  #      s1+='-'
   # else:
    #    s1+=c
#print(s1)


#capatalized first letter of every word using title
#s=input()
##print(s)

#capatalized first letter of every word withoutusing title
#res=''
#cap=word[0].upper()+word[1:]
    #res=res+' '+cap
#print(res)

#reverse the string without using slicing
#s = input("Enter a string: ")
#rev = ""

#print("Reversed string:", rev)

#length of the longest word in a sentence and print word
#s = input("Enter a sentence: ")
#words = s.split()
#longest = max(words, key=len)
#print("Longest word:", longest)
#print("Length:", len(longest))

#check weather the number is palindrome
#s=input("enter string")
#if s==s[::-1]:
    #print("palindrome")
#else:
    #print("not palindrome")

#remove dublicates in a string
#s=input("enter a string")
#res=""
#for char in s:
    #if char not in res:   
       # res += char
#print("String without duplicates:", res)

#finding most repeated character
#s=input("enter string:")
#freq={}
#for char in s:
    #if char not in freq:
   #  else:
 #       freq[char]+=1
#m=max(freq.values())
#for i in freq:
    #if freq[i]==m:
        #print(i)
#password validation
#password=input("enter the passwprd:")
#l=len(password)
#if not l>=6 and l<22:
 #   c=1
#for  i in range(l):
 #     uc=0
   # if password[i].islower():
        #lc=0
    #if password[i].isdigit():
     #   d=0
    #if password[i] in "!@$%^&*":
     #   sp_count+=1
    #if sp_count>=2:
     #   sp=0
    #fc+=uc+lc+d+sp+cc+c
    #print(fc)

#s = "malayalam"
i, j = 0, len(s) - 1
#is_palindrome = True

#while i <= j:
 #   if s[i] != s[j]:
  #      is_palindrome = False
   #     break
    #i += 1
    #j -= 1

#if is_palindrome:
 #   print("Palindrome")
#else:
 #   print("Not Palindrome")


















