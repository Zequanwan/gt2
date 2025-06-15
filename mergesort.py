def merge_sort(arr): # 2 Parameternamen optimieren 7 Funktionsbenennungsformat optimieren
    """
    Sorts a list in ascending order using the merge sort algorithm.
    
    Args:
        arr (list): The list to be sorted. 
        
    Returns:
        None: The input list is sorted in-place. 
    """
    if (len(arr) > 1): # 4 Optimieren von if-Funktionen
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        l = r = i = 0 # 5 Optimierung der Parametrierung

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                arr[i] = left[l]  # 1 Direkte Zuweisung ersetzt ASSIGNMENT-Aufruf
                l += 1
            else:
                arr[i] = right[r]  
                r += 1
            i += 1

        while l < len(left):
            arr[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            arr[i] = right[r]
            r += 1
            i += 1

import matplotlib.pyplot as plt

if __name__ == "__main__": # 6 Fügen Sie den Haupteingang hinzu
    """
    Main execution block when the script is run directly.
    """
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    sorted_list=my_list.copy() # 3 Sortieren Sie die Kopie und lassen Sie die Originalliste unverändert
    merge_sort(sorted_list)
    

    plt.figure(figsize=(10, 5))

    plt.plot(my_list, label='Original List', marker='o', color='blue', linestyle='-')
    plt.plot(sorted_list, label='Sorted List', marker='s', color='red', linestyle='--')
    
    plt.title('Comparison of Original and Sorted Lists')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.legend()

    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()