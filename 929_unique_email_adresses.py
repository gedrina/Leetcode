class Solution:
    def numUniqueEmails(self, emails) -> int:
        
        # first efficient solution
        # unique = set()

        # for e in emails:
        #     local, domain = e.split('@')
        #     local = local.split('+')[0]
        #     local = local.replace('.','')
        #     unique.add((local,domain))
        # return len(unique)
        unique = set()

        for e in emails:
            i, local = 0, ''
            while e[i] not in ["@","+"]:
                if e[i] != '.':
                    local += e[i]
                i += 1
            while e[i] != '@':
                i += 1
            domain = e[i+1:]
            unique.add((local,domain))
        return len(unique)
    
# example
sol = Solution()
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(sol.numUniqueEmails(emails))
                