# import pickle

# with open("rainfall_risk_random_forest.pkl", "rb") as f:
#     model = pickle.load(f)

# print(type(model))
# print(hasattr(model, "estimators_"))

# import pickle

# with open(r"D:\ClimateGuardAI\models\rainfall_risk_random_forest.pkl", "rb") as f:
#     model = pickle.load(f)

# print(type(model))
# print(hasattr(model, "estimators_"))
# ===========================
# import pickle

# with open(r"D:\ClimateGuardAI\backend\ml\artifacts\rainfall_risk_random_forest.pkl", "rb") as f:
#     obj = pickle.load(f)

# print(type(obj))

#  ++++++++++++++++

# import pickle

# with open(r"D:\ClimateGuardAI\backend\ml\artifacts\rainfall_risk_random_forest.pkl", "rb") as f:
#     model = pickle.load(f)

# print(type(model))
# print(hasattr(model, "estimators_"))
# print(len(model.estimators_))


import os
import pickle

ARTIFACTS_PATH = r"D:\ClimateGuardAI\backend\ml\artifacts"

files = [
    "rainfall_risk_random_forest.pkl",
    "rainfall_risk_scaler.pkl",
    "rainfall_risk_label_encoder.pkl",
    "rainfall_risk_xgboost.pkl",
    "rainfall_risk_logistic_regression.pkl"

]

for file in files:
    file_path = os.path.join(ARTIFACTS_PATH, file)

    print(f"\nChecking {file_path}")

    with open(file_path, "rb") as f:
        obj = pickle.load(f)

    print("Type:", type(obj))

    if hasattr(obj, "n_features_in_"):
        print("n_features_in_:", obj.n_features_in_)

    if hasattr(obj, "classes_"):
        print("classes_:", obj.classes_)

    if hasattr(obj, "estimators_"):
        print("Number of trees:", len(obj.estimators_))


import os
import pickle
from sklearn.utils.validation import check_is_fitted

model_path = r"D:\ClimateGuardAI\backend\ml\artifacts\rainfall_risk_label_encoder.pkl"

with open(model_path, "rb") as f:
    model = pickle.load(f)

try:
    check_is_fitted(model)
    print("✅ Model is fitted")
except Exception as e:
    print("❌ Model is NOT fitted")
    print(type(e).__name__)
    print(e)

print("\nModel attributes:")
print("Has n_features_in_:", hasattr(model, "n_features_in_"))
print("Has estimators_:", hasattr(model, "estimators_"))

import os
import pickle
from sklearn.utils.validation import check_is_fitted

model_path = r"D:\ClimateGuardAI\backend\ml\artifacts\rainfall_risk_scaler.pkl"

with open(model_path, "rb") as f:
    model = pickle.load(f)

try:
    check_is_fitted(model)
    print("✅ Model is fitted")
except Exception as e:
    print("❌ Model is NOT fitted")
    print(type(e).__name__)
    print(e)

print("\nModel attributes:")
print("Has n_features_in_:", hasattr(model, "n_features_in_"))
print("Has estimators_:", hasattr(model, "estimators_"))

import os
import pickle
from sklearn.utils.validation import check_is_fitted

model_path = r"D:\ClimateGuardAI\backend\ml\artifacts\rainfall_risk_random_forest.pkl"

with open(model_path, "rb") as f:
    model = pickle.load(f)

try:
    check_is_fitted(model)
    print("✅ Model is fitted")
except Exception as e:
    print("❌ Model is NOT fitted")
    print(type(e).__name__)
    print(e)

print("\nrfModel attributes:")
print("Has n_features_in_:", hasattr(model, "n_features_in_"))
print("Has estimators_:", hasattr(model, "estimators_"))

import os
import pickle
from sklearn.utils.validation import check_is_fitted

model_path = r"D:\ClimateGuardAI\backend\ml\artifacts\rainfall_risk_xgboost.pkl"

with open(model_path, "rb") as f:
    model = pickle.load(f)

try:
    check_is_fitted(model)
    print("✅ Model is fitted")
except Exception as e:
    print("❌ Model is NOT fitted")
    print(type(e).__name__)
    print(e)

print("\nxgboostModel attributes:")
print("Has n_features_in_:", hasattr(model, "n_features_in_"))
print("Has estimators_:", hasattr(model, "estimators_"))

import os
import pickle
from sklearn.utils.validation import check_is_fitted

model_path = r"D:\ClimateGuardAI\backend\ml\artifacts\rainfall_risk_logistic_regression.pkl"

with open(model_path, "rb") as f:
    model = pickle.load(f)

try:
    check_is_fitted(model)
    print("✅ Model is fitted")
except Exception as e:
    print("❌ Model is NOT fitted")
    print(type(e).__name__)
    print(e)

print("\nlogModel attributes:")
print("Has n_features_in_:", hasattr(model, "n_features_in_"))
print("Has estimators_:", hasattr(model, "estimators_"))