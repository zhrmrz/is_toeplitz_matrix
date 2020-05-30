class Sol:
    def is_toeplitz_matrix(self,matrix):
        rows,cols=len(matrix),len(matrix[0])
        for i in range(rows-1):
            for j in range(cols-1):
                if matrix[i][j]!=matrix[i+1][j+1]:
                    return False
        return True


if __name__ == '__main__':
    p=Sol()
    print(p.is_toeplitz_matrix( matrix = [
  [1,2],
  [2,2]
]))
