from typing import List, Optional, Tuple
import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError
from my_model.config.core import config


#def drop_na_inputs(*, input_data: pd.DataFrame) -> pd.DataFrame:
#    """Check model inputs for na values and filter."""
    
#    # copy of the input DataFrame
#    validated_data = input_data.copy()
#    # find variables with missing data that are not included in "numerical_vars_with_na"
#    new_vars_with_na = [var for var in config.model_config.features 
#                        if var not in config.model_config.numerical_vars_with_na
#                        and validated_data[var].isnull().sum() > 0]
#    # remove the variables previously found
#    validated_data.dropna(subset=new_vars_with_na, inplace=True)

#    return validated_data


def validate_inputs(*, input_data: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:
    """Check model inputs for unprocessable values."""

    # convert syntax error field names (beginning with numbers)
    relevant_data = input_data[config.model_config.features].copy()
    #validated_data = drop_na_inputs(input_data=relevant_data)
    errors = None

    try:
        # replace numpy nans so that pydantic can validate
#        MultipleGenderDataInputs(inputs=validated_data.replace({np.nan: None}).to_dict(orient="records"))
        MultipleGenderDataInputs(inputs=relevant_data.replace({np.nan: None}).to_dict(orient="records"))
    except ValidationError as error:
        errors = error.json()

    return relevant_data, errors


class GenderDataInputSchema(BaseModel):
    age: Optional[int]
    bmi: Optional[float]
    sex: Optional[str]
    smoker: Optional[str]
    region: Optional[str]
    children: Optional[int]


class MultipleGenderDataInputs(BaseModel):
    inputs: List[GenderDataInputSchema]
