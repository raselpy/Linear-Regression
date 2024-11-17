# Linear Regression Implementation (Basic)

This repository contains a basic implementation of the initialization of a linear regression model using Python and NumPy. The code prepares the feature matrix for linear regression by adding a bias term (intercept) but does not yet implement the actual learning process (gradient descent).

## Features

- Simple `LinearRegression` class with:
  - `eta`: Learning rate (default 0.1)
  - `n_iter`: Number of iterations (default 50)
- `fit()` method adds a column of ones to the input matrix `X` to account for the bias term.

## Code Overview

The main components of the code include:

1. **Initialization**:
   The `LinearRegression` class is initialized with a learning rate (`eta`) and the number of iterations (`n_iter`).

2. **Fitting**:
   The `fit()` method modifies the feature matrix `X` by adding a column of ones to account for the bias term.



