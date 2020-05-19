# tasks that can be handled by the package
BINARY_CLASSIFICATION = "binary_classification"
MULTICLASS_CLASSIFICATION = "multiclass_classification"
REGRESSION = "regression"


class AlgorithmsRegistry:

    registry = {
        BINARY_CLASSIFICATION: {},
        MULTICLASS_CLASSIFICATION: {},
        REGRESSION: {},
    }

    @staticmethod
    def add(
        task_name,
        model_class,
        model_params,
        required_preprocessing,
        additional,
        default_params,
    ):
        model_information = {
            "class": model_class,
            "params": model_params,
            "required_preprocessing": required_preprocessing,
            "additional": additional,
            "default_params": default_params,
        }
        AlgorithmsRegistry.registry[task_name][
            model_class.algorithm_short_name
        ] = model_information

    @staticmethod
    def get_supported_ml_tasks():
        return AlgorithmsRegistry.registry.keys()

    @staticmethod
    def get_algorithm_class(ml_task, algorithm_name):
        return AlgorithmsRegistry.registry[ml_task][algorithm_name]["class"]

    @staticmethod
    def get_long_name(ml_task, algorithm_name):
        return AlgorithmsRegistry.registry[ml_task][algorithm_name][
            "class"
        ].algorithm_name


# Import algorithm to be registered
import supervised.algorithms.random_forest
import supervised.algorithms.xgboost
import supervised.algorithms.decision_tree
import supervised.algorithms.baseline
import supervised.algorithms.lightgbm
import supervised.algorithms.extra_trees
import supervised.algorithms.catboost
import supervised.algorithms.linear
