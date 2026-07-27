import pytest
import pandas as pd
from src .cleaning import clean_meal_plan

def test_cleaning():
    sample = pd.Series(["Meal Plan 1", "Not Selected", "Meal Plan 2"])   # tiny, hand-made test data — no file involved
    result = clean_meal_plan(sample)                                     # calls YOUR function, which you haven't written yet
    assert pd.isna(result[1])  

def test_meal_stays_unchanged():
    sample = pd.Series(["Meal Plan 1", "Not Selected", "Meal Plan 2"])  
    result = clean_meal_plan(sample)
    assert result[0] == "Meal Plan 1"

def test_nan_unchanged():
    sample = pd.Series(["Meal Plan 1", "Not Selected", pd.NA])  
    result = clean_meal_plan(sample)
    assert pd.isna(result[2])

