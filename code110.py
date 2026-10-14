nums = []
for i in range(14, 56):
    nums.append(i)

print(nums)

#exceto no numero 25, sobrescreva os demais pela letra 'a'

for i in range(len(nums)):
    if nums[i] == 25:
        continue
    nums[i] = 'a'