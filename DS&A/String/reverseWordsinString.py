# Reverse Words in String liter
# Write a function that takes in a string of words seperated by one or more whitespaces and returns a string
# that has these words in reverse order. You're not allowed to use split or reverse methods
# you can use join methods
# ex 1. "whitespaces    4" => "4    whitespaces"
# ex 2. "tim is great" => "great is tim"
# def reverseWordsInString(string):
# 	store = []
# 	startIdx =0

#     for idx in range(len(string)):
# 	    char = string[idx]

# 		if char == " ":
# 			store.append(string[startIdx:idx])
# 			startIdx = idx
# 		elif string[startIdx] == " ":
# 			store.append(" ")
# 			startIdx = idx
# 	store.append(string[startIdx:])
# 	reverse(store)
#     return "".join(store)

# def reverse(arr):
# 	start = 0
# 	end = len(arr)-1
# 	while start < end:
# 		arr[start],arr[end] = arr[end],arr[start]
# 		start+=1
# 		end-=1
# 	return arr

def reverseWordsInString(string):
	store = []
	startIdx =0
	for idx in range(len(string)):
		char = string[idx]
		if char == " ":
			store.insert(0, string[startIdx:idx])
			startIdx = idx
		elif string[startIdx] == " ":
			store.insert(0," ")
			startIdx = idx
	store.insert(0, string[startIdx:])
	return "".join(store)

print(reverseWordsInString("a good   example"))
