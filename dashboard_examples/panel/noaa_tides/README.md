# NOAA Tides and Currents data exploration (v6)

This notebook uses the NOAA tides and current data to create a custom data explorer.  
Its a loose reimagining of the [original viewer](https://tidesandcurrents.noaa.gov/).  
It is intended as a proof of concept and demonstration of capabilities in Panel and  
Holoviews.   
  
In this notebook you can see that we can interactively build our individual dashboard  
pages here in the notebook. Then, once we are happy with the results, we can move on  
to building a multi-page app by stringing together the individual dashboard pages.  
We by add the suffix of `.servable()` to the final Panel object we want as our  
final dashboard. Finally, this notebook can then be deployed via command line:  
`panel serve water_dashboard.ipynb`. Alternately, it can be served via CDSDashboards  
on a JupyterHub or Nebari server. A tutorial of deploying this notebooks on 
Nebari can be found [here]().
  

## Caveats
  
There are plenty of edge cases were data may not be available for a given  
gauge or data type. We knowingly bypass these with a try/except since this is intended  
for demonstration purposes only.   


## Environment

The conda environment relies on the [noaa-coops](https://github.com/GClunies/noaa_coops) 
package to interact the the [NOAA API](https://api.tidesandcurrents.noaa.gov/api/prod/).  

The conda environment can be built via:

```python
conda env create water_dashboard.yml
```
