def f1s(pred,label):
    if pred>0 and label>0:
        return 'TP'
    if pred==0 and label==0:
        return 'TN'
    if pred==0 and label>0:
        return 'FN'
    if pred>0 and label==0:
        return 'FP'
def precesion(TP,TN,FN,FP):
    precision = TP / (TP + FP)
    recall = TP/(TP+FN)
    f1_score= 2*precision*recall / (precision + recall)
    return precision,recall,f1_score