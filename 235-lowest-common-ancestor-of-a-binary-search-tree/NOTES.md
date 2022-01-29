Option 1:
- We can do dfs and iterate through each node and then keep track of parents for each node.
- After we get the parents for both the nodes we can get the latest commom match.
- TC : O(e+v)
​
Option 2:
- we skip the nodes that cannot have the target nodes as its childreen.
- If value is 2 and 3 and the node is 4 that means there is no point in going right of 4.
-