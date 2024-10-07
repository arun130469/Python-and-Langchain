
# Setting Up and Using Jupyter Notebooks in GitHub Codespace

This guide provides step-by-step instructions for setting up and using Jupyter notebooks within a GitHub Codespace.

## 1. Create or Login to github account
 - If you don’t have a GitHub account, create one or log in to your existing account.

## 2. Fork repository
 - Fork the repository we provided. This will create a copy under your GitHub repositories.

## 3. Open Your Codespace

- Open the repository, click the 'Code' button, and select the 'Codespaces' tab.
- click on codespace section and create codespace.

## 4. Install Jupyter Notebook

If Jupyter is not already installed in your Codespace, you'll need to install it:

```bash
pip install notebook
```

## 5. Create a New Jupyter Notebook
To create a new Jupyter notebook:
1. Open the command palette in CodeSpace by pressing `Ctrl + Shift + P` (or `Cmd + Shift + P` on macOS).
2. Type `Jupyter: Create New Blank Notebook` and select it from the options.
3. Choose the kernel you want to use for the notebook (e.g., Python).
4. A new notebook will open, and you can start adding code cells.

## 6. Use an Existing Notebook

If you already have a `.ipynb` file in your repository:

- Open the file directly from the file explorer in Code by clicking on it.
- The notebook will open in the notebook editor, and you can start working with it.

## 7. Run the Jupyter Notebook

- To run cells within the notebook, click the "Run" button next to each cell or use the `Shift + Enter` shortcut to run the current cell and move to the next one.
- First time you will need to select kernal, your codespace might not have Kernal and the shortcut was to do that is adding follwing jupyter extension.
```
Name: Jupyter
Id: ms-toolsai.jupyter
Description: Jupyter notebook support, interactive programming and computing that supports Intellisense, debugging and more.
Version: 2024.7.0
Publisher: Microsoft
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter
```

## 8. Save and Commit Your Work

- Save your notebook regularly by pressing `Ctrl + S` (or `Cmd + S` on macOS).
- To commit your changes to GitHub, use the standard Git commands in the terminal or the Source Control panel in Codespace.


This setup allows you to work seamlessly with Jupyter notebooks within your Codespace environment.
