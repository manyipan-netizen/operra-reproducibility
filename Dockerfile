FROM rocker/verse:4.5.0

RUN install2.r ggplot2 dplyr kableExtra && \
    apt-get update && apt-get install -y --no-install-recommends \
    openjdk-21-jre-headless \
    && apt-get clean && rm -rf /var/lib/apt/lists/* && \
    curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR=/usr/local bash

COPY requirements.txt .
RUN uv pip install --system --no-cache polars snakemake -r requirements.txt && \
    curl -s https://get.nextflow.io | bash && mv nextflow /usr/local/bin/

EXPOSE 8787
ENV USER=rstudio
CMD ["/init"]
