from reader import *
from ganterReuter import *
from order import *
from random_sampler3 import *

import sys
import matplotlib.pyplot as plt
import time

text = input("Exp Num?")
#unique = {}
#items_transactions = {}
#sort = {}
#transactions = {}
#split_instances = {}
#transactionsCout = 0
#unique, item_transactions, sort, transactions , transactionsCount= readInTransactions('transactions.txt')
#print("unique: ",unique)
old_stdout = sys.stdout

if(text == "1"):
   print('---------------------------------------------------------------------')
   print("GR original sort")
   #print("freqOrder: ",freqOrder(unique))
   calls=[]
   collisions=[]
   #start_time = time.time()
   for k in range(20):
      print("Sample Size: ", (k+1)*20)
      log_file = open("Sample_"+str((k+1)*20)+"_sorted.log","w")
      sys.stdout = log_file
      print("Sample Size: ", (k+1)*20)
      for n in range(10,76):
         unique = {}
         items_transactions = {}
         sort = {}
         transactions = {}
         split_instances = {}
         closed_sets = {}
         transactionsCout = 0
         closureCalls=0
         collisions=0
         unique, item_transactions, sort, transactions , transactionsCount= readInTrunkatedChunkTransactions(random_sampler("chess.txt",(k+1)*20),n)
         closed_sets, closureCalls, collisions = ganterReuter(transactions,item_transactions,freqOrder(unique))
         #timeRn = time.time() - start_time
         if n%5==0:
            print("      itemset Size: ", n)
            print("            Closure Calls: ",closureCalls)
            print("            Colisions: ",collisions)
            print("---***---")
   #print("--- %s milliseconds ---" % ((timeRn) * 1000))
      sys.stdout = old_stdout
      log_file.close()
      print('---------------------------------------------------------------------')

if(text == "2"):
   print('---------------------------------------------------------------------')
   print("GR original reverse sort")
      #print("freqOrder: ",freqOrder(unique))
   calls=[]
   collisions=[]
   #start_time = time.time()
   for k in range(20):
      print("Sample Size: ", (k+1)*20)
      log_file = open("Sample_"+str((k+1)*20)+"_reverse_sorted.log","w")
      sys.stdout = log_file
      print("Sample Size: ", (k+1)*20)
      for n in range(10,76):
         unique = {}
         items_transactions = {}
         sort = {}
         transactions = {}
         split_instances = {}
         closed_sets = {}
         transactionsCout = 0
         closureCalls=0
         collisions=0
         unique, item_transactions, sort, transactions , transactionsCount= readInTrunkatedChunkTransactions(random_sampler("chess.txt",(k+1)*20),n)
         closed_sets, closureCalls, collisions = ganterReuter(transactions,item_transactions,freqReverseOrder(unique))
         #timeRn = time.time() - start_time
         if n%5==0:
            print("      itemset Size: ", n)
            print("            Closure Calls: ",closureCalls)
            print("            Colisions: ",collisions)
            print("---***---")
   #print("--- %s milliseconds ---" % ((timeRn) * 1000))
      sys.stdout = old_stdout
      log_file.close()
      print('---------------------------------------------------------------------')

if(text == "3"):
   print('---------------------------------------------------------------------')
   print("GR original")
   #print("freqOrder: ",freqOrder(unique))
   calls=[]
   collisions=[]
   #start_time = time.time()
   for k in range(20):
      print("Sample Size: ", (k+1)*20)
      log_file = open("Sample_"+str((k+1)*20)+"_alphabethic.log","w")
      sys.stdout = log_file
      print("Sample Size: ", (k+1)*20)
      for n in range(10,76):
         unique = {}
         items_transactions = {}
         sort = {}
         transactions = {}
         split_instances = {}
         closed_sets = {}
         transactionsCout = 0
         closureCalls=0
         collisions=0
         unique, item_transactions, sort, transactions , transactionsCount= readInTrunkatedChunkTransactions(random_sampler("chess.txt",(k+1)*20),n)
         closed_sets, closureCalls, collisions = ganterReuter(transactions,item_transactions,abOrder(unique))
         #timeRn = time.time() - start_time
         if n%5==0:
            print("      itemset Size: ", n)
            print("            Closure Calls: ",closureCalls)
            print("            Colisions: ",collisions)
            print("---***---")
   #print("--- %s milliseconds ---" % ((timeRn) * 1000))
      sys.stdout = old_stdout
      log_file.close()
      print('---------------------------------------------------------------------')
if(text == "4"):
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
   GR_outputs = [['']]
   sub_transactions = {}
   for sub_inst in split_instances:
      for tr in transactions:
         newSet = list(set(transactions[tr]).intersection(set(split_instances[sub_inst])))
         if len(newSet) > 0:
            sub_transactions.update({tr:newSet})
      curr_instance={}
      for a in split_instances[sub_inst]:
         curr_instance.update({a:sub_inst})
      ##print(curr_instance)
      GR_outputs.append(ganterReuter(sub_transactions,item_transactions,freqOrder(curr_instance),False)[0])
      sub_transactions.clear()
      #print(GR_outputs[counter])
      counter+=1
   timeRn = time.time() - start_time
   print("--- %s milliseconds ---" % ((timeRn) * 1000))
   start_time = time.time()
   while len(GR_outputs)>1:
      ct=len(GR_outputs)//2
      for i in range(len(GR_outputs)//2):
         GR_outputs[len(GR_outputs)-1-i] = mergeOutputs(GR_outputs[i],GR_outputs[len(GR_outputs)-1-i],item_transactions,transactionsCount)
      for i in range(ct):
         del GR_outputs[0]
   timeRn = time.time() - start_time
   print("---  Merged in %s milliseconds ---" % ((timeRn) * 1000))
   print(GR_outputs)
if(text == "5"):
   print('---------------------------------------------------------------------')
   print("GR Merge(direct)")
   for c in sort:
      #print ("item: ", c, ", count: ", unique[c], "; support: ", item_transactions[c])
      if unique[c] not in split_instances:
                   split_instances.update({unique[c]:[c]})
      else:
         split_instances[unique[c]].append(c)
   start_time = time.time()
   counter = 0
   GR_outputs = [['']]
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
      GR_outputs.append(ganterReuter(sub_transactions,item_transactions,freqOrder(curr_instance),False)[0])
      sub_transactions.clear()
      #print(GR_outputs[counter])
      counter += 1
   timeRn = time.time() - start_time
   print("--- %s milliseconds ---" % ((timeRn) * 1000))
   dump = GR_outputs.pop(len(GR_outputs)-1)
   start_time = time.time()
   for instance in reversed(GR_outputs):
      dump = mergeOutputs(dump,instance, item_transactions,transactionsCount)
   timeRn = time.time() - start_time
   print("---  Merged in %s milliseconds ---" % ((timeRn) * 1000))
   print(len(dump))
   print('---------------------------------------------------------------------')
