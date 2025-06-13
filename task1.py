import heapq

def min_connection_cost(cables):
    heapq.heapify(cables)  # створити min-heap
    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        cost = first + second
        total_cost += cost
        heapq.heappush(cables, cost)

    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
print(min_connection_cost(cables))  # Виведе: 29

# 1. [2, 3, 4, 6] -> з'єднуємо 2+3=5 → нова купа: [4, 5, 6]
# 2. [4, 5, 6]   -> з'єднуємо 4+5=9 → нова купа: [6, 9]
# 3. [6, 9]     -> з'єднуємо 6+9=15 → нова купа: [15]

# Сума всіх об'єднань: 5 + 9 + 15 = 29