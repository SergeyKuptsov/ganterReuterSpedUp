import time
import math
def increment(A, i, sort):
    newA=A[:]
    newA.append(i)
    for c in sort:
        if (c in newA):
            if (i==c):
                break
            else:
                newA.remove(str(c))
    return newA

def support_of_set (A, item_transactions, transactionsCount = 1):
    if '' not in A:
        support = set(item_transactions[A[0]])
        for c in A:
            support = support.intersection(item_transactions[c])
        return support
    else:
        return range(1, transactionsCount+1)

def closure_of_set (A, transactions, item_transactions,unique):
    closure = set(unique)
    support = support_of_set(A, item_transactions)
    #print("BUILDING CLOSURE FOR: ", A, "; SUPPORT: ", support)
    #print("ELEMENTS IN ORIGINAL SUPERSET: ", closure)
    for tr in support:
            closure=closure.intersection(transactions[tr])
            #print("CLOSURE FOR TR nr_", tr,": ", closure)
    return list(closure)

def max_wrt_order (A, sort):
    if len(A)>0:
        curr_max = sort[A[0]]
        temp_sort={}
        for a in A:
            temp_sort.update({a:sort[a]})
        for a in A:
            #print(curr_max)
            if temp_sort[a] >= curr_max:
                curr_max = sort[a]
        ret_key=""
        for key in temp_sort.keys():
            if temp_sort[key] == curr_max:
                ret_key=key
        return ret_key
    else:
        for key in temp_sort.keys():
            if temp_sort[key] == max(temp_sort.keys(), key=(lambda k: temp_sort[k])):
                return key

def get_index_order(c, sort):
    return sort[c]


def ganterReuter(transactions, item_transactions, sort, merge=False):
    closedSets = []
    closedSets.append([''])
    counterCalls = 0
    counterCollisions = 0
    checkSupport = 0
    A=[]
    temp = []
    var = []
    #print("TRANSACTIONS: " ,transactions)
    #print("SORT:", sort)
    if merge:
        for tr in transactions:
            if len(list(support_of_set(transactions[tr],item_transactions)))>1:
                break
            else:
                checkSupport += 1
        if checkSupport == len(transactions):
            closedSets =  list(transactions.values())
            closedSets.append('')
            print("Closure Calls ", counterCalls)
            print("Collisions ", counterCollisions)
            return closedSets
    while ( set(var) & set(sort) != set (sort)):
        for char in sort:
            if char not in A:
                #print('CHAR: ' , char)
                temp = closure_of_set(increment(A,char,sort),transactions, item_transactions,sort)
                #print("CLOSURE: ", temp)
                counterCalls += 1
                var = temp[:]
                #print("VAR: ", var)
                #print("A: ", A)
                for elt in A:
                    if elt in temp:
                        temp.remove(str(elt))
                max_el = max_wrt_order(temp,sort)
                #print("MAX_ELT: ", max_el)
                #print("max: ", get_index_order(max_el,sort))
                #print("char: ", get_index_order(char,sort))
                #print("COMPARISON: ", get_index_order(max_el,sort) <= get_index_order(char,sort))
                if get_index_order(max_el,sort) <= get_index_order(char,sort):
                    A=var
                    closedSets.append(A)
                    break
                else:
                    counterCollisions += 1  
                    #print("Collided at: ", var, "with literal: ", char)       
    #print("Closure Calls ", counterCalls)
    #print("Collisions ", counterCollisions)
    if support_of_set(closedSets[len(closedSets)-1],item_transactions) == set():
        closedSets.pop(len(closedSets)-1)
    return [closedSets, counterCalls,counterCollisions]

def mergeOutputs(A,B,item_transactions,transactionsCount):
    start_time = time.time()
    unitedSetsDict={}
    unitedSets = []
    candidate = []
    #print("A: ", A)
    #print("B: ", B)
    for a in A:
        for b in B:
            #print("a: ", a)
            #print("b: ", b)
            sup_a = set(support_of_set(a,item_transactions,transactionsCount))
            sup_b = set(support_of_set(b,item_transactions,transactionsCount))
            if (sup_a & sup_b):
                candidate = list(set(a).union(set(b)))[:]
                #print("Candidate: ", candidate)
                if '' in candidate and len(candidate)>1:
                    candidate.remove('')
                    #print("Candidate cleared: ", candidate)
                    if str(list(sup_a & sup_b)) not in unitedSets:
                        unitedSetsDict.update({str(list(sup_a & sup_b)):candidate})
                    else:
                        if len(candidate) >= len(unitedSets[str(list(sup_a & sup_b))]):
                            unitedSetsDict[str(list(sup_a & sup_b))] = candidate
                else:
                    if str(list(sup_a & sup_b)) not in unitedSets:
                        unitedSetsDict.update({str(list(sup_a & sup_b)):candidate})
                    else:
                        if len(candidate) >= len(unitedSets[str(list(sup_a & sup_b))]):
                            unitedSetsDict[str(list(sup_a & sup_b))] = candidate
                
                #print("unitedSets: ", unitedSetsDict)
                unitedSets = list(unitedSetsDict.values())
    print("--- Merged in %s seconds ---" % (time.time() - start_time))
    return unitedSets
