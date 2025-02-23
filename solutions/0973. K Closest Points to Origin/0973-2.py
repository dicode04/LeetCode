class Solution:
  def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    def squareDist(p: List[int]) -> int:
      return p[0] * p[0] + p[1] * p[1]

    def quickSelect(l: int, r: int, k: int) -> None:
      pivot = points[r]

      nextSwapped = l
      for i in range(l, r):
        if squareDist(points[i]) <= squareDist(pivot):
          points[nextSwapped], points[i] = points[i], points[nextSwapped]
          nextSwapped += 1
      points[nextSwapped], points[r] = points[r], points[nextSwapped]

      count = nextSwapped - l + 1  # Of points <= pivot
      if count == k:
        return
      if count > k:
        quickSelect(l, nextSwapped - 1, k)
      else:
        quickSelect(nextSwapped + 1, r, k - count)

    quickSelect(0, len(points) - 1, K)
    return points[0:K]
