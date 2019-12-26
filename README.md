# cf-educational
A simple Python script to obtain problems of "Educational Rounds" of CodeForces platform. Educational rounds generally contain straightforward problems with standard concepts which are ideal for practice. 

Unfortunately, there's no way to obtain all such problems by rating/tag on their "Problemset" page. Fortunately, CodeForces has a really nice API which can help us get what we want :)

# How to use?
Simply install the required packages (virtual environment is recommended):
```sh
pip install -r requirements.txt
```
Run:
```sh
python cf_educational.py
```
Problems will be sorted by difficulty, and will be from tags given in TAGS variable. Use semicolon for multiple tags. eg. TAGS='dp; dfs and similar'. If you want problems across all tags, keep TAGS=''.

Sample output when TAGS='dp;dfs and similar':
```
2000    GCD Counting    https://www.codeforces.com/problemset/problem/1101/D
2000    Tree Painting   https://www.codeforces.com/problemset/problem/1187/E
2100    Generate a String       https://www.codeforces.com/problemset/problem/710/E
2200    Minimal Segment Cover   https://www.codeforces.com/problemset/problem/1175/E
2200    Three Pieces    https://www.codeforces.com/problemset/problem/1065/D
2300    0-1-Tree        https://www.codeforces.com/problemset/problem/1156/D
2300    The Maximum Subtree     https://www.codeforces.com/problemset/problem/1238/F
2400    Knapsack        https://www.codeforces.com/problemset/problem/1132/E
2500    Flow Control    https://www.codeforces.com/problemset/problem/990/F
2500    Up and Down the Tree    https://www.codeforces.com/problemset/problem/1065/F
2600    Road Projects   https://www.codeforces.com/problemset/problem/1016/F
2800    Choosing Two Paths      https://www.codeforces.com/problemset/problem/1073/F
```
