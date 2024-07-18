def q36():
    # https://leetcode.com/discuss/interview-question/4947290/google-phone-maximum-total-score
    arr = [5, 3, 5, 3, 5]

    last_max = arr[0]

    last_max_idx = 0

    n = len(arr)

    ans = 0

    local_sum = 0

    for i in range(1, n):
        if arr[i] >= last_max:
            ans = max(ans, i*arr[i])
            local_sum = 0
            last_max_idx = i
            last_max = arr[i]
        else:
            local_sum += arr[i]

    print(ans, local_sum)
        
    print(ans+local_sum)

def q35():
    s = "Today is the greatest day ever!"
    ans = 1
    h = {}
    repeat_count = 1
    st = ""

    words = s.split(" ")

    for w in words:
        for ch in w:
            if ch not in h:
                h[ch] = 1
            else:
                h[ch] += 1
                repeat_count = max(repeat_count, h[ch])

        print(repeat_count)
        if repeat_count > ans:
            ans = repeat_count
            st = w
        h = {}

    if st == "":
        st = words[0]

    print(st)

def q352():
    arr = [1,3,4,5,12]

    mx = -1
    mxval = -1
    n = len(arr)

    for i in range(n):
        if arr[i] > mxval:
            mxval = arr[i]
            mx = i

    arr[:] = arr[:i] + arr[i+1:]

    n = len(arr)
    dp = [0] * (mxval+1)
    dp[0] = 1
    print(arr, mxval)
    for a in arr:
        for j in range(mxval, a-1, -1):
            dp[j] += dp[j -a]

    print(dp)

    print(dp[mxval])

def q34():
    # heights = [
    # [4, 9, 7, 6, 5],
    # [2, 6, 5, 4, 3],
    # [6, 5, 1, 2, 8],
    # [3, 4, 7, 2, 5]
    # ]

    # town1 = [1, 4]
    # town2 = [3, 1]

    heights = [
    [9, 0, 1, 0],
    [0, 0, 1, 0],
    [1, 1, 1, 0]
    ]

    town1 = [1, 3]
    town2 = [2, 3]

    m = len(heights)
    n = len(heights[0])
    dp = [[0] * n for _ in range(m)]
    # dp[town1[0]][town1[1]] = 1
    # dp[town2[0]][town2[1]] = 2

    def dfs(i, j, last, val, match):
        if i<0 or i>=m or j<0 or j>=n or heights[i][j] < last or dp[i][j] == match:
            return
        dp[i][j] += val
        l = heights[i][j]
        dfs(i-1, j, l, val, match)
        dfs(i, j-1, l, val, match)
        dfs(i+1, j, l, val, match)
        dfs(i, j+1, l, val, match)

    dfs(town1[0], town1[1], 0, 1, 1)
    dfs(town2[0], town2[1], 0, 2, 3)

    ai = 0
    aj = 0
    ans = -1

    for i in range(m):
        for j in range(n):
            if dp[i][j] and heights[i][j] > ans:
                ans = heights[i][j]
                ai = i
                aj = j

    print(dp)
    print(ai, aj)

q34()
