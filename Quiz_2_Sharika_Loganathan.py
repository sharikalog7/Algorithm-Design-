{\rtf1\ansi\ansicpg1252\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww30040\viewh18340\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 """\
Created on Tue Sep 13 21:53:57 2022\
\
@author: sharikaloganathan\
"""\
\
\
#\
#Test Case 1: Find 8 in \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}\
\
#Test Case 2: Find 32 in \{1,5,7,9,15,30,33,37,41,42,43,65,69\}\
\
  \
# Function to perform T3 sublist search\
def sublist3search(l, r, key, arr):\
  \
    if (r >= l):\
  \
        # Find the mid1 and mid2\
        midval1 = l + (r - l) //3\
        midval2 = r - (r - l) //3\
  \
        # CChecking if key is present\
        if (arr[midval1] == key): \
            return midval1\
          \
        if (arr[midval2] == key): \
            return midval2\
          \
      \
        if (key < arr[midval1]): \
  \
            \
            return sublist3search(l, midval1 - 1, key, arr)\
            print(key)\
          \
        elif (key > arr[midval2]): \
  \
            \
            return sublist3search(midval2 + 1, r, key, arr)\
          \
        else: \
  \
          \
            \
            return sublist3search(midval1 + 1, \
                                 midval2 - 1, key, arr)\
        \
          \
    # Key not found\
    \
    return -1\
  \
# Driver code\
\
\
if __name__ == '__main__':\
    \
   # sdict = \{1,5,7,9,15,30,33,37,41,42,43,65,69:8\}\
   \
    l = 0\
    \
    #Test Case 1 \
    arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\
    r = len(arr)   \
    \
    \
    key=8   \
    pos= sublist3search(l, r, key, arr)    \
\
    if pos >=1:\
    \
        print( "Item",key, "is found at position ", pos)\
        print()\
    \
    else:\
    \
        print(key ,"not found\\ n ")\
        \
        \
\
    #Test Case 2 \
    arr=[1,5,7,9,15,30,33,37,41,42,43,65,69]\
    r = len(arr)\
    key=32   \
    pos = sublist3search(l, r, key, arr)\
\
\
    if pos >=1:\
    \
        print( key, "is found at ", pos )\
    \
    else:\
    \
        print(key ,"not found")}