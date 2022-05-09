class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_to_char = {
            2 : ['a','b','c'],
            3 : ['d','e','f'],
            4 : ['g','h','i'],
            5 : ['j','k','l'],
            6 : ['m','n','o'],
            7 : ['p','q','r','s'],
            8 : ['t','u','v'],
            9 : ['w','x','y','z']
        }
        
        self.combinations = deque()
        for i in digits:
            self.combinations.append(number_to_char[int(i)])
        
        self.res = []
        def CC(values, current, index):
            if index >= len(values):
                if current != "":
                    self.res.append(current)
                return
            for i in values[index]:
                CC(values, current+i, index+1)
        CC(self.combinations,'', 0)
        
        return self.res
        