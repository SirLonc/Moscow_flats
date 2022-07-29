import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from catboost import CatBoostRegressor
from sklearn.metrics import r2_score
import joblib


if __name__ == '__main__':
    catboost = CatBoostRegressor(random_seed=1, loss_function='RMSE', boosting_type='Ordered', use_best_model=True)

    df = pd.read_csv('model_data.csv')
    X = df.drop('price', axis=1)
    y = df['price']

    X_trainval, X_test, y_trainval, y_test = train_test_split(X, y, test_size=0.33, random_state=11)
    X_train, X_val, y_train, y_val = train_test_split(X_trainval, y_trainval, test_size=0.25, random_state=12)
    catboost.fit(X_train, y_train, eval_set=(X_val, y_val), verbose=False, use_best_model=True)

    pred_train_cb = catboost.predict(X_train)
    pred_test_cb = catboost.predict(X_test)
    pred_cb = catboost.predict(X)

    print(f'Train R2: {r2_score(y_train,pred_train_cb): .2f}')
    print(f'Test R2: {r2_score(y_test,pred_test_cb): .2f}')
    print(f'R2: {catboost.score(X, y): .2f}')

    joblib.dump(catboost, "price_predictor.joblib")
