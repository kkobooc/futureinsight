import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(answer_cols, labels, train_df, model_name):
    X_train = train_df[answer_cols]
    y_train = train_df[labels]
    
    # 모델 학습
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    
    # 모델 저장
    path = f"./model/{model_name}.pkl"
    joblib.dump(clf, path)
    return clf


def use_model(test_df, model_name):
    # 모델 로드
    path = f"./model/{model_name}.pkl"
    loaded_model = joblib.load(path)
    
    # 로드한 모델로 예측 수행
    pred = loaded_model.predict(test_df)
    return pred
