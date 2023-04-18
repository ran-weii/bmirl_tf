from ..base import base_params
from copy import deepcopy

params = deepcopy(base_params)
params.update({
    'domain': 'hopper',
    'task': 'medium-expert-v2',
    'exp_name': 'hopper_medium_expert'
})
params['kwargs'].update({
    'pool_load_path': 'd4rl/hopper-medium-expert-v2',
    'expert_load_path': 'd4rl/hopper-expert-v2',
    'model_load_dir': 'logs/pretrained_models/hopper-medium-expert-v2/BNN_pretrain',
})
