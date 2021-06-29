import sys
import recursion


print(sys.argv)

_, base, exp = sys.argv
result = recursion.our_pow(int(base), int(exp))
print(result)