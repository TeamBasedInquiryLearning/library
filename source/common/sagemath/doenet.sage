def doenet_matrix(mat):
    result = ""
    for row in mat.rows():
        nums = [str(c) for c in row]
        result += f"<row>{' '.join(nums)}</row>"
    return result
