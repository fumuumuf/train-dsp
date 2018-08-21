# 
# このソースコードは, 『Pythonで学ぶ実践画像・音声処理入門』のサイトからお借りしている.
# http://www.slp.k.hosei.ac.jp/~itou/book/2018/PythonMedia/index.html
#
# ## log ##
# audioplayをjupyter用に変更, もとの関数は`audiopaly_org`にメソッド名変更
# 

import numpy as np
import simpleaudio as sa
import IPython.display

def audioplay_org(y, fs):
    """
    オリジナルの audioplay
    :param y:
    :param fs:
    :return:
    """
    yout = np.iinfo(np.int16).max / np.max(np.abs(y)) * y
    yout = yout.astype(np.int16)
    play_obj = sa.play_buffer(yout, y.ndim, 2, fs)


def audioplay(y, fs):
    """
    jupyter用にaudioplayを変更
    :param y:
    :param fs:
    :return:
    """
    IPython.display.display(IPython.display.Audio(y, rate=fs))


import scipy.io.wavfile as sw


def wavread(wavefile):
    fs, y = sw.read(wavefile)
    if y.dtype == 'float32' or y.dtype == 'float64':
        max_y = 1
    elif y.dtype == 'uint8':
        y = y - 128
        max_y = 128
    elif y.dtype == 'int16':
        max_y = np.abs(np.iinfo(np.int16).min)
    else:
        max_y = np.abs(np.iinfo(np.int16).min)
    y = y / max_y
    y = y.astype(np.float32)
    return (y, fs)


def wavwrite(wavefile, data, fs):
    if data.dtype == 'float32' or data.dtype == 'float64':
        max_y = 1
    elif data.dtype == 'uint8':
        data = y - 128
        max_y = 128
    elif data.dtype == 'int16':
        max_y = np.abs(np.iinfo(np.int16).min)
    else:
        max_y = np.abs(np.iinfo(np.int16).min)
    data = np.int16(data / max_y * np.abs(np.iinfo(np.int16).min))
    sw.write(wavefile, fs, data)


import cv2



# def implay(frame,fps): # color video only
def implay_org(frame):  # color video only
    """
    オリジナルの implay 関数
    """
    #    f_rate = np.int(1000/fps)
    for k in np.arange(1, frame.shape[3]):
        cv2.imshow('frame', frame[:, :, :, k])
        cv2.waitKey(1)
    #        cv2.waitKey(f_rate)
def implay(frame, interval_sec=0.01):
    """
    jupyter用に変更した implay 関数
    """
    import time
    for k in np.arange(1, frame.shape[3]):
        plt.imshow(frame[:, :, :, k])
        IPython.display.display(plt.gcf())
        time.sleep(0.050)
        IPython.display.clear_output(wait=True)

import mpl_toolkits.mplot3d as mm
import matplotlib.pyplot as plt


# def stem3(z):
#     fig = plt.figure()
#     ax = mm.Axes3D(fig)
#     if z.ndim == 1:
#         Y = 1
#         X = z.shape[0]
#     else:
#         X, Y = z.shape
#     x, y = np.meshgrid(range(X), range(Y))
#     plt.contourf(x,y,z)
#     plt.show()

def stem3(z):
    fig = plt.figure()
    ax = mm.Axes3D(fig)
    if z.ndim == 1:
        Y = 1
        X = z.shape[0]
    else:
        X, Y = z.shape
    for x in range(X):
        for y in range(Y):
            if Y == 1:
                ax.plot([x, x], [y, y], [0, z[x]], 'b-')
                ax.scatter(x, y, z[x], 'o', color='b')
            else:
                ax.plot([x, x], [y, y], [0, z[x, y]], 'b-')
                ax.scatter(x, y, z[x, y], 'o', color='b')
    plt.show()


import plotly.offline as po
import plotly.graph_objs as go


def mesh(z):
    data = [go.Surface(z=z)]
    fig = go.Figure(data=data)
    po.plot(fig)
