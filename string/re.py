def nonrepeating(str1):
   charorder = []
   count = {}
   for i in str1:
      if i in count:
         count[i] += 1
      else:
         count[i] = 1
         charorder.append(i)
   for i in charorder:
      if count[i] == 1:
        return i
   return None

print(nonrepeating('malayalam'))
