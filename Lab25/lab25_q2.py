import time
from functools import wraps
def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[{func.__name__}] execution time: {elapsed:.6f} seconds")
        return result
    return wrapper
class LinearAlgebra:
    def __init__(self, A=None, B=None):
        self._A = self._validate(A) if A is not None else self._read_matrix("A")
        self._B = self._validate(B) if B is not None else self._read_matrix("B")

    @staticmethod
    def _read_int(prompt):
        while True:
            try:
                value = int(input(prompt))
                if value <= 0:
                    raise ValueError
                return value
            except ValueError:
                print("Please enter a positive integer.")

    @classmethod
    def _read_matrix(cls, name):
        rows = cls._read_int(f"Number of rows in matrix {name}: ")
        cols = cls._read_int(f"Number of columns in matrix {name}: ")
        print(f"Enter the {cols} elements of each row of {name}, separated by spaces.")
        matrix = []
        for i in range(rows):
            while True:
                try:
                    row = [float(x) for x in input(f"  {name} row {i + 1}: ").split()]
                    if len(row) != cols:
                        raise ValueError(f"expected {cols} elements, got {len(row)}")
                    matrix.append(row)
                    break
                except ValueError as e:
                    print(f"Invalid input ({e}). Re-enter this row.")
        return matrix

    @staticmethod
    def _validate(matrix):
        if not isinstance(matrix, list) or not matrix:
            raise TypeError("A matrix must be a non-empty list of lists.")
        if not all(isinstance(row, list) and row for row in matrix):
            raise TypeError("Every row must be a non-empty list.")
        width = len(matrix[0])
        if any(len(row) != width for row in matrix):
            raise ValueError("All rows must have the same number of columns.")
        for row in matrix:
            for x in row:
                if isinstance(x, bool) or not isinstance(x, (int, float)):
                    raise TypeError(f"Matrix elements must be numbers, got {x!r}.")
        return [row[:] for row in matrix]   # defensive copy
    @property
    def matrices(self):
        """Returns the matrices (A, B)."""
        return self._A, self._B

    @matrices.setter
    def matrices(self, value):
        try:
            A, B = value
        except (TypeError, ValueError):
            raise ValueError("Assign a tuple of two matrices: (A, B).")
        self._A, self._B = self._validate(A), self._validate(B)

    def edit_element(self, which, i, j, value):
        which = which.upper()
        if which not in ("A", "B"):
            raise ValueError("Matrix name must be 'A' or 'B'.")
        A, B = self.matrices
        target = A if which == "A" else B
        if not (1 <= i <= len(target) and 1 <= j <= len(target[0])):
            raise IndexError(f"Position ({i}, {j}) is outside matrix {which}.")
        target[i - 1][j - 1] = value
        self.matrices = (A, B)

    @measure_time
    def multiply(self):
        A, B = self.matrices
        rows_A, cols_A = len(A), len(A[0])
        rows_B, cols_B = len(B), len(B[0])

        if cols_A != rows_B:
            raise ValueError(
                f"Cannot multiply: columns of A ({cols_A}) must equal rows of B ({rows_B})."
            )

        result = [[0] * cols_B for _ in range(rows_A)]
        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    result[i][j] += A[i][k] * B[k][j]
        return result


def show(matrix, name):
    print(f"{name} =")
    for row in matrix:
        print("  ", row)


if __name__ == "__main__":
    la = LinearAlgebra()
    A, B = la.matrices
    show(A, "A")
    show(B, "B")

    while input("Edit an element? (y/n): ").strip().lower() == "y":
        try:
            which = input("  Which matrix (A/B)? ")
            i = int(input("  Row number: "))
            j = int(input("  Column number: "))
            val = float(input("  New value: "))
            la.edit_element(which, i, j, val)
            A, B = la.matrices
            show(A, "A")
            show(B, "B")
        except (ValueError, IndexError) as e:
            print("Error:", e)

    try:
        show(la.multiply(), "A x B")
    except ValueError as e:
        print("Error:", e)

    n = 50
    A50 = [[(i + j) % 10 for j in range(n)] for i in range(n)]
    B50 = [[(i * j) % 10 for j in range(n)] for i in range(n)]
    big = LinearAlgebra(A50, B50)
    print("\nMultiplying two 50x50 matrices:")
    big.multiply()