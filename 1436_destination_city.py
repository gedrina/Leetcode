class Solution:
    def destCity(self, paths) -> str:
        cities = set()

        for p in paths:
            cities.add(p[0])
        
        for p in paths:
            if p[1] not in cities:
                return p[1]
            
# example
sol = Solution()
paths =[["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(sol.destCity(paths))