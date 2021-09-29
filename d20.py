#!/usr/bin/env python`
import random
import sys

entries = {}
totalweight = 0.0
d20 = []

task = raw_input("enter first task name:  ")
weight = float(raw_input("give weight to the task (use whatever scale u want):  "))

while task != "":
    print "loading up", task, weight
    totalweight += weight
    entries[task] = weight
    task = raw_input("enter task name, or hit enter  if that's enough:  ")
    if task != "": weight = float(raw_input("give weight (whatever):  "))
print "entries", entries
print "totalweight", totalweight


for key in entries:
    orig_weight = entries[key]
    percentageweight = orig_weight/totalweight
    #print "percent", percentageweight
    #now you need to turn the persent into a num out of 20
    normalweight = int(percentageweight*20)
    if normalweight < 1: normalweight = 1
    #print "normalizedkey", normalweight
    while normalweight > 0:
        d20.append(key)
        normalweight -= 1
while len(d20) < 20:
    d20.append("joker") #hmm they stil dont add up
for n in range (0, len(d20)):
    print str(n+1), d20[n]

#if (len(sys.arv) >= 2 && sys.argv[1] == "m"):
if (sys.argv[1] == "m"):
    pass
else:
    dieroll = random.randint(0,19)
    print "rolled a", dieroll+1
    print "so, time for a", d20[dieroll]
