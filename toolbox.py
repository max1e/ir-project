# General
def score_to_rank(scores):
    indices = list(range(1, len(scores)+1))
    return list([ranking for _, ranking in sorted(zip(scores, indices), reverse=True)])

# Evaluation
def precision(query_relevancy_labels, k):
    return (1/k)*sum(query_relevancy_labels[:k])
    
def recall(query_relevancy_labels, k):
    if sum(query_relevancy_labels) == 0:
        return 0
    return sum(query_relevancy_labels[:k])/sum(query_relevancy_labels)

def F_score(query_relevancy_labels, k):
    prekie = precision(query_relevancy_labels, k)
    reka = recall(query_relevancy_labels, k)
    return (2*prekie*reka)/(prekie+reka) if prekie + reka != 0 else 0