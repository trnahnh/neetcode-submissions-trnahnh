from collections import deque

class Solution:
	def foreignDictionary(self, words: list[str]) -> str:
		graph = {}
		indegree = {}

		for word in words:
			for char in word:
				graph[char] = set()
				indegree[char] = 0

		for i in range(len(words) - 1):
			first = words[i]
			second = words[i + 1]
			if len(first) > len(second) and first.startswith(second):
				return ""

			for j in range(min(len(first), len(second))):
				a = first[j]
				b = second[j]

				if a != b:
					if b not in graph[a]:
						graph[a].add(b)
						indegree[b] += 1
					break

		queue = deque()

		for char in indegree:
			if indegree[char] == 0:
				queue.append(char)

		result = []

		while queue:
			char = queue.popleft()
			result.append(char)

			for neighbor in graph[char]:
				indegree[neighbor] -= 1

				if indegree[neighbor] == 0:
					queue.append(neighbor)

		if len(result) != len(indegree):
			return ""

		return "".join(result)