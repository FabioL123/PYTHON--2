def merge_sort(strings):
    if len(strings) <= 1:
        return strings

    # Divide the list into two halves
    mid = len(strings) // 2
    left_half = merge_sort(strings[:mid])
    right_half = merge_sort(strings[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    sorted_list = []
    i = j = 0

    # Compare elements from both halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Add any remaining elements
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list


# Example usage
words = ["banana", "apple", "cherry", "date"]
sorted_words = merge_sort(words)

print(sorted_words)