class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: x[1])
        people.sort(key=lambda x: x[0], reverse=True)
        result = []

        for i in range(len(people)):
            result.insert(people[i][1], people[i])
        
        return result
