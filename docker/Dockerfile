# どのイメージを基にするか
FROM continuumio/anaconda3:5.2.0

RUN apt-get install -y gcc libasound2-dev bzip2 git unzip vim libgl1-mesa-dev pulseaudio

RUN conda install -y opencv plotly && \
 pip install  simpleaudio autopep8

RUN conda install -c conda-forge -y jupyterlab jupyter_contrib_nbextensions

# jupyter設定
RUN mkdir -p /root/.jupyter && \
    echo "c.NotebookApp.token = ''" > /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.open_browser = False" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.notebook_dir = '/root/'" >> /root/.jupyter/jupyter_notebook_config.py 

# vim key bind
# Create required directory in case (optional)
RUN mkdir -p $(jupyter --data-dir)/nbextensions && \
    cd $(jupyter --data-dir)/nbextensions && \
    git clone https://github.com/lambdalisue/jupyter-vim-binding vim_binding 


ENV PYTHONPATH=/root/lib:$PYTHONPATH

EXPOSE 8888
CMD /bin/bash -c 'jupyter notebook --ip="*" --port=8888 --allow-root'
