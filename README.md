# Rhode Island Wave
A mathematically hot-swappable audit station designed for conducting RLA's in 
Rhode Island.

# Execution Directions
This project is built using **Python 3**. 

If you already have pip installed (Just try running `pip` from the command line), simply 
run `pip install -r requirements.txt`. 

If not, then you will have to install `pip`. You can either just install `pip` by itself,
but we recommend installing `anaconda`, which will sandbox your python installation so that
it won't interfere with anything else on your system. 

Install `anaconda` for your respective operating system by [following this](https://conda.io/docs/user-guide/install/index.html#regular-installation). Once `conda` is installed, create a new conda environment that
 uses `python 3` and `pyqt 5`. For most systems, this is done by `conda create --name
 riwave python=3 pyqt=5`

After the environment has been properly set up, run `source activate riwave` to activate
the environment. You should see a `(riwave)` on the very left of your prompt.

Whether or not you installed `anaconda` or just `pip` by itself, run `python __main__.py` 
in the `WAVE` folder to begin the audit station.
