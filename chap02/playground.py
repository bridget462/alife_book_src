#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
import numpy as np
from alifebook_lib.visualizers import MatrixVisualizer

# visualizerの初期化 (Appendix参照)
# MatrixVisualizer(width=600, height=600, value_range_ min=0, value_range_max=1)
visualizer = MatrixVisualizer()
sample_matrix = np.array([[col/20 for col in range(20)] for row in range(10)])

while visualizer:  # visualizerはウィンドウが閉じられるとFalseを返す
    visualizer.update(sample_matrix)
