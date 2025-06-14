import heapq

def merge_k_lists(lists):
    heap = []
    result = []

    # Додаємо перші елементи всіх списків у купу
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))  # (значення, індекс списку, індекс в списку)

    while heap:
        val, list_idx, element_idx = heapq.heappop(heap)
        result.append(val)

        # Якщо в списку ще є елементи — додаємо наступний у купу
        if element_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][element_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, element_idx + 1))

    return result

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)