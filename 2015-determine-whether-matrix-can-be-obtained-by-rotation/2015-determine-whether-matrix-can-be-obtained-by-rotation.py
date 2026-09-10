class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # flatMat = Counter(tuple(row) for row in mat)
        # flatTag = Counter(tuple(row) for row in target)

        # print(flatMat)
        # print(flatTag)

        # return flatMat == flatTag
        angles = 0
        size = len(mat)

        while angles < 4:
            for i in range(size):
                for j in range(i, size):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            for i in range(size):
                mat[i].reverse()

            if mat == target:
                return True
            angles+=1
        return False


