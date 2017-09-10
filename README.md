# FakeNewsClassifier

uses Scrapy 1.4 With Python 3.

For Python 3 and anaconda, use
docker run -i -t -p 8888:8888 continuumio/anaconda3 /bin/bash -c "/opt/conda/bin/conda install jupyter -y --quiet && mkdir /opt/notebooks && /opt/conda/bin/jupyter notebook --notebook-dir=/opt/notebooks --ip='*' --port=8888 --no-browser --allow-root"

To log into a shell, use 
docker exec -it <name> /bin/bash
Followed by commands :-
1. conda install -y -c  conda-forge scrapy
2. pip install newspaper3k
3. cd /opt/notebooks
4. scrapy startproject news
