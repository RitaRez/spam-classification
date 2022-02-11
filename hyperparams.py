random_forest_hp = {
    'criterion': ("gini", "entropy"), 
    'max_depth': [1, 3, 5, 10, 20],
    'min_samples_split': [20, 40, 200, 1000],
    'min_samples_leaf': [10, 20, 100, 500]
}


svm_hp = {
    'kernel': ("linear", "poly", "rbf", "sigmoid"), 
    'degree': [1, 3, 5, 10],
    'gamma': ("scale", "auto"), 
    'shrinking': (True, False)
}

grad_boosting_hp = {
    'loss': ("deviance", "exponential"), 
    'n_estimators': [50, 100, 150, 200],
    'criterion': ("friedman_mse", "squared_error"), 
    'max_depth': [1, 3, 5, 10],    
    'min_samples_split': [2, 3, 5],
    'min_samples_leaf': [1, 2, 5, 7]
}