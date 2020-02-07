#Docker File: Airbnb Price Predictor
#Authors: Group 313 - Suvarna Moharir, Jaekeun Lee, Chimaobi Amadi

#use rocker/tidyverse as the base image
FROM rocker/tidyverse
RUN apt-get update
RUN apt-get install r-base r-base-dev -y

#installing required R packages
RUN Rscript -e "install.packages('testthat')"

#installing the anaconda distribution of python
RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.js.map' -delete && \
    /opt/conda/bin/conda clean -afy && \
    /opt/conda/bin/conda update -n base -c defaults conda

#putting anaconda python in path
ENV PATH="/opt/conda/bin:${PATH}"

#installing chromium and unzipper    
RUN apt-get update && apt install -y chromium && apt-get install -y libnss3 && apt-get install unzip

#installing chromedriver
RUN wget -q "https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_linux64.zip" -O /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip -d /usr/bin/ \
    && rm /tmp/chromedriver.zip && chown root:root /usr/bin/chromedriver && chmod +x /usr/bin/chromedriver

#installing altair and selenium 
RUN conda install -y -c conda-forge altair && conda install -y vega_datasets && conda install -y selenium

 
#adding required python packages 

RUN conda install -y -c anaconda \ 
    docopt \
    requests && \
    conda install -y -c anaconda python && \
    conda install -y -c anaconda pandas && \
    conda install -y -c conda-forge/label/gcc7 xgboost && \
    conda install -y numpy && \
    conda install -y scikit-learn && \
    conda install -y altair 

RUN conda install -y -c conda-forge/label/gcc7 selenium && \
    conda install -y -c conda-forge python-chromedriver-binary && \
    conda install -y -c conda-forge matplotlib


CMD ["/bin/bash"]

