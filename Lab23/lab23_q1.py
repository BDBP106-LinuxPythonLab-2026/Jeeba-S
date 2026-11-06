def dot(a, b):
    if len(a) != len(b):
        print("Error: vectors must be the same length for a dot product")
        return None
    return sum(x * y for x, y in zip(a, b))


def mat_vec(M, v):
    if any(len(row) != len(v) for row in M):
        print("Error: number of matrix columns must equal vector length")
        return None
    return [sum(m * x for m, x in zip(row, v)) for row in M]


def mat_mat(A, B):
    if any(len(row) != len(B) for row in A):
        print("Error: columns of A must equal rows of B")
        return None
    cols_B = list(zip(*B))
    return [[sum(a * b for a, b in zip(row, col)) for col in cols_B] for row in A]


def cross(a, b):
    if len(a) != 3 or len(b) != 3:
        print("Error: cross product needs two vectors of length 3")
        return None
    return [a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0]]


if __name__ == "__main__":
    print(dot([1, 2, 3], [4, 5, 6]))
    print(mat_vec([[1, 2], [3, 4]], [5, 6]))
    print(mat_mat([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
    print(cross([1, 0, 0], [0, 1, 0]))
    print(dot([1, 2], [1, 2, 3]))

