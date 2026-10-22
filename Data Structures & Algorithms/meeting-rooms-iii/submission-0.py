class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = []
        count = [0] * n

        for i in range(n):
            heapq.heappush(available, (0, i))
        
        for start, end in meetings:
            while available and available[0][0] < start:
                endTime, room = heapq.heappop(available)
                heapq.heappush(available, (start, room))
            
            endTime, room = heapq.heappop(available)
            heapq.heappush(available, (endTime + (end - start), room))
            count[room] += 1
        
        return count.index(max(count))