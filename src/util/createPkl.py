import pickle
import numpy as np
import os


youhi_label = ['brutal_scene', 'game', 'smoke', 'erotic']

target = '/content/drive/My Drive/youhi_label.pkl'
with open(target, 'wb') as f:
  pickle.dump(youhi_label, f)

target ='./youhi_label.pkl'
if os.path.getsize(target) > 0:
  with open(target,'rb') as f:
    new_pkl = pickle.load(f)

print(new_pkl)

f.close()