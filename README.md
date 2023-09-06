# A Bayesian Approach to Robust Inverse Reinforcement Learning
Code to reproduce the experiments for [A Bayesian Approach to Robust Inverse Reinforcement Learning](https://openreview.net/forum?id=W5SrUCN0yUa).

Our implementation builds upon the code for [RAMBO](https://github.com/marc-rigter/rambo).

## Installation
1. Install [MuJoCo 2.1.0](https://github.com/deepmind/mujoco/releases) to `~/.mujoco/mujoco210`.
2. Create a conda environment and install the code base as `rambo`.
```
cd rambo
conda env create -f environment/rambo_env.yml
conda activate rambo
pip install -e .
```

## Usage
Configuration files can be found in `examples/config/`. Our algorithms proposed in the paper are labeled as: BM-IRL=birl, RM-IRL=rirl. For example, to run BM-IRL on the halfcheetah-medium-expert task from the D4RL benchmark, use the following:

```
rambo run_example examples.development --config examples.config.birl.mujoco.halcheetach_medium_expert --seed 0 --gpus 1
```

Alternatively, edit the `.sh` file and run:

```
sh run_example.sh
```

## Logging
All logs are saved as `.csv` files in `./logs`.

## Note
This code base uses tensorflow 1.14, which can be hard to install for new users. 

Paralle to this code base, we have also developed a [Pytorch implementation](https://github.com/rw422scarlet/btom_irl) which is more readable but has not been benchmarked.

## Citation
```
@inproceedings{wei2023bayesian,
  title={A Bayesian Approach to Robust Inverse Reinforcement Learning},
  author={Wei, Ran and Zeng, Siliang and Li, Chenliang and Garcia, Alfredo and McDonald, Anthony and Hong, Mingyi},
  booktitle={Conference on Robot Learning},
  year={2023},
  organization={PMLR}
}
```
