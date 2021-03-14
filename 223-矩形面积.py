class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        I = max(A, E)
        J = max(B, F)
        K = min(C, G)
        L = min(D, H)

        if K >= I and L >= J:
            return (C - A) * (D - B) + (G - E) * (H - F) - (K - I) * (L - J)

        return (C - A) * (D - B) + (G - E) * (H - F)
