
def rata_rata(data):
    if len(data) == 0:
        return "Data kosong, rata-rata tidak dapat dihitung"

    total = sum(data)
    return total / len(data)


# Test case 1
print("Test 1:", rata_rata([80, 90, 70]))

# Test case 2
print("Test 2:", rata_rata([60, 80]))

# Test case 3
print("Test 3:", rata_rata([70, 80, 90, 100]))

# Test case 4: list kosong
print("Test 4:", rata_rata([]))
