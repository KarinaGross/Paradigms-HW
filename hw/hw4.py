import math

def correlation_of_Pirson(arr1: list, arr2: list):
    if len(arr1) != len(arr2) or len(arr1) == 0:
        return "Arrays must be the same length"
    
    m_x = (sum(arr1))/(len(arr1))
    m_y = (sum(arr2))/(len(arr2))
    numerator = sum(map(lambda x, y: (x - m_x) * (y - m_y), arr1, arr2))
    denominator = math.sqrt(sum(map(lambda x: (x - m_x)**2, arr1))) * math.sqrt(sum((map(lambda y: (y - m_y)**2, arr2))))
    
    if denominator == 0:
        return "The denominator must be greater than zero"

    return numerator / denominator



list_x = [1, 2, 3, 4]
list_y = [2, 3, 9, 7]
print(correlation_of_Pirson(list_x, list_y))