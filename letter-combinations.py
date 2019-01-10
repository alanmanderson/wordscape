letters = ['o','a','i', 'p','n']

for i in range(len(letters)):
  for j in range(i+1, len(letters)):
    if i == 4: continue
    if j == 4: continue
    k = 4
    #for k in range(j+1, len(letters)):
    print(letters[i] + letters[j] + letters[k])
    print(letters[i] + letters[k] + letters[j])
    print(letters[j] + letters[i] + letters[k])
    print(letters[j] + letters[k] + letters[i])
    print(letters[k] + letters[i] + letters[j])
    print(letters[k] + letters[k] + letters[i])
        
