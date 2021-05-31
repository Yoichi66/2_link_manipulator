# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import math


# 逆運動学の計算
def ik(L, p2):
    x, y = p2
    l1, l2 = L
    l3 = math.sqrt((x * x) + (y * y))
    th2 = math.pi - math.acos(((l1 * l1) + (l2 * l2) - (l3 * l3)) / (2 * l1 * l2))
    th1 = math.atan2(y, x) - math.acos(((l1 * l1) + (l3 * l3) - (l2 * l2)) / (2 * l1 * l3))
    return [th1, th2]


# 順運動学の計算
def fk(L, th):
    # 各リンクの長さと関節角度の取得
    l1, l2 = L
    th1, th2 = th

    # リンク1の手先
    x1 = l1 * math.cos(th1)
    y1 = l1 * math.sin(th1)

    # リンク2の手先
    x2 = x1 + l2 * math.cos(th1 + th2)
    y2 = y1 + l2 * math.sin(th1 + th2)

    # 手先位置をNumPy配列に格納して返す
    return np.array([[0, 0], [x1, y1], [x2, y2]])


def main():
    # リンク1, 2の長さ
    L = [0.5, 0.5]
    p2 = [0.5, 0.5]
    # 第1, 2の関節角度
    # th = np.radians([90, 0])

    # 順運動学の計算
    th = ik(L, p2)
    p = fk(L, th)

    # グラフ描画位置の設定
    fig, ax = plt.subplots()
    plt.axis('equal')
    plt.subplots_adjust(left=0.1, bottom=0.15)
    plt.xlim([-1, 1])
    plt.ylim([-0.3, 1.3])
    # グラフ描画
    plt.grid()
    graph, = plt.plot(p.T[0], p.T[1])

    def update_th1(slider_val):
        # 関節1の角度を更新
        p2[0] = slider_val

        th = ik(L, p2)
        # 順運動学の計算
        p = fk(L, th)

        # 手先位置を更新
        graph.set_data(p.T[0], p.T[1])
        graph.set_linestyle('-')
        graph.set_linewidth(5)
        graph.set_marker('o')
        graph.set_markerfacecolor('g')
        graph.set_markeredgecolor('g')
        graph.set_markersize(15)

        # グラフの再描画
        fig.canvas.draw_idle()

    def update_th2(slider_val):
        # 関節2の角度を更新
        p2[1] = slider_val
        th = ik(L, p2)
        # 順運動学の計算
        p = fk(L, th)

        # 手先位置を更新
        graph.set_data(p.T[0], p.T[1])
        graph.set_linestyle('-')
        graph.set_linewidth(5)
        graph.set_marker('o')
        graph.set_markerfacecolor('g')
        graph.set_markeredgecolor('g')
        graph.set_markersize(15)

        # グラフの再描画
        fig.canvas.draw_idle()

    # スライダーの表示位置
    slider1_pos = plt.axes([0.1, 0.05, 0.8, 0.03])
    slider2_pos = plt.axes([0.1, 0.01, 0.8, 0.03])

    # Sliderオブジェクトのインスタンス作成
    threshold_slider1 = Slider(slider1_pos, 'x', -1, 1)
    threshold_slider2 = Slider(slider2_pos, 'y', -1, 1)

    # スライダーの値が変更された場合の処理を呼び出し
    threshold_slider1.on_changed(update_th1)
    threshold_slider2.on_changed(update_th2)
    graph.set_linestyle('-')
    graph.set_linewidth(5)
    graph.set_marker('o')
    graph.set_markerfacecolor('g')
    graph.set_markeredgecolor('g')
    graph.set_markersize(15)
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()