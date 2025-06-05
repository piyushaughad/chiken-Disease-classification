from cnnClasifier import logger
from cnnClasifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClasifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClasifier.pipeline.stage_03_training import ModelTrainingPipeline
from cnnClasifier.pipeline.stage_04_evaluation import EvaluationPipeline


STAGE_NAME= "Data ingestion stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME= "Prepare Base Model"

if __name__ == "__main__":
    try:
        logger.info(f"*********************************")
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
    except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME= "Training"

if __name__ == "__main__":
    try:
        logger.info(f"*********************************")
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
    except Exception as e:
        logger.exception(e)
        raise e
    


STAGE_NAME= "Evaluation Stage"

if __name__ == "__main__":
    try:
        logger.info(f"*********************************")
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
    except Exception as e:
        logger.exception(e)
        raise e