Example Conformal Maps app to demonstrate Voila

This code is found here: https://github.com/zolabar/Conformal-Maps

It is added as a submodule to this repo.  The easiest way to run it is to do the following.

1. Initiate the submodule:
    ```
    git submodule init
    git submodule update
    ```

2. Create conda environment. 
   
    ```
    conda env create -f environment.yml
    conda activate voila-dashboard

    ```

3. Run the app.
   ```
   cd Conformal-Maps
   voila example_voila.ipynb

   ```

## Deploy app on CDS Dashboards

To deploy on Nebari with CDS Dashboards:

1. Choose nebari-git-dashboard environment.
2. Point to  "dashboard_examples/voila/Conformal-Maps/example_voila.ipynb" in your jupyter tree.  
3. Choose "voia" as your framework.
