import os
import sys
from pathlib import Path
import numpy as np
import pandas as pd
from src.exception import CustomException
import pickle




def save_object(file_path:Path,obj):
    try:

        dir_path=Path(file_path)

        dir_path.parent.mkdir(parents=True,exist_ok=True)

        with open(file_path,"wb") as file_obj:

            pickle.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)