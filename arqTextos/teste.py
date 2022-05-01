
arr=[2, 2, 2, 2, 4, 1]

print(arr)

def SumMultiplier(arr):
  resultado="false"
  for k in arr:
    for i in arr:
      if (i!=k):
        if (i*k)>(2*sum(arr)):
          print("true")
          resultado="true"
  return resultado

  # code goes here
  # return arr


# keep this function call here
print(SumMultiplier(raw))