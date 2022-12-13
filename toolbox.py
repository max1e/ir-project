def score_to_rank(scores):
    indices = list(range(1, len(scores)+1))
    return list([ranking for _, ranking in sorted(zip(scores, indices), reverse=True)])