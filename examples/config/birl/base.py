base_params = {
    'type': 'BIRL',
    'universe': 'gym',

    'kwargs': {
        'log_dir': './logs/birl',
        'log_wandb': False,

        'epoch_length': 1000,
        'n_epochs': 500,
        'train_every_n_steps': 1,
        'n_train_repeat': 1,
        'eval_render_mode': None,
        'evaluate_interval': 1,
        'eval_n_episodes': 10,
        'eval_deterministic': True,
        'separate_mean_var': True,
        
        # sac args
        'discount': 0.99,
        'tau': 5e-3,
        'alpha': 1.,
        'min_alpha': 0.1,
        'auto_alpha': True,
        
        # reward args
        'num_expert_traj': 10,
        'rwd_done_flag': True,
        'reward_scale': 1.0,
        'rwd_clip_max': 10.,
        'rwd_rollout_batch_size': 1000,
        'rwd_rollout_length': 40,
        'rwd_update_method': 'traj', # traj or marginal
        'rwd_update_steps': 1,
        'grad_penalty': 0.,
        'l2_penalty': 0.001,

        # dynamics args
        'adversary_loss_weighting': 0.01,
        'adv_update_steps': 50,
        'adv_rollout_length': 10,

        # 'num_expert_traj': 100,
        # 'rwd_done_flag': True,
        # 'reward_scale': 1.0,
        # 'rwd_clip_max': 40.,
        # 'rwd_rollout_batch_size': 1000,
        # 'rwd_update_steps': 40,
        # 'rwd_rollout_length': 40,
        # 'rwd_update_method': 'marginal', # traj or marginal
        # 'grad_penalty': 4,

        # 'adversary_loss_weighting': 0.0768,
        # 'adv_update_steps': 40,
        # 'adv_rollout_length': 10,
    
        # training args
        'critic_lr': 3e-4,
        'actor_lr': 3e-4,
        'adv_lr': 1e-4,
        'rwd_lr': 1e-4,
        'real_ratio': 0.5,
        'train_adversarial': True,
        'model_rollout_freq': 250,
        'model_retain_epochs': 5,
        'rollout_batch_size': 10000,
        'rollout_length': 40,
        'deterministic': False,
        'num_networks': 7,
        'num_elites': 5,

        # pretrain args
        'max_model_t': None,
        'pretrain_bc': False,
        'dynamics_pretrain_epochs': 1,
        # enter None or model path without extension: /Users/hfml/Documents/Ran/rambo/logs/hopper-medium-expert-v2/models
        'model_load_dir': None,
        # enter None or checkpoint path up to task name: /Users/hfml/Documents/Ran/rambo/logs/hopper-medium-expert-v2
        'checkpoint_load_dir': None,
    }
}
