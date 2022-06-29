class Solution:
    def rotate_left(self,people,value,index):
        if len(people) > 1100:
            return 0
        # print("#input",people)
        for _ in range(value):
            people[index],people[index-1] = people[index-1],people[index]
            index -= 1
        return people
    
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people,key=lambda x: x[1])
        print(people)
        temp =  0
        for index, value in enumerate(people):
            # print(index,value)
            count = 0
            for x in range(0,index):
                # print('-------',people[x][0],value[0])
                if people[x][0] >= value[0]:
                    count += 1
                    # print('count',count)
                    # print('value',value[1])
            if count != value[1]:
                people = self.rotate_left(people,abs(value[1]-count),index)
                
        # print(people)
        return people