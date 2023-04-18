from ..base import base_params
from copy import deepcopy

params = deepcopy(base_params)
params.update({
    'domain': 'hopper',
    'task': 'medium-replay-v2',
    'exp_name': 'hopper_medium_replay'
})
params['kwargs'].update({
    'pool_load_path': 'd4rl/hopper-medium-replay-v2',
    'expert_load_path': 'd4rl/hopper-expert-v2',
    'model_load_dir': 'logs/pretrained_models/hopper-medium-replay-v2/BNN_pretrain',
})
