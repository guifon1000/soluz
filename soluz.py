import sys
import sys
sys.path.append('../triangleLib')
sys.path.append('../openfoam_utils')
import mesh
import readMSH
import pygmsh as pg
import subprocess
import meshio


name = 'soluz'
exe_gmsh = '/home/fon/gmsh-2.16.0-Linux/bin/gmsh'
geom = mesh.echanger(name)
#geom = mesh.simple_square(name)
subprocess.call([exe_gmsh,name+'.geo','-2','-o',name+'.msh','>',name+'.mshlog'])
d = readMSH.read_msh_file(name)
readMSH.write_fms_file(name,**d)
#points,cells,pt_data, cell_data, field_data = pg.generate_mesh(geom)
#meshio.write(name+'.vtu', points, cells)# ells['quad'])    #{'mu':mu}
