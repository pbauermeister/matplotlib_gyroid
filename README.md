# Gyroid 3D plot, using Python and Mathplotlib

I found a [code snippet](https://forum.freecadweb.org/viewtopic.php?t=19819#p233282) drawing a Gyroid (in Mathplotlib)
and generating an STL file:

![Screenshot](Screenshot.png "Gyroid plot in Mathplotlib")

After minimal restructuring, this is a basis project to plot any surface defined by an equation of type `f(x, y, z) = 0`.

## How to install
Example with Debian-based distros:
```
sudo apt install python3 python3-wheel python3-pip
pip3 install numpy scikit-image  numpy-stl
```

## How to run
```
./gyroid.py
```
