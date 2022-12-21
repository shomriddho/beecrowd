N = int(input())
print("{}:{}:{}"
.format(int(N/3600),
int(N%3600/60),
int(N%60)))