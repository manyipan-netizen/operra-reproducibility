# SwissRN Workshop on Computational Reproducibility

Part of the OPeR-RA project.

The website for this workshop is: 

## Citation

Cite this workshop as: <https://crsuzh.pages.uzh.ch/operra-reproducibility>

A BibTeX entry is given by:

## Development in Docker

TBC: 

Build Docker image:

```{bash}
docker build -t pyverse .
```

Run container as live dev session:

```{bash}
docker run --rm -d -p 8787:8787 -e PASSWORD=rstudio \
  -v "$(pwd)":/home/rstudio/project pyverse
```

Or, using Docker Compose:

```{bash}
docker compose up -d
```

Open RStudio Server at [http://localhost:8787/](http://localhost:8787/).
