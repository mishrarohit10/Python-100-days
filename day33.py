dic = {
  "bruce" : "Wayne",
  "wow" : "nice"
}
# print(dic['wow']) 
# # print(dic[54])
# print(dic.get(54))
# print(dic.keys())

# for key in dic.keys():
#   print(dic[key])

print(dic.items())
for key, value in dic.items():
  print(f"{key} {value}")