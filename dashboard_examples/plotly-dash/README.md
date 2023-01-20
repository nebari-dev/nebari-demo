The code for the example apps is found here: https://github.com/plotly/dash-sample-apps

In order to run the apps in each folder, you will need to go to a specific example and install the dependencies in requirements.txt.  For example,

```
    pip install -r requirements.txt
```

However, if you want to create a conda environment that can run a few interesting examples of our choosing, you can do the following:

1. Create conda environment using environment.yml file.
   
    ```
    conda env create -f environment.yml
    conda activate plotly-dashboard

    ```

2. There are 3 apps that will run with the packages installed from the environment.yml file.  These are dash-brain-viewer, dash-oil-and-gas, and dash-uber-rides-demo. To run one of them do the following:
   
   ```
   python run dash-oil-and-gas/app.py

   ```