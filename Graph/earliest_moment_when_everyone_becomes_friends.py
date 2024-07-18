# link - https://www.naukri.com/code360/problems/the-earliest-moment-when-everyone-become-friends_1376604?leftPanelTabValue=PROBLEM

from os import *
from sys import *
from collections import *
from math import *

def minTime(logs, n):
	# Write your code here.
	ln = len(logs)
	if ln < n-1:
		return -1

	time = 0
	count = 0

	parents = list(range(n))
	ranks = [1] * n

	def find(src):
		if parents[src] == src:
			return src
		parents[src] = find(parents[src])

		return parents[src]

	def union(u, v):
		pu = find(u)
		pv = find(v)
		if pu == pv:
			return False
		if ranks[pu] < ranks[pv]:
			parents[pu] = pv
		elif ranks[pv] < ranks[pu]:
			parents[pv] = pu
		else:
			parents[pv] = pu
			ranks[pu] += 1
		# parents[pu] = pv
		return True

	logs = sorted(logs)

	for t, u, v in logs:
		if union(u, v):
			# print(u)
			# print(v)
			
			time = max(time, t)
			# print(time)
			count += 1
		if count == n-1:
			# print(f" time -- {time}")
			return time


	return 0