import json

def dec(val, base):
    val = val.lower()
    total = 0
    for ch in val:
        if '0' <= ch <= '9':
            d = ord(ch) - ord('0')
        elif 'a' <= ch <= 'z':
            d = ord(ch) - ord('a') + 10
        else:
            continue
        total = total * base + d
    return total

def lagr(pts):
    res = 0.0
    k = len(pts)
    for i in range(k):
        xi, yi = pts[i]
        term = yi
        for j in range(k):
            if i != j:
                xj, _ = pts[j]
                term *= (0 - xj) / (xi - xj)
        res += term
    return round(res)

def combs(arr, k):
    res = []
    def dfs(start, path):
        if len(path) == k:
            res.append(path[:])
            return
        for i in range(start, len(arr)):
            path.append(arr[i])
            dfs(i + 1, path)
            path.pop()
    dfs(0, [])
    return res

def run(filename):
    with open(filename, "r") as f:
        data = json.load(f)

    n = data["keys"]["n"]
    k = data["keys"]["k"]

    pts = []
    for key in data:
        if key.isdigit():
            base = int(data[key]["base"])
            yval = data[key]["value"]
            y = dec(yval, base)
            x = int(key)
            pts.append((x, y))

    kcombs = combs(pts, k)
    sec_count = {}
    for c in kcombs:
        s = lagr(c)
        if s in sec_count:
            sec_count[s] += 1
        else:
            sec_count[s] = 1

    max_freq = 0
    true_sec = None
    for s in sec_count:
        if sec_count[s] > max_freq:
            max_freq = sec_count[s]
            true_sec = s

    return true_sec, sec_count

# Run both test cases
s1, all1 = run("test_case1.json")
s2, all2 = run("test_case2.json")

with open("output.txt", "w") as f:
    f.write("Test Case 1 Secret: {}\n".format(s1))
    f.write("All Values: {}\n".format(all1))
    f.write("Test Case 2 Secret: {}\n".format(s2))
    f.write("All Values: {}\n".format(all2))

print("Secret for test_case1.json:", s1)
print("Secret for test_case2.json:", s2)
