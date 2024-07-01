# Wrong Submission
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         longestPrefix = strs[0]
#         print(strs[1::1])
#         for i in strs[1::1]:
#             # print(i, " -> ", i.find(longestPrefix))
#             if(i.find(longestPrefix) == -1):
#                 # print("Here!")
#                 while(i.find(longestPrefix) != -1 or longestPrefix != ""):
#                     # print("Decreaseing longestPrefix...")
#                     longestPrefix = longestPrefix[:len(longestPrefix)-1]
#                     # print("longestPrefix-> ", longestPrefix)
#                     if(i.find(longestPrefix) != -1):
#                         break
        
#         return longestPrefix
# Here, I was checking whether the longestPrefix was present ANYWHERE because I was checking it at -1. But the test case ["c","acc","ccc"] bowled me as I got "c" present at 1 in "acc" but it should be able to find that chatacter at the 0th character - so, I changed it and got the right answer

# Correct:

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestPrefix = strs[0]
        print(strs[1::1])
        for i in strs[1::1]:
            print(i, " -> ", i.find(longestPrefix))
            if(i.find(longestPrefix) != 0):
                while(i.find(longestPrefix) != 0 or longestPrefix != ""):
                    print("Decreaseing longestPrefix...")
                    longestPrefix = longestPrefix[:len(longestPrefix)-1]
                    print("longestPrefix-> ", longestPrefix)
                    if(i.find(longestPrefix) == 0):
                        break
        
        return longestPrefix
                

                
# Changes Made: I checked if the longestPrefix was ever present at 0th index or not.
    
                

                


        