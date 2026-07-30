import pytest
import pandas as pd
from src.cleaning import clean_meal_plan, drop_rare_meal_plan

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

def test_drop_rare_meal_plan():
    sample = pd.Series(["Meal Plan 1", "Meal Plan 3", "Meal Plan 2"])
    result = drop_rare_meal_plan(sample)
    assert  "Meal Plan 3" not in result
    assert len(result) == 2 
