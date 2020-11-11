"""
数据生成的主要逻辑
"""


import numpy as np


def generate_matrix(
    board_grid: int, unit_grid: int, unit_n: int, positions: list
):
    """生成指定布局矩阵

    Args:
        board_grid (int): 布局板分辨率，代表矩形区域的边长像素数
        unit_grid (int): 矩形组件分辨率
        unit_n (int): 组件数
        positions (list): 每个元素代表每个组件的位置
    Returns:
        np.ndarray: 布局矩阵
    """
    # TODO: 实现布局矩阵的生成
    length = int(board_grid / unit_grid)
    size = length ** 2
    img = np.ones(size)
    for item in positions:
        img[item - 1] = 0
    img = img.reshape(unit_grid, -1)
    return img
