"""
deal path interview

You are given a list of log entries, where each log entry contains an IP address, a user ID, and a timestamp. Your task is to identify IP addresses that have been accessed within a 1-second window. These IP addresses are considered spam.
Task:
Write a function find_spam_ips(logs: List[str]) -> List[str] that returns a list of IP addresses that have been accessed within 1 seconds. The IP addresses should be returned in no particular order.

Constraints:
The input list logs will contain between 1 and 10^5 log entries.
Timestamps are sorted in non-decreasing order.
Each log entry has the format "IP_ADDRESS, USER_ID,TIMESTAMP", where IP_ADDRESS and USER_ID are alphanumeric strings, TIMESTAMP is a non-negative integer.

"""
from typing import List
class Solution:
    def find_spam_ips(self, logs: List[str]) -> List[str]:
        logsList = [[(x.strip()) for x in l.split(',')] for l in logs]
        #print(logsList)
       
        l=0
        result=[]
        freq = {}   #adress:freq
        for r in range(len(logsList)):           
            freq[logsList[r][0]]=freq.get(logsList[r][0],0)+1
            #print("pointers are "+ str(l),str(r))
            #print(freq)
            while int(logsList[r][2])-int(logsList[l][2]) >1:
                l+=1
                #print("shrinking window")
                #print(logsList[l][0])
                if logsList[l][0] in freq:
                    freq[logsList[l][0]]-=1
                if logsList[l][0]==0:
                    del freq[logsList[l][0]]
            #print("checking count of >4: "+str(freq[logsList[r][0]]))
            if freq[logsList[r][0]]>4:
                #print("Found a count>4")
                result.append(logsList[r][0])
            #print("ending loop for: "+str(r)+"\n\n")
                
        return result
    




s=Solution()
input1 = ["127.88.123, 23, 123456",
         "127.88.65, 23, 123456",
         "127.88.123, 23, 123457",
         "127.88.123, 23, 123457",
         "127.88.123, 23, 123457",
         "127.88.123, 23, 123457",
         "127.88.76, 23, 123459",
         "127.88.123, 23, 123460",
         "127.88.123, 23, 123461",
         ]
out1=s.find_spam_ips(input1)
print(out1==['127.88.123'])


input2 = [
    "127.0.0.1, user1, 100",
    "127.0.0.2, user2, 101",
    "127.0.0.3, user3, 102"
]
out2=s.find_spam_ips(input2)

print(out2==[])


input3  =[
    "127.0.0.1, user1, 100",
    "127.0.0.1, user1, 100",
    "127.0.0.1, user1, 100",
    "127.0.0.1, user1, 100",
    "127.0.0.1, user1, 100",  # 5 accesses at timestamp 100
    "127.0.0.2, user2, 100",
    "127.0.0.2, user2, 100",
    "127.0.0.2, user2, 100",
    "127.0.0.2, user2, 100",
    "127.0.0.2, user2, 100"   # 5 accesses at timestamp 100
]
out3=s.find_spam_ips(input3)
print(out3 ==['127.0.0.1', '127.0.0.2'])