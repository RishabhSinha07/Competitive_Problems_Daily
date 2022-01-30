class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        N, hash_value, msb_power = len(s), 0, pow(power,k,modulo)
        # msb_power will be the constant attached with the most significant bit of the substring of length k
        result = len(s)
        
        # Function to get respective values of the alphabet
        def var(char):
            return ord(char)-ord('a')+1
        
        for i in range(N-1,-1,-1):
            # Add the new value to the hash value after shifting it one bit to the left
            hash_value = (hash_value*power + var(s[i]))%modulo
            
            if i+k < N:
                # If the size of substring == k we pop the msb and left shift
                hash_value = (hash_value - var(s[i+k])*msb_power)%modulo
            
            if hash_value == hashValue:
                result = i
        
        return s[result:result+k]
        