FROM jupyter/minimal-notebook:95f855f8e55f

ENV MAIN_PATH=/usr/local/bin/avanetix_qws
ENV LIBS_PATH=${MAIN_PATH}/libs
ENV CONFIG_PATH=${MAIN_PATH}/config
ENV NOTEBOOK_PATH=${MAIN_PATH}/notebooks

RUN pip install --upgrade pip && \ 
	pip install qiskit matplotlib pylatexenc pillow

RUN pip install dwave-ocean-sdk

RUN pip install jupyter --upgrade
RUN pip install jupyterlab --upgrade
RUN pip install ipywidgets

EXPOSE 8888

CMD cd ${MAIN_PATH} && sh config/run_jupyter.sh
