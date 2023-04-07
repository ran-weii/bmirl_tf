import os
import io
import datetime
import numpy as np
import pandas as pd
import cv2
import pdb
import matplotlib
matplotlib.use('Agg')
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from softlearning.misc.utils import _make_dir

class Writer():

    def __init__(self, log_dir, log_wandb, wandb_project="", wandb_group="", config=None):
        self.log_dir = log_dir
        self._data = {}
        self._data_3d = {}
        
        _make_dir(log_dir)
        self.csv_dir = os.path.join(log_dir, f"history.csv")
        self.history = []
        print('[ Writer ] Log dir: {}'.format(log_dir))

    def __getitem__(self, key):
        if key in self._data:
            return self._data[key]
        else:
            return self._data_3d[key]

    def __getattr__(self, attr):
        return getattr(self._writer, attr)

    def _add_label(self, data, label):
        if label not in data:
            data[label] = 0

    def add_scalar(self, label, val, epoch):
        self._add_label(self._data, label)
        if epoch > self._data[label]:
            self._data[label] = epoch

    def add_dict(self, dictionary, epoch):
        self.history.append(dictionary.copy())
        pd.DataFrame(self.history).to_csv(self.csv_dir, index=False)

    def plot_cdfs(self, label, epoch, env_mean, model_mean, env_paths, model_paths):
        plt.clf()
        plt.plot(env_mean, linewidth=2, label='env', c='k')
        plt.plot(model_mean, linewidth=2, label='model', c='b')

        for path in env_paths:
            plt.plot(path['rewards'].cumsum(), alpha=0.5, c='k')
        for path in model_paths:
            plt.plot(path['rewards'].cumsum(), alpha=0.5, c='b')

        plt.ylabel('cumulative return')
        plt.xlabel('step')
        plt.legend()
        self._savefig(label, epoch)

    def _savefig(self, label, epoch):
        buf = io.BytesIO()
        plt.savefig(buf, format='png', layout = 'tight')
        buf.seek(0)
        img = cv2.imdecode(np.fromstring(buf.getvalue(), dtype=np.uint8), -1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = img.transpose(2,0,1) / 255.
        self._writer.add_image(label, img, epoch)
        return img
