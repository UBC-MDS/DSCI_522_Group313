FROM rocker/tidyverse

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

# put anaconda python in path
ENV PATH="/opt/conda/bin:${PATH}"
   
RUN apt-get update

RUN apt-get install r-base r-base-dev -y

RUN Rscript -e "install.packages('testthat')"

#installing docopt python package
RUN conda install -y -c anaconda \ 
    docopt && \
    python
    
RUN conda install scikit-learn
RUN conda install -y -c anaconda python
RUN conda install -y -c pandas 
Run conda install -y -c yconda-forge xgboost  
RUN conda install -y -c conda-forge altair
RUN conda install -c conda-forge selenium