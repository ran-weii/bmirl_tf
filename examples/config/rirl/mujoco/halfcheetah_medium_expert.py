from ..base import base_params
from copy import deepcopy

params = deepcopy(base_params)
params.update({
    'domain': 'halfcheetah',
    'task': 'medium-expert-v2',
    'exp_name': 'halfcheetah_medium_expert'
})
params['kwargs'].update({
    'pool_load_path': 'd4rl/halfcheetah-medium-expert-v2',
    'expert_load_path': 'd4rl/halfcheetah-expert-v2',
    'rollout_length': 5,
    'adversary_loss_weighting': 0.0768,
    'model_load_dir': 'logs/pretrained_models/halfcheetah-medium-expert-v2/BNN_pretrain',
})
