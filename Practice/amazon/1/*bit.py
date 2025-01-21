"""////////////////////////////////////////////////////////////////////////////////////
• Build a system to detect single bit set in a binary data. 
	○ Number of bits as input 4. Input to the code will be string
	○ Output  - single bit (True or False or None) 
	○ How would you test it.

//
//"0001" --> 1 (True)
"0010" --> 1 (True) 
//0011 ---> 0 (False)
//0100 --> 1
//0000 --> 0 (False)
//02342 --> None

//string input -> integer base 10 --> check if this integer is one of {0001, 0010,1000,0100}  
//empty string or if len<4 : None
//Build a system to detect one-hot encoder
//Number of bits as input
//Output  - single bit

//"0001" -> [0,0,0,1] --> loop through each element sum==1 
// O(n)
// frequency=Counter( "0001") -> frequency={'0':3,'1':1} -> O()
"""
class Solution:
    def detectBits(self, s:str)-> bool:
        #edge cases
        if len(s)<4 or not s:
            retunr None
       
        result =0 
        for c in s:
            if c in ['0','1']:
                num=int(c)
                result+=num     
            else:
                return None
        return True if result==1 else False
            
            
        