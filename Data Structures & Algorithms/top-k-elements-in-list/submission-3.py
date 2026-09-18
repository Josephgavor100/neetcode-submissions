# Brute force Solution

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Count frequencies
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            
        # sort items by frequency in descending order
        sorted_items = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        
        # Collect top-k frequncy nums
        top_k_frequent = []
        for i in range(k):
            top_k_frequent.append(sorted_items[i][0])

        return top_k_frequent