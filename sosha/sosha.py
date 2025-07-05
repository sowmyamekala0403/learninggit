def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# Example usage:
if __name__ == "__main__":
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    print(fibonacci_series(n))