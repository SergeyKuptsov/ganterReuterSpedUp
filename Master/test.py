from reader import *
from ganterReuter import *
from order import *
import time
start_time = time.time()
unique = {}
items_transactions = {}
sort = {}
transactions = {}
split_instances = {}
transactionsCout = 0
unique, item_transactions, sort, transactions , transactionsCount= readInTransactions('transactions.txt')
print("unique: ",unique)
print('---------------------------------------------------------------------')
print("GR original sort")
print("freqOrder: ",freqOrder(unique))
start_time = time.time()
print(ganterReuter(transactions,item_transactions,freqOrder(unique)))
print("--- %s seconds ---" % (time.time() - start_time))
print('---------------------------------------------------------------------')
print("GR original reverse sort")
print("freqReversedOrder: ",freqReverseOrder(unique))
start_time = time.time()
print(ganterReuter(transactions,item_transactions,freqReverseOrder(unique)))
print("--- %s seconds ---" % (time.time() - start_time))
print('---------------------------------------------------------------------')
print("GR original")
print("abOrder: ",abOrder(unique))
start_time = time.time()
print(ganterReuter(transactions,item_transactions,abOrder(unique)))
print("---%s seconds ---" % (time.time() - start_time))
print('---------------------------------------------------------------------')
print('---------------------------------------------------------------------')
print("GR Merge(tree)")
for c in sort:
   #print ("item: ", c, ", count: ", unique[c], "; support: ", item_transactions[c])
   if unique[c] not in split_instances:
                split_instances.update({unique[c]:[c]})
   else:
      split_instances[unique[c]].append(c)
print(split_instances)
start_time = time.time()
counter = 0
GR_outputs = []
sub_transactions = {}
for sub_inst in split_instances:
   for tr in transactions:
      newSet = list(set(transactions[tr]).intersection(set(split_instances[sub_inst])))
      if len(newSet) > 0:
         sub_transactions.update({tr:newSet})
   curr_instance={}
   for a in split_instances[sub_inst]:
      curr_instance.update({a:sub_inst})
   print(curr_instance)
   GR_outputs.append(ganterReuter(sub_transactions,item_transactions,freqOrderForMerge(curr_instance),True))
   sub_transactions.clear()
   #print(GR_outputs[counter])
print("---%s seconds ---" % (time.time() - start_time))
start_time = time.time()
while len(GR_outputs)>1:
   ct=len(GR_outputs)//2
   for i in range(len(GR_outputs)//2):
      GR_outputs[len(GR_outputs)-1-i] = mergeOutputs(GR_outputs[i],GR_outputs[len(GR_outputs)-1-i],item_transactions,transactionsCount)
   for i in range(ct):
      del GR_outputs[0]
print("--- Merged in %s seconds ---" % (time.time() - start_time))
print(GR_outputs)

print("GR Merge(direct)")
for c in sort:
   #print ("item: ", c, ", count: ", unique[c], "; support: ", item_transactions[c])
   if unique[c] not in split_instances:
                split_instances.update({unique[c]:[c]})
   else:
      split_instances[unique[c]].append(c)
start_time = time.time()
counter = 0
GR_outputs = []
sub_transactions = {}
for sub_inst in split_instances:
   for tr in transactions:
      newSet = list(set(transactions[tr]).intersection(set(split_instances[sub_inst])))
      if len(newSet) > 0:
         sub_transactions.update({tr:newSet})
   curr_instance={}
   for a in split_instances[sub_inst]:
      curr_instance.update({a:sub_inst})
   print(curr_instance)
   GR_outputs.append(ganterReuter(sub_transactions,item_transactions,freqOrderForMerge(curr_instance),True))
   sub_transactions.clear()
   #print(GR_outputs[counter])
   counter += 1
print("---%s seconds ---" % (time.time() - start_time))
dump = GR_outputs.pop(len(GR_outputs)-1)
start_time = time.time()
for instance in reversed(GR_outputs):
   dump = mergeOutputs(dump,instance, item_transactions,transactionsCount)
print(dump)
