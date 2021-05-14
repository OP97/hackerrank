def sockMerchant(n, ar):
    # Write your code here
    # 1 2 2 2 1 3 3
    return sum([ar.count(i) // 2 for i in set(ar)])