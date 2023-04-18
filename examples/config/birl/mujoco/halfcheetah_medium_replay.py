from ..base import base_params
from copy import deepcopy

params = deepcopy(base_params)
params.update({
    'domain': 'halfcheetah',
    'task': 'medium-replay-v2',
    'exp_name': 'halfcheetah_medium_replay'
})
params['kwargs'].update({
    'pool_load_path': 'd4rl/halfcheetah-medium-replay-v2',
    'expert_load_path': 'd4rl/halfcheetah-expert-v2',
    'model_load_dir': 'logs/pretrained_models/halfcheetah-medium-replay-v2/BNN_pretrain',
    'rollout_batch_size': 50000,
    'rollout_length': 5,
    'adv_rollout_length': 5,
})
