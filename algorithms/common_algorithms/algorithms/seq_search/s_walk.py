import random
# set up variables
my_nums = [random.randint(0,100) for x in range(100)]
target = 99
ans = 'false'
# iterate through list
for num in my_nums:
	# compare index value to missing
	if num == target:
		ans = 'true'
print(ans)
