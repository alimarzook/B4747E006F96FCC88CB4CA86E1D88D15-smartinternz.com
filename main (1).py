def linearsearchproduct(productlist,targetproduct):
  indices = []
  for index,product in enumerate(productlist):
    if product == targetproduct:
      indices.append(index)
  return indices

product = ["shoes","boot","lofear","shoes","sandel","shoes"]
target = "shoes"
result = linearsearchproduct(product, target)
print(result)