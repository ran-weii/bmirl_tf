from copy import deepcopy


def create_SAC_algorithm(variant, *args, **kwargs):
    from .sac import SAC

    algorithm = SAC(*args, **kwargs)

    return algorithm


def create_SQL_algorithm(variant, *args, **kwargs):
    from .sql import SQL

    algorithm = SQL(*args, **kwargs)

    return algorithm

def create_RAMBO_algorithm(variant, *args, **kwargs):
    from rambo.algorithms.rambo import RAMBO

    algorithm = RAMBO(config=variant, *args, **kwargs)

    return algorithm

def create_RIRL_algorithm(variant, *args, **kwargs):
    from rambo.algorithms.rirl import RIRL

    algorithm = RIRL(config=variant, *args, **kwargs)

    return algorithm

def create_BIRL_algorithm(variant, *args, **kwargs):
    from rambo.algorithms.birl import BIRL

    algorithm = BIRL(config=variant, *args, **kwargs)

    return algorithm

ALGORITHM_CLASSES = {
    'SAC': create_SAC_algorithm,
    'SQL': create_SQL_algorithm,
    'RAMBO': create_RAMBO_algorithm,
    'RIRL': create_RIRL_algorithm,
    'BIRL': create_BIRL_algorithm
}


def get_algorithm_from_variant(variant,
                               *args,
                               **kwargs):
    algorithm_params = variant['algorithm_params']
    algorithm_type = algorithm_params['type']
    algorithm_kwargs = deepcopy(algorithm_params['kwargs'])
    algorithm = ALGORITHM_CLASSES[algorithm_type](
        variant, *args, **algorithm_kwargs, **kwargs)


    return algorithm
