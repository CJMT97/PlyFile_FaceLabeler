# PlyFile_FaceLabeler
This is a simple program for adding scalar labels to the face element section of a .ply file. This can be done provided the vertices have already been labeled an the resulting labeling is done by majority of the vetices in each face.

# Running the program
To run the program use one of the following...

`python PlyLabeler.py input.ply`

This will store the output in the cwd with the name input_labeled.ply.

`python PlyLabeler.py input.ply output.ply`

This will store the output in the cwd with the name output.ply

