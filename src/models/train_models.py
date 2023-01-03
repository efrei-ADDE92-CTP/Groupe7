{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# import load_iris_dataset\n",
    "import sys\n",
    "sys.path.append('../data')\n",
    "import make_dataset\n",
    "\n",
    "df = make_dataset.load_iris_dataset()\n",
    "df.head()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.9.12 ('base')",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.9.12"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "5c6a328c3dae7a0c12012862982ee9605db1881d32a9f60b075ff1e1dc4cc909"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
