# General
def score_to_rank(scores):
    indices = list(range(1, len(scores)+1))
    return list([ranking for _, ranking in sorted(zip(scores, indices), reverse=True)])

# Evaluation
def reciprocal_rank(query_relevancy_labels):
    if not 1 in query_relevancy_labels:
        return 0

    first_relevant_idx = next(idx for idx, label in enumerate(query_relevancy_labels) if label==1)
    return 1 / (first_relevant_idx + 1)