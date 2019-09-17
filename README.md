# FOSS4G UK 2019 Geoprocessing with Jupyter Notebooks

This repo will be updated closer to the FOSS4G UK workshop that is scheduled on Thursday 19th September 2019.

This repo is being updated, please download a fresh copy ahead of the workshop.

## Workshop Overview

The Jupyter notebook is becoming the de-facto environment for data scientists using the so-called "pydata stack" (python packages of numpy, pandas, matplotlib, other). Now, there is increasing crossover between desktop GIS specialists and python developers, as python packages that manipulate geographic data mature. Notebooks are a powerful yet easy to use environment to write code with and allow you to interact with your data and share workflows easily.

The objectives of this short workshop are to provide GIS users with a hands-on introduction to (a) how to set up a jupyter notebook environment locally using Anaconda and install various required python packages (b) undertake some simple geo-processing tasks using a mixture of "geo" packages within the "pydata" ecosystem, e.g. rasterio, xarray and geopandas, (c) visualise processing outputs.

The workshop is aimed at GIS desktop users with "beginner-level" awareness of python but have not used Jupyter notebooks and want to learn more. If you're familar with python and notebooks, then still free feel to come along as you may pick up some tips on the way.

## Prerequisites for Participants - what you need to do beforehand

* Bring a laptop. Laptop spec? If it can run qgis, then you should be okay.
* A local copy of this repository. You can either git clone, or download the zip and extract to your local disc.
* Attempt to build your environment, following the steps in the next section. If this isn't successful, we will briefly run through this at the beginning of the workshop too.

## How to build your Environment

We will use `Miniconda` together with a `requirements.yml` file that will provision all the packages with a virtual environment.

* If you do not have either `Anaconda` or `miniconda` installed, then go and download `miniconda` from https://docs.conda.io/en/latest/miniconda.html.
* Select the Python 3.x option rather than the 2.x version to download and run the installer.

* For Windows users, here's a link to the [Win64 Installer](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe). Download this and run the exe installer

* For those on MacOS and are happy with terminal, try either:

```bash
# get the latest MacOS 64-bit installer
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
bash Miniconda3-latest-MacOSX-x86_64.sh
```

```bash
# get the latest linux 64-bit installer
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-MacOSX-x86_64.sh
```

Download a copy of this repository, either downloading of the zip or via git, with:

```bash
git clone git@github.com:samfranklin/foss4guk19-jupyter.git
```

Open your terminal and change directory into this repository.

```bash
cd foss4guk19-jupyter
```

Check your terminal can use the conda program with

```bash
conda --version
```

Create the conda environment using the environment yaml file, this can take between 5 - 10 minutes:

```bash
conda env create --file requirements.yml
```

Activate the environment

```bash
conda activate jgpenv
```

Launch a Jupyter Notebook

```bash
jupyter notebook
```

You are ready to go!
