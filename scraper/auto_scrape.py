import os
import subprocess

SPIDERS_DIR=os.path.join(os.path.dirname(__file__), "markets", "spiders")

spiders=[
    f.replace(".py","") for f in os.listdir(SPIDERS_DIR)
    if f.endswith(".py") and f !="__init__.py"
]

if not spiders:
    print("No spiders available")
    exit(1)

for spider_name in spiders:
    print(f"Running spider: {spider_name}")
    try:
        subprocess.run(["scrapy","crawl",spider_name],check=True,cwd=os.path.dirname(__file__))
        print(f"finished {spider_name}")
    except subprocess.CalledProcessError:
        print(f"!!! Error while running {spider_name} !!!")
