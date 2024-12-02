import hashlib

for i in range(1, 99999999):
    result = hashlib.md5(f"iwrupvqb{i}".encode("utf8")).hexdigest()
    if str(result).startswith("000000"):
        print(result, i)
        break