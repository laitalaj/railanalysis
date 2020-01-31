# railanalysis

Project for Network Analysis, spring 2020, University of Helsinki

## Getting started

1. Install [Anaconda](https://www.anaconda.com/)
2. Create the environment:
`conda env create -f environment.yml`
3. Activate the environment:
`conda activate railanalysis`
4. You might need to manually create the Jupyter notebook kernel.
Using Anaconda's python, do
`python -m ipykernel install --user --name railanalysis`
5. Run Jupyter (it should be included in the Anaconda distribution):
`jupyter notebook .`
6. Open the `DataLoading.ipynb` -notebook
7. Make sure to switch to your new kernel
8. Start analysing!

## License

All files except for the data are made available under GNU GPL v3.
The source of the data is Open Street Map, and as such falls under the Open Data Commons ODbL:

**The contents of the `data`-subdirectory are made available under the Open Database License: http://opendatacommons.org/licenses/odbl/1.0/.**
**Any rights in individual contents of the data are licensed under the Database Contents License: http://opendatacommons.org/licenses/dbcl/1.0/**