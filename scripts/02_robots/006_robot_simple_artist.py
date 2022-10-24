import os
from compas.artists import Artist
from compas.robots import RobotModel
from compas.robots import LocalPackageMeshLoader

urdf_folder = os.path.join(os.path.dirname(__file__), "../../data/robots")
urdf_file = os.path.join(urdf_folder, "ur10e.urdf")

model = RobotModel.from_urdf_file(urdf_file)
model.load_geometry(LocalPackageMeshLoader(urdf_folder, "ur_description"))

artist = Artist(model, layer="Robot")
artist.clear_layer()
artist.draw_visual()
artist.redraw()
