import os
import glob
import pickle
import gzip
import pdb
import numpy as np
def restore_pool(
        replay_pool,
        experiment_root,
        save_path=None,
        normalize_states=True,
        normalize_rewards=False,
        obs_mean=None,
        obs_std=None,
    ):
    if 'd4rl' in experiment_root:
        data = restore_pool_d4rl(replay_pool, experiment_root[5:])

    data, obs_mean, obs_std = normalise_data(
        data, normalize_states, normalize_rewards, experiment_root, obs_mean, obs_std
    )
    replay_pool.add_samples(data)

    print('[ mbpo/off_policy ] Replay pool has size: {}'.format(replay_pool.size))
    return obs_mean, obs_std

def restore_pool_d4rl(replay_pool, name):
    import gym
    import d4rl
    data = gym.make(name).get_dataset()

    data["observations"] = data["observations"][data["timeouts"] == False]
    data["actions"] = data["actions"][data["timeouts"] == False]
    data["rewards"] = data["rewards"][data["timeouts"] == False].reshape(-1, 1)
    data["next_observations"] = data["next_observations"][data["timeouts"] == False]
    data["terminals"] = data["terminals"][data["timeouts"] == False].reshape(-1, 1)
    
    return data

def normalise_data(data, normalize_states, normalize_rewards, dataset_name, obs_mean=None, obs_std=None):
    # obs_mean = None
    # obs_std = None
    if (not normalize_states) and (not normalize_rewards):
        return data, obs_mean, obs_std

    obs = data["observations"]
    next_obs = data["next_observations"]
    rewards = data["rewards"]

    # compute mean and std across subsample of data
    inds = np.floor(np.linspace(0, obs.shape[0]-1, num=10000)).astype(int)

    # subtract 1 from antmaze rewards per IQL paper
    if 'antmaze' in dataset_name:
        data['rewards'] -= 1

    if normalize_rewards:
        rew_std = np.std(rewards[inds, :], axis=0) + 1e-6
        data['rewards'] = rewards / rew_std

    if normalize_states:
        obs_mean = obs_mean if obs_mean is not None else np.mean(obs[inds, :], axis=0)
        obs_std = obs_std if obs_std is not None else np.std(obs[inds, :], axis=0) + 1e-6 # avoid division by zero
        obs_norm = (obs - obs_mean) / obs_std
        next_obs_norm = (next_obs - obs_mean) / obs_std

        data["observations"] = obs_norm
        data["next_observations"] = next_obs_norm

    return data, obs_mean, obs_std

def parse_stacked_trajectories(data, max_eps=None, skip_terminated=True, obs_mean=None, obs_std=None):
    obs_mean = 0. if obs_mean is None else obs_mean
    obs_std = 1. if obs_std is None else obs_std

    obs = data["observations"]
    act = data["actions"]
    rwd = data["rewards"]
    next_obs = data["next_observations"]
    terminated = data["terminals"]
    timeout = np.expand_dims(data['timeouts'], axis=1)

    eps_id = np.cumsum(terminated + timeout, axis=0).flatten()
    eps_id = np.insert(eps_id, 0, 0)[:-1] # offset by 1 step
    max_eps = eps_id.max() + 1 if max_eps is None else max_eps

    dataset = []
    for e in np.unique(eps_id):
        if terminated[eps_id == e].sum() > 0 and skip_terminated:
            continue

        dataset.append({
            "obs": (obs[eps_id == e] - obs_mean) / obs_std,
            "act": act[eps_id == e],
            "rwd": rwd[eps_id == e],
            "next_obs": (next_obs[eps_id == e] - obs_mean) / obs_std,
            "done": terminated[eps_id == e],
        })

        if len(dataset) >= max_eps:
            break
    return dataset

def sample_expert_segments(traj_dataset, num_samples, seg_len=200):
    # assume equal trajectory lengths
    max_len = traj_dataset[0]["obs"].shape[0]
    
    obs = []
    act = []
    done = []
    eps_id = np.random.randint(0, len(traj_dataset), num_samples)
    for i in eps_id:
        traj = traj_dataset[i]
        seg_start = np.random.randint(0, max_len - seg_len)
        obs.append(traj["obs"][seg_start:seg_start+seg_len])
        act.append(traj["act"][seg_start:seg_start+seg_len])
        done.append(traj["done"][seg_start:seg_start+seg_len])
    
    obs = np.stack(obs)
    act = np.stack(act)
    done = np.stack(done)
    return obs, act, done