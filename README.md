# competitive-programming-
Time Complexity Analysis 
consider following code in c 
int make_magic(int n) {
  int t = 0;
  for (int x=1; x<n; x*=2){
    for (int y=0; y<x; y++){
      t++; 
    }
  }
}
Analysis: 
The run time is O(n)
Basically, 
i = n, inner loops run n times 
i = n/2, inner loops run n/2 times 
i = n/4, inner loops run n/4 times 
...
In total, n + n/2 + n/4 + ... = 2n 
