class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x : abs(x[0]-x[1]), reverse=True)
        total_cost = 0
        city_a, city_b = 0,0
        
        for i,j in costs:
            if city_a == len(costs)//2:
                total_cost+=j
                city_b+=1
            elif city_b == len(costs)//2:
                total_cost+=i
                city_a+=1
            elif i <= j:
                city_a+=1
                total_cost+=i
            else:
                city_b+=1
                total_cost+=j
        
        return  total_cost