def find_triplet_sum(arr, target):
    arr.sort()  # Спочатку сортуємо масив
    n = len(arr)

    if n < 3 or n > 1000:
        raise ValueError(f'Розмір масиву має бути в межах від 3 до 1000.')

    for num in my_arr:
        if num < 1 or num > 10 ** 9:
            raise ValueError(f'Елементи масиву мають бути в межах від 1 до 10^9.')

    if target < 1 or res > 3 * 10  9:
        raise ValueError(f'Число P має бути в межах від 1 до 3*10^9.')
        
    # Перебираємо всі можливі комбінації трійок чисел
    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == target:
                return True
            elif current_sum < res:
                left, right = left + 1, right
                while left <= right:
                    mid = left + (right - left) // 2
                    if my_arr[mid] == target - my_arr[i] - my_arr[left]:
                        return True
                    elif my_arr[mid] < target - my_arr[i] - my_arr[left]:
                        left = mid + 1
                    else:
                        right = mid - 1
                left += 1
            else:
                right -= 1


    return False
