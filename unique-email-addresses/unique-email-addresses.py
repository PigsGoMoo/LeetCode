class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        
        # T: O(n^2)
#         for email in emails:
#             local = ""
#             domain = False
#             plus = False

#             for i in range(len(email)):
#                 if not domain:
#                     char = email[i]
                    
#                     if char not in ".@+" and not plus:
#                         local += char
#                     elif char == "@":
#                         domain = True
#                     elif char == "+":
#                         plus = True
                        
#                 else:
#                     local += email[i-1:]
#                     break
#             ans.add(local)
            
#         return len(ans)
                        
        # Optimizing
        for email in emails:
            # Split the email by the @ sign
            name, domain = email.split('@')
            # Then split it by the plus. We only need the part in front of the period, so grab idx 0
            # And we ignore any periods, so just replace it with an empty string
            local = name.split('+')[0].replace(".", "")
            
            ans.add(local + '@' + domain)
            
        return len(ans)