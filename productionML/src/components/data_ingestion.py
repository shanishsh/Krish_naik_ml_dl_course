import sys,os
from pathlib import Path
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation, DataTransformationConfig

@dataclass
class DataIngestionConfig:
    project_root:Path=Path(__file__).resolve().parent.parent.parent

    artifact_dir:Path=project_root/"artifact"

    train_data_path:Path=artifact_dir/"train.csv"
    test_data_path:Path=artifact_dir/"test.csv"
    raw_data_path:Path=artifact_dir/"data.csv"


class DataIngestion:
    def __init__(self) -> None:
        self.data_ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            logging.info("Read the dataset as datafrome")
            data_path=self.data_ingestion_config.project_root/"notebook"/"data"/"stud.csv"
            df=pd.read_csv(data_path)

            self.data_ingestion_config.artifact_dir.mkdir(exist_ok=True,parents=True)

            df.to_csv(self.data_ingestion_config.raw_data_path,header=True,index=False)

            logging.info("Train test split initiated")

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.data_ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.data_ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")

            return(
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)

