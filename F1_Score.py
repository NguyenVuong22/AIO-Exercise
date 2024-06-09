# đánh giá classification model bằng F1-Score
import math
def calc_f1_score(tp, fp, fn):
  Precision = tp/(tp + fp)
  Recall = tp / (tp + fn)
  F1_score = 2*(Precision * Recall)/(Precision + Recall)
  return F1_score
assert round(calc_f1_score(tp = 2, fp = 3, fn = 5), 2) == 0.33
print(round(calc_f1_score(tp = 2, fp = 3, fn = 5), 2))