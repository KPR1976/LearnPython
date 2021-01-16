'''
The process_numbers() function must select all numeric values, even those values that are strings, and return them as a list. 
The values must be converted to numbers and included in the returned list. The list must be sorted. 
The function must handle the possibility that the input parameter isn't formatted as a list. In that case, it must return an empty list.

The process_names() function must select all string values that aren't numeric and return them as a list. The list must be sorted. 
The function must handle the possibility that the input parameter isn't formatted as a list. In that case, it must return an empty list.
'''

def process_numbers(data):
    result = []
    if isinstance(data, list):
        for d in data:
            if isinstance(d, int) or isinstance(d, float):
                result.append(d)
            elif d.isnumeric():
                result.append(int(d))
        return sorted(result)
    else:
        return result
    
def process_names(data):
    result = []
    if isinstance(data, list):
        for d in data:
            if isinstance(d, str) and d.isnumeric() == False:
                result.append(d)
        return sorted(result)
    else:
        return result