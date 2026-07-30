# Generated on 2026-07-30T16:41:38.031495

def calculate_loss(y_true, y_pred):
    import numpy as np
    return np.mean((y_true - y_pred)**2)
