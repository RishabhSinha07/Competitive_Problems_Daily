import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # First, sorting according to the lastday.
        courses.sort(key=lambda x: x[1])
        totalDays = 0
        maxHeap = []
        for i in range(len(courses)):
            # If course can be taken, keep adding course
            totalDays += courses[i][0]
            # Python default is minHEap, so adding -ve of that value
            heapq.heappush(maxHeap, -courses[i][0])
            # Now, if totalDays exceeds the last day after taking that course,
            # remove the course with maximum duration
            if courses[i][1] < totalDays:
                courseWithMaxDuration = heapq.heappop(maxHeap)
                # Since, we added the negative values because of maxHeap in Python
                totalDays += courseWithMaxDuration
        # Length of heap will determine number of courses taken,
        # as it will only contain courses taken
        return len(maxHeap)