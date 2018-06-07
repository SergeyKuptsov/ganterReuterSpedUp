#defining partial order
import operator

def freqReverseOrder(unique):
    return dict(sorted(unique.items(), key=operator.itemgetter(1)));

def abOrder(unique):
    i = 1
    abSort={}
    for key in sorted(unique):
        abSort.update({key:i})
        i+=1
    return abSort

def freqOrder(unique):
    i = unique[max(unique.keys(), key=(lambda k: unique[k]))]
    print(i)
    abSort={}
    for key in unique:
        j= i - unique[key]
        abSort.update({key:j})
    return dict(sorted(abSort.items(), key=operator.itemgetter(1)));
