#!/usr/bin/python3
print("".join("{}" for _ in range(97, 123)).format(*[chr(i) for i in range(97, 123)]), end="")


