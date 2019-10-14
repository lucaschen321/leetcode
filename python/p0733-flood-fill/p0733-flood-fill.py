from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        original_color = image[sr][sc]
        visited = set()
        stack = [(sr, sc)]

        while stack:
            x, y = stack.pop()
            if 0 <= x < len(image) and 0 <= y < len(image[0]) and (x, y) not in visited and image[x][y] == original_color:
                image[x][y] = newColor
                visited.add((x, y))

                stack.append((x - 1, y))
                stack.append((x + 1, y))
                stack.append((x, y - 1))
                stack.append((x, y + 1))

        return image
