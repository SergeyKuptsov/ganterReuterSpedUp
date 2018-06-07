#defining partial order
import operator

def freqReverseOrder(unique):
    dict_to_return ={}
    dict_to_return=dict(sorted(unique.items(), key=operator.itemgetter(1)));
    i=1
    for a in dict_to_return:
        dict_to_return[a]=i;
        i+=1
    return dict_to_return

def abOrder(unique):
    i = 1
    abSort={}
    for key in sorted(unique):
        abSort.update({key:i})
        i+=1
    i=1
    for a in abSort:
        abSort[a]=i;
        i+=1
    return abSort

def freqOrder(unique):
    dict_to_return ={}
    i = unique[max(unique.keys(), key=(lambda k: unique[k]))]
    abSort={}
    for key in unique:
        j= i - unique[key] + 1
        abSort.update({key:j})
    dict_to_return =dict(sorted(abSort.items(), key=operator.itemgetter(1)));
    i=1
    for a in dict_to_return:
        dict_to_return[a]=i;
        i+=1
    return dict_to_return

### NOW WITH MERGE

def freqReverseOrderForMerge(unique):
    return dict(sorted(unique.items(), key=operator.itemgetter(1)));

def abOrderForMerge(unique):
    i = 1
    abSort={}
    for key in sorted(unique):
        abSort.update({key:i})
        i+=1
    return abSort

def freqOrderForMerge(unique):
    i = unique[max(unique.keys(), key=(lambda k: unique[k]))]
    abSort={}
    for key in unique:
        j= i - unique[key] + 1
        abSort.update({key:j})
    return dict(sorted(abSort.items(), key=operator.itemgetter(1)));
