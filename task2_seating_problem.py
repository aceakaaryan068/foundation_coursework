import itertools
import math
import time

# students and their cities
students = {
    1: ("Asha",   "Kathmandu"),
    2: ("Bikash", "Pokhara"),
    3: ("Nisha",  "Kathmandu"),
    4: ("Rohan",  "Lalitpur"),
    5: ("Suman",  "Pokhara"),
    6: ("Pooja",  "Lalitpur"),
}

# pairs who cannot sit next to each other (friends)
friends = {(1,3), (2,5), (4,6), (1,2)}


# check if an arrangement breaks any rule
def is_valid(seats):
    for i in range(len(seats) - 1):
        a, b = seats[i], seats[i+1]
        if (a,b) in friends or (b,a) in friends:
            return False                        # rule 1: no friends adjacent
        if students[a][1] == students[b][1]:
            return False                        # rule 2: no same city adjacent
    return True


# brute force — try every single permutation
def brute_force():
    for perm in itertools.permutations(students):
        if is_valid(perm):
            return perm


# heuristic — seat most constrained students first
def heuristic():
    # count how many restrictions each student has
    score = {s: 0 for s in students}
    for a, b in friends:
        score[a] += 1
        score[b] += 1
    for a in students:
        for b in students:
            if a != b and students[a][1] == students[b][1]:
                score[a] += 1

    order = sorted(students, key=lambda s: score[s], reverse=True)

    seats = []
    for s in order:
        # try every position and pick the one with fewest violations
        best, best_v = 0, float("inf")
        for i in range(len(seats) + 1):
            trial = seats[:i] + [s] + seats[i:]
            v = sum(
                1 for j in range(len(trial)-1)
                if (trial[j],trial[j+1]) in friends
                or (trial[j+1],trial[j]) in friends
                or students[trial[j]][1] == students[trial[j+1]][1]
            )
            if v < best_v:
                best_v, best = v, i
        seats.insert(best, s)

    return tuple(seats)


# print seats nicely
def show(seats, label):
    names = " -> ".join(students[s][0] for s in seats)
    print(f"  {label}: {names}  ({'valid' if is_valid(seats) else 'invalid'})")


# --- run ---
print("\nTask 2: Seating Arrangement\n")

t = time.perf_counter()
bf = brute_force()
print(f"Brute Force   ({math.factorial(len(students)):,} permutations, {(time.perf_counter()-t)*1000:.3f}ms)")
show(bf, "Result")

t = time.perf_counter()
h = heuristic()
print(f"\nHeuristic     ({(time.perf_counter()-t)*1000:.4f}ms)")
show(h, "Result")

print("\nWhy brute force breaks down:")
print(f"  {'n':<6} {'n!':<25} {'time @ 1M/sec'}")
print("  " + "-"*45)
for n in [5, 8, 10, 12, 15, 20]:
    f = math.factorial(n)
    s = f / 1_000_000
    if   s < 60:       t = f"{s:.1f}s"
    elif s < 3600:     t = f"{s/60:.1f}min"
    elif s < 86400:    t = f"{s/3600:.0f}hrs"
    elif s < 31536000: t = f"{s/86400:.0f}days"
    else:              t = f"{s/31536000:.1e}yrs"
    print(f"  {n:<6} {f:<25,} {t}")