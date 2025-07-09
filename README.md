# 🌟 Day 88 — GFG 160 Days DSA Challenge
### 🧾 Problem: K Sum Paths in a Binary Tree
### 🔍 Problem Overview:
Count all the paths in a binary tree where the sum of node values equals k. The path does not need to start at the root or end at a leaf, but it must go downwards (parent to child).

## 🧠 Solution Insight:
✅ Utilized prefix sum technique with a hashmap to keep track of the sum frequencies
✅ DFS traversal while maintaining running curr_sum
✅ For each node, checked how many times curr_sum - k has occurred
✅ Used backtracking to remove the current path sum post DFS call for correctness

## 💡 Key Code Techniques:
prefix_sum[curr_sum - k] → Checks valid path count ending at current node

prefix_sum[curr_sum] += 1 → Tracks frequency of prefix sums

prefix_sum[curr_sum] -= 1 → Essential for clean backtracking

## ✅ Output Stats:
🔢 Test Cases Passed: 1120 / 1120

🎯 Accuracy: 100%

⏱️ Time Taken: 0.35 sec

🏆 Points Scored: 4 / 4

📊 Total Score: 339

## 📌 Key Takeaway:
“Optimized logic often lies hidden in unseen patterns—prefix sum is one such gem.” 🧩✨

## 📌 Hashtags:
#gfg160 #geekstreak2025 #Day88
#DSA #KSum #PrefixSum #BinaryTree
#ProblemSolving #Python #CodeNewbie
#framesbyvikash #1001DaysOfCode
