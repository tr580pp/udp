n = int(input())
weights = []
for _ in range(n):
    weights.append(float(input()))

weights.sort()
left, right = 0, n - 1
trips = 0

while left <= right:
    if left == right:
        trips += 1
        break
    if weights[left] + weights[right] <= 3.0:
        left += 1
    right -= 1
    trips += 1

print(trips)