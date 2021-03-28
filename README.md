###How to install
Make sure you have **Anaconda**, create a virtual env with Python 3
```buildoutcfg
conda create -n sneaker-crawler-env-python3 python=3
```

Install `scrapy`  in the virtual env
```buildoutcfg
conda activate sneaker-crawler-env-python3
pip install Scrapy
```

There's a built-in `RUN` script that executes
```buildoutcfg
scrapy runspider theiconic_spider.py -o theiconic.jl
```
Essentially, it calls the simple `theiconic_spider.py` that we defined for crawling data from [The Iconic](https://www.theiconic.com.au/) and dumps the parsed data in json into `theiconic.jl`

Happy hacking!  
