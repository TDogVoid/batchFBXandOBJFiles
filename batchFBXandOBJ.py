import bpy
import os

# get the current path and make a new folder for the exported meshes
fbxPath = bpy.path.abspath('//FBX/')
objPath = bpy.path.abspath('//OBJ/')

if not os.path.exists(fbxPath):
    os.makedirs(fbxPath)

if not os.path.exists(objPath):
    os.makedirs(objPath)

for object in bpy.context.selected_objects:

    # deselect all meshes
    bpy.ops.object.select_all(action='DESELECT')

    # select the object
    object.select = True

    # export object with its name as file name
    fPath = str((fbxPath + object.name + '.fbx'))
    oPath = str((objPath + object.name + '.obj'))

    # export FBX
    bpy.ops.export_scene.fbx(filepath=fPath,
                            check_existing=True, 
                            filter_glob="*.fbx", 
                            use_selection=True,  
                            axis_forward='-Z', 
                            axis_up='Y', 
                            object_types={'MESH'}, 
                            global_scale=1.0,
                            apply_unit_scale=True,
                            apply_scale_options='FBX_SCALE_NONE',
                            bake_space_transform=True,
                            use_mesh_modifiers=True)
    
    # export OBJ
    bpy.ops.export_scene.obj(filepath=oPath, 
                            check_existing=True, 
                            axis_forward='-Z', 
                            axis_up='Y', 
                            filter_glob="*.obj;*.mtl", 
                            use_selection=True,  
                            use_mesh_modifiers=True, 
                            use_edges=True, 
                            use_smooth_groups=False, 
                            use_smooth_groups_bitflags=False, 
                            use_normals=True, 
                            use_uvs=True, 
                            use_materials=True, 
                            use_triangles=False, 
                            use_nurbs=False, 
                            use_vertex_groups=False, 
                            use_blen_objects=True, 
                            group_by_object=False, 
                            group_by_material=False, 
                            keep_vertex_order=False, 
                            global_scale=1.0, 
                            path_mode='AUTO')
