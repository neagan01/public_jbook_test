#!/usr/bin/env python
# coding: utf-8

# # Appendix Z: Creating your own Jupyter Book textbook
# 
# Here the procedure used to develop this textbook (created 2022-2023) is described. This was created on a Windows 10 machine. This is by no means the best way to do this, it is simply the way it was done here.
# 
# 1. Install Anaconda from https://www.anaconda.com/
# 2. Create new Python 3.7 environment was created in Anaconda by going to the Environments tab and selecting "create". Call it "py37". This may help with Windows compatibility issues.
# 3. Run Anaconda Prompt (found in Programs/Anaconda3 (64-bit)/)
# 4. Load environment with "activate py37"
# 5. Install jupyter books with the command "conda install -c conda-forge jupyter-book". It may take a bit to successfully install.
# 6. Navigate to the folder where you will create your book.
# 7. Create a template book with "jupyter-book create bookname"
# 8. Build the book with command "jupyter-book build bookname"
# 9. With an appropriate editor (e.g., Notebook++), modify your title and other details in the "_config.yml" file.
# 10. Move your book contents into the "bookname" folder.
# 11. Define the organization of your book by editing the "_toc.yml" file
# 12. Open book by navigating to "bookname/_build/html" and opening an html file to jump to that chapter of the book.

# ## Additional resources for building Jupyter notebooks and textbooks for chemical engineering courses
# 
# 1. Jupyter book current documentation: https://jupyterbook.org/en/stable/intro.html
# 2. Dominguez et al., 2021, Teaching chemical engineering using Jupyter notebook: Problem generators and lecturing tools. https://doi.org/10.1016/j.ece.2021.06.004
# 

# In[ ]:




