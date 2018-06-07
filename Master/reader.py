def readInTransactions(file):
    with open(file) as f:
        read_data = f.read().splitlines()
        f.closed
    unique = {} #items superset
    item_transactions = {} #supports of items
    transactions = {} #storing transactions
    tid = 0
    for c in read_data:#counting unique values along with the inclusion counters
        tid += 1
        transactions.update({tid:c.split()})
        for char in c.split():
            if char not in unique:
                unique.update({char:1})
                item_transactions.update({char:[tid]})
            else:
                unique[char] += 1
                item_transactions[char].append(tid)
    sort = sorted(unique, key=unique.__getitem__, reverse=True) #descending ordering of the elements by frequency
    return (unique, item_transactions, sort, transactions, tid)
