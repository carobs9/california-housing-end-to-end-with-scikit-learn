"""
California Housing, End to End with Scikit-Learn

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - load_housing
import tempfile
import tarfile
import urllib.request
from pathlib import Path

import pandas as pd


URL = "https://github.com/ageron/data/raw/main/housing.tgz"

def load_housing():
    base = Path(tempfile.gettempdir())
    tgz_path = base / "housing.tgz"
    csv_path = base / "housing" / "housing.csv"

    if not tgz_path.is_file():
        urllib.request.urlretrieve(URL, tgz_path)

    if not csv_path.is_file():
        with tarfile.open(tgz_path) as tar:
            tar.extractall(path=base)

    return pd.read_csv(csv_path)

# Step 2 - income_categories
def income_categories(df):
    cats = pd.cut(
        df["median_income"],
        bins=[0, 1.5, 3, 4.5, 6, np.inf],
        labels=[1, 2, 3, 4, 5],
    )
    return cats.astype(int)

# Step 3 - stratified_split (not yet solved)
# TODO: implement

# Step 4 - explore_correlations (not yet solved)
# TODO: implement

# Step 5 - add_ratio_features (not yet solved)
# TODO: implement

# Step 6 - split_features_labels (not yet solved)
# TODO: implement

# Step 7 - ClusterSimilarity (not yet solved)
# TODO: implement

# Step 8 - numeric_pipeline (not yet solved)
# TODO: implement

# Step 9 - categorical_pipeline (not yet solved)
# TODO: implement

# Step 10 - build_preprocessing (not yet solved)
# TODO: implement

# Step 11 - rmse (not yet solved)
# TODO: implement

# Step 12 - dummy_baseline_rmse (not yet solved)
# TODO: implement

# Step 13 - cross_val_rmse (not yet solved)
# TODO: implement

# Step 14 - linear_model (not yet solved)
# TODO: implement

# Step 15 - forest_model (not yet solved)
# TODO: implement

# Step 16 - random_search (not yet solved)
# TODO: implement

# Step 17 - test_rmse (not yet solved)
# TODO: implement

# Step 18 - bootstrap_rmse_ci (not yet solved)
# TODO: implement

# Step 19 - feature_importances (not yet solved)
# TODO: implement

# Step 20 - worst_errors (not yet solved)
# TODO: implement

# Step 21 - save_and_reload (not yet solved)
# TODO: implement

# Step 22 - predict_new (not yet solved)
# TODO: implement

