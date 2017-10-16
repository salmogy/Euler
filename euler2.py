# def even_fibonacci_sum(n):
    # Generate a list containing all fibonacci numbers up to n

    # Sum together all even numbers in this list.



# f(1) = 1
# f(2) = 1
# f(n) = f(n-2) + f(n-1)

def f(n):
    if (n < 2):
        return 1

    return f(n-1) + f(n-2)

print f(5000)


##############
      f(5000)
  f(4999)   f(4998)
f(4997) f(4998)   4