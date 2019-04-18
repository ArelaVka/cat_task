from numpy import zeros, dot, savetxt
from numpy.linalg import norm
import re


def count_lines(txt_file):
    n = 0
    with open(txt_file, 'r') as file:
        for line in file:
            n += 1
    return n


def cosine_distance(u, v):
    return 1.0 - (dot(u, v) / (norm(u) * norm(v)))


if __name__ == '__main__':
    input_file = 'sentences.txt'
    lines = count_lines(input_file)
    with open(input_file) as f:
        lines = count_lines(input_file)
        words = {}
        lcount, wcount = 0, 0
        for line in f:
            p = re.compile(r"[^a-z]+")
            tokens = p.split(line.lower())
            tokens.pop()
            for token in tokens:
                if token not in words:
                    words[token] = {
                        "index": wcount,
                        "frequency": [0] * lines
                    }
                    wcount += 1
                elif words[token]["frequency"][lcount] != 0:
                    continue
                words[token]["frequency"][lcount] = tokens.count(token)
            lcount += 1
        matrix = zeros((lines, len(words)))
        print(matrix)
        for word in words:
            i, j = 0, words[word]["index"]
            for occ in words[word]["frequency"]:
                matrix[i, j] = occ
                i += 1
        print(matrix)
        distance = []
        u = matrix[0,]
        for i in range(1, lines):
            v = matrix[i,]
            distance.append({"index": i, "distance": cosine_distance(u, v)})
        distance.sort(key=lambda x: x["distance"])
        print("The 1st closest sentence is a sentence #%d with a cosine distance of %.2f.\n" \
              "The 2nd closest sentence is a sentence #%d with a cosine distance of %.2f." % (
                  distance[0]["index"],
                  distance[0]["distance"],
                  distance[1]["index"],
                  distance[1]["distance"]
              ))
