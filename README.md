# PCA
This is boilerplate code to create a publication quality figure using principle component analysis.  It is an R script and has the dependency **ggbiplot**, which you can install in R, using the command `install.packages('ggbiplot')`.

## Quick start
```sh
Rscript pca.R
```

## Input data    
For the example the input file is in the form of tab seperate columns, where the columns A-Z represent amino acid counts.

## Output
If **PCA** ran correctly you should get an output image titled figure.tiff.  If you use the test data, the figure will
look like the image below:
___
<p align="center">
    <img src="figure.png">
</p>
