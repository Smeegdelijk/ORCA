READ_ME is out of date, ORCA is currently being updated :D

# ORCA
Python scripts that predict and plot the location of the origin of replication (*oriC*) of circular bacterial genomes based on Z-curve, GC-skew, *dnaA*-box, and gene location analyses. This README will not explain all of ORCA's methods, those can be read in `ORCA.pdf`. All functions, main or helper, are labelled with docs-strings and type-hinting for ease-of-use. Most functions in ORCA can be used seperately as well. For example, `calc_disparities` in `ORCA.py` can be used outside of ORCA, too. As well as all functions for fetching files from NCBI, or plotter functions, etc.

Please, see their provided docs-strings for more info. ORCA was previously available here: https://github.com/Mister-Teapot/OriC_Finder. This repository still contains all datasets and scripts used for the analyses.

## `ORCA.py`
This script predicts the origin of replication for circular bacterial DNA. It makes use of a combination of [Z-curve](https://en.wikipedia.org/wiki/Z_curve) and [GC-skew](https://en.wikipedia.org/wiki/GC_skew) analysis. You can load the required FASTA files yourself, or simply provide an accession and NCBI-account email and the `find_oriCs` function will fetch them. The docs-string of the function shows more information on what is needed to use ORCA.

Please, make sure to load the proper file formats into the function, otherwise ORCA will not work. A lot of invalid parameters will throw warnings or errors, but it is not improbable that a few were missed.

**Example use of ORCA**
```
>>> import joblib, ORCA
>>> email = 'example@email.com'
>>> model = joblib.load('Machine_Learning/75_train_model.pkl')
>>> properties = ORCA.find_oriCs(accession='NC_000962', email=email, api_key=None, model=model)
>>> for key in ['accession', 'oriC_middles', 'predictions', 'gc_conc', 'seq_len']:
...     print(key, properties[key])
accession NC_000962.3
oriC_middles [4411229, 3903606]
Predictions [1.0078976155574155, -1.0150783114803241]
gc_conc 0.6561466628826449
seq_len 4411532
```

**NOTE**: *oriC*s are NOT sorted, do not assume the first *oriC* in the list is the *oriC* with the best score.
```
>>> oriC_dict = find_oriCs(accession='NC_000913', email='example@email.com')
>>> oriC = oriC_dict['oriCs'][0]
>>> print(oriC.z_score)
1.0
```

**Libraries and Versions used:**
- [Python 3.9.13 - 3.10.5](https://www.python.org/)
  - [SciPy 1.8.1](https://scipy.org/)
  - [Pandas 1.4.3](https://pandas.pydata.org/)
  - [NumPy 1.23.0](https://numpy.org/)
  - [Biopython 1.79](https://biopython.org/)
  - [Scikit-learn 1.1.1](https://scikit-learn.org/)
  - [Matplotlib 3.5.2](https://matplotlib.org/)

### `peak.py`
This script contains the `Peak`-class. This class is used in handling potential *oriC*s. The `'oriCs'` key in the properties dictionary that is returned by `find_oriCs` consists of a list of `Peak` objects. Each `Peak` represents a potential *oriC* and has attributes for its Z-, G-, and D-score as well as the confidence a potential machine learing model has.

### `helper_functions.py`
Script with a lot of useful functions used to make ORCA work. Not all are used anymore, but might be of use to others. All functions are provided with docs-string.



### `plotter_functions.py`
There are 3 general functions in this file which can be used to plot any generic 1D-np.array. To use these functions, make sure to have [matplotlib](https://matplotlib.org/) installed
- `plot_Z_curve_3D`: Makes a 3D-plot of the Z-curve.
- `plot_Z_curve_2D`: Can plot a maximum of four curves in a single 2D-plot. This one is useful for plotting single or multiple Z-curve or GC-skew components agaist each other.
- `plot_GC_skew`: Does the same as `plot_Z_curve_2D`, except only takes one array.
### Machine_learning
This folder contains two SVCs saved as pickle files. They can easily be loaded with the `joblib` from the standard Python library.
- `75_train_model.pkl`: SVC trained on 75 % of the DoriC dataset
- `exp_train_model.pkl`: SVC trained on all but the experimentally verified data.
- `train_save_model.py`: Script for training the SVC.
- `tuning.py`: Script for tuning the hyperparameters of the chosen model.
- `tuning.csv`: CSV file of all potential *oriC*s ORCA has found on the DoriC dataset with True-False labels for whether they are True *oriC*s. This file was used for training the SVCs.

### DoriC_processing
The DoriC data can be downloaded from http://tubic.tju.edu.cn/doric/public/index.php as a .RAR. Unpack this however you want and you'll be left with a CSV-file.
- `data_prep_doric.py`: Processes DoriC CSV into something more usable.
- `download_files.py`: This script was used to download the necessary FASTA-files for ORCA to use when predicting all accessions in DoriC.
