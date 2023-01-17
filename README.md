
# COMPAS introduction

[📃 COMPAS documentation](https://compas.dev/compas/latest) | 
[🎦 Slides](https://docs.google.com/presentation/d/1O7gikm_zixRJgeckK2vlUnkcBZXqPbUmIM2Bj3-Do9k/edit?usp=sharing)

## Installation

> **NOTE**: If you're on Windows, all commands below have to be executed in the *Anaconda Prompt* (NOT the *Command Prompt*)

We use `conda` to make sure we have clean, isolated environment for dependencies.

<details><summary>First time using <code>conda</code>?</summary>
<p>

Make sure you run this at least once:

    (base) conda config --add channels conda-forge

</p>
</details>


    (base) conda env create -f https://dfab.link/intro.yml

### Add to Rhino

    (base)  conda activate intro
    (intro) python -m compas_rhino.install

### Get the workshop files

Clone the repository:

    (intro) cd Documents
    (intro) git clone https://github.com/gramaziokohler/compas_introduction.git

### Verify installation

    (intro) python -m compas

    Yay! COMPAS is installed correctly!

    COMPAS: 1.17.4
    Python: 3.9.13 (CPython)
    Extensions: ['compas-occ', 'compas-rrc', 'compas-view2', 'compas-cgal', 'compas-fab']

### Update installation

To update your environment:

    (intro) conda env update -f https://dfab.link/intro.yml


