def rabin_karp(haystack, needle):

    if not needle or not haystack or len(haystack) < len(needle):
        return []


    def hash_str(s):
        h = 0
        for ch in s:
            h = (h * 256 + ord(ch)) % 101
        return h

    needle_hash = hash_str(needle)
    haystack_hash = hash_str(haystack[:len(needle)])
    indices = []


    for i in range(len(haystack) - len(needle) + 1):

        if haystack_hash == needle_hash and haystack[i:i+len(needle)] == needle:
            indices.append(i)

        if i < len(haystack) - len(needle):
            haystack_hash = (haystack_hash * 256 - ord(haystack[i]) * 256**len(needle) + ord(haystack[i+len(needle)])) % 101

    return indices




