"""Quick helpers."""

def load_lines(path):
    with open(path, encoding="utf-8") as f:
        return [ln.strip() for ln in f if ln.strip()]

def clamp(value, low, high):
    return max(low, min(value, high))

def chunks(items, size):
    for i in range(0, len(items), size):
        yield items[i : i + size]

if __name__ == "__main__":
    print(most_common("abracadabra"))
