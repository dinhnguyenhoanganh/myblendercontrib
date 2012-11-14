# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

bl_info = {
        'name': "MilkShape3D MS3D format (.ms3d)",
        'description': "Import / Export MilkShape3D MS3D files"\
                " (conform with v1.8.4)",
        'author': "Alexander Nussbaumer",
        'version': (0, 4, 9, 0),
        'blender': (2, 6, 3, 0),
        'location': "File > Import & File > Export",
        #'warning': "[2012-11-14] exporter is working (without animation)",
        'wiki_url': "http://wiki.blender.org/index.php/Extensions:2.6/Py/"\
                "Scripts/Import-Export/MilkShape3D_MS3D",
        'tracker_url': "http://projects.blender.org/tracker/index.php"\
                "?func=detail&aid=29404",
        'category': 'Import-Export',
        }

###############################################################################
#234567890123456789012345678901234567890123456789012345678901234567890123456789
#--------1---------2---------3---------4---------5---------6---------7---------


# ##### BEGIN COPYRIGHT BLOCK #####
#
# initial script copyright (c)2011,2012 Alexander Nussbaumer
#
# ##### END COPYRIGHT BLOCK #####


# To support reload properly, try to access a package var,
# if it's there, reload everything
if ('bpy' in locals()):
    import imp
    if 'io_scene_ms3d.ms3d_ui' in locals():
        imp.reload(io_scene_ms3d.ms3d_ui)
else:
    from io_scene_ms3d.ms3d_ui import (
            Ms3dImportOperator,
            Ms3dExportOperator,
            )


#import blender stuff
from bpy.utils import (
        register_module,
        unregister_module,
        )
from bpy.types import (
        INFO_MT_file_export,
        INFO_MT_file_import,
        )


###############################################################################
# registration
def register():
    register_module(__name__)
    INFO_MT_file_export.append(Ms3dExportOperator.menu_func)
    INFO_MT_file_import.append(Ms3dImportOperator.menu_func)


def unregister():
    unregister_module(__name__)
    INFO_MT_file_export.remove(Ms3dExportOperator.menu_func)
    INFO_MT_file_import.remove(Ms3dImportOperator.menu_func)


###############################################################################
# global entry point
if (__name__ == "__main__"):
    register()


###############################################################################
#234567890123456789012345678901234567890123456789012345678901234567890123456789
#--------1---------2---------3---------4---------5---------6---------7---------
# ##### END OF FILE #####
