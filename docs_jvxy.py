"""Quick helpers."""

def group_by(items, key):
    out = {}
    for it in items:
        out.setdefault(key(it), []).append(it)
    return out

def clamp(value, low, high):
    return max(low, min(value, high))

def most_common(xs):
    return max(set(xs), key=xs.count) if xs else None

# cleanup later
