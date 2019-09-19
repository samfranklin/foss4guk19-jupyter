# FOSS4G UK 2019 Geoprocessing with Jupyter Notebooks

## Workshop Overview

The Jupyter notebook is becoming the de-facto environment for data scientists using the so-called "pydata stack" (python packages of numpy, pandas, matplotlib, other). Now, there is increasing crossover between desktop GIS specialists and python developers, as python packages that manipulate geographic data mature. Notebooks are a powerful yet easy to use environment to write code with and allow you to interact with your data and share workflows easily.

The objectives of this short workshop are to provide GIS users with a hands-on introduction to (a) how to set up a jupyter notebook environment locally using Anaconda and install various required python packages (b) undertake some simple geo-processing tasks using a mixture of "geo" packages within the "pydata" ecosystem, e.g. rasterio, xarray and geopandas, (c) visualise processing outputs.

The workshop is aimed at GIS desktop users with "beginner-level" awareness of python but have not used Jupyter notebooks and want to learn more. If you're familar with python and notebooks, then still free feel to come along as you may pick up some tips on the way.

## Prerequisites for Participants - what you need to do beforehand

* Bring a laptop. Laptop spec? If it can run qgis, then you should be okay.
* A local copy of this repository. You can either git clone, or download the zip and extract to your local disc. Here is the URL:

https://github.com/samfranklin/foss4guk19-jupyter

 
## Introduction/Background

### Why this workshop?

* 18 months ago I took a job and worked with a number of data scientists (without gis applications background) who all used the `pydata` stack and not gis apps for geospatial data manipulation and processing.
* In the python data community jupyter notebooks were the go-to for data hacking, loading, manipulation and visualisation. 
* I saw a bit of a disconnect between the pydata community and the traditional GIS community. Even at FOSS4G UK, I hadn't seen any workshops, so decided to share some lessons learned. 

### Who is the Workshop For?

I want to cater someone with one or all of the following requirements: 

* Anaconda complete beginner, never installed, but wants to try it
* Jupyter Notebook complete beginner, never installed, but wants to try it
* Some awareness of python probably from GIS desktop appsm like QGIS or Esri's ArcPy
* Someone that wants to share repeatable spatial data processing workflows.
* Someone that wants to interactively develop a workflow without a labourious re-run of an entire workflow, like blind debugging
* Some that is curious!

If you're sitting here, and you don't fit that profile, `DO NOT PANIC` you can treat this as a fresher.

### There are a bunch of interactive tools similar to notebooks, why jupyter notebooks?

* There was a great talk earlier by Mila Frerichs in the technical track.
* It's true there's a couple of new jams, e.g. [ObservableHQ](https://observablehq.com/) and [JupyterLab](https://jupyter.org/try), however this is aimed at beginners, so the Jupyter Notebook is simple and therefore a good place to start. 

### Some background before we dive in
* What is `Anaconda`? - see the [docs](https://anaconda.org/about) - Anaconda is a data-science software platform, for 
* What is `conda` ? - see the [docs](https://conda.io/en/latest/) - Conda is an open source package management system and environment management system that runs on Windows, macOS and Linux.
* What is a jupyter notebook and how do I run it - let's have a look at an uber simple example using `/test-packages-notebook-overview.ipynb`

## How this workshop will run
* Primary aim is to get your environment set up. This is often a big hurdle to adoption.
* For the 'beginners' I will walk through the two notebooks (time dependant) cell by cell and describe what's happening.
* If you are more comfortable with python and notebooks and are curious about the geoprocessing examples, feel free to work through them at your own (quicker) pace, instructions are on the notebooks.
* If you wanna hack on your own notebooks after getting an idea, feel free to just crack on with that.

## How to build your Environment

We will use `Miniconda` together with a `requirements.yml` file that will provision all the packages with a virtual python environment.

* If you do not have either `Anaconda` or `miniconda` installed, then go and download `miniconda` from https://docs.conda.io/en/latest/miniconda.html.
* Select the Python 3.x option rather than the 2.x version to download and run the installer.


* For Windows users, here's a link to the [Win64 Installer](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe). Download this and run the exe installer

* For those on MacOS or Linux and are happy with terminal, try either:

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


## Backup Option for a Build environment fail.

In the event your environment doesn't build or the the conference WiFi isn't up to it, you can follow along to the workshop and view the jupyter notebooks via `nbviewer` using https://nbviewer.jupyter.org/github/samfranklin/foss4guk19-jupyter/tree/master/tutorials/, and select the notebooks with 'nbviewer'

