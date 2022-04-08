# Lets create the graph data first
graph = {}
graph["you"] = ["alice", "bob", "claire"] 
graph["bob"] = ["anuj", "peggy"] 
graph["alice"] = ["peggy"] 
graph["claire"] = ["thom", "jonny"] 
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

# BFS algorithm
from collections import deque

def person_is_eligible(name):
	# write custome logic that would help
	# check the necessary conditions
	return name[-1] == 'm'

def search(name):
	search_queue = deque()
	search_queue += graph[name]

	# You need to keep track of the people you have already searched
	# This is necessary to prevent infinite loop
	searched = []
	while search_queue:
		person = search_queue.popleft()
		# Only search people not already searched
		if person not in searched:
			if person_is_eligible(person):
				print("{} is eligible!".format(person))
				return True
			else:
				search_queue += graph[person]
				searched.append(person)
	return False

print(search("you"))