
# Time Complexity: O(∣E∣ log∣(v/e))  where |E|is the number of total flights and d is the maximum number of flights
# and v is the number of vertices
# Space Complexity: O(|V| + |E|)where |V|is the number of airports and |E|is the number of flights.
def findItinerary(tickets):
        graph = defaultdict(list)

        for src, dest in sorted(tickets, reverse=True):
            graph[src].append(dest)
            
        stack = ['JFK']
        path = []

        while stack:
            if graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            else:
                path.append(stack.pop())
        return path[::-1] # return backwards
