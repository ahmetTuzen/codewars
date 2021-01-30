def longest_consec(strarr, k):
    if len(strarr) < k or k <= 0 or len(strarr) == 0:
        return ""
    result = []

    for i in range(len(strarr)-k+1):
        dummy = ""
        for j in range(k):
            dummy += strarr[i+j]
        result.append(dummy)

    lenList = [len(i) for i in result]

    maxLen = max(lenList)

    for element in result:
        if len(element) == maxLen:
            return element
