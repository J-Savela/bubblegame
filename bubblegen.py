# Function for extending a bubbleset by one step in all possible ways
# Input: bubbleset
# Output: set of bubblesets
def extend(bubbleset):
    gems = set()
    for bubble in bubbleset:
        gems.update(map(abs, bubble))
    next_gem = 1
    while True:
        if next_gem not in gems:
            break
        else:
            next_gem += 1

    new_bubblesets = []
    # 1. choose bubble
    for bubble in bubbleset:
        is_redundant = False
        for i in gems:
            if i in bubble and -i in bubble:
                is_redundant = True
                break
        if is_redundant:
            continue
        new_set = bubbleset.copy()
        new_set.remove(bubble)
        # 2. choose partition
        p1 = list(bubble)
        p2 = []
        # ---
        b1 = set(p1)
        b1.add(-next_gem)
        b2 = set(p2)
        b2.add(next_gem)
        x = new_set.copy()
        x.append(b1)
        x.append(b2)
        # 3. add to collection
        new_bubblesets.append(x)
        y = len(p1)
        for i in range(y):
            p2.append(p1.pop())
            b1 = set(p1)
            b1.add(-next_gem)
            b2 = set(p2)
            b2.add(next_gem)
            x = new_set.copy()
            x.append(b1)
            x.append(b2)
            # 3. add to collection
            new_bubblesets.append(x)
    return new_bubblesets

# Function for generating bubblesets that can be resolved in d steps
# Input: integer d
# Output: set of bubblesets resolvable in d steps
def generate(d):
    bubblesets = [[set()]]
    for _ in range(d):
        new_bubblesets = []
        for bubbleset in bubblesets:
            new_bubblesets += extend(bubbleset)
        bubblesets = new_bubblesets
    return bubblesets
