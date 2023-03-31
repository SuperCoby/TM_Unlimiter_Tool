import bpy
from mathutils import Vector
import struct
import os
from bpy.props import StringProperty, FloatProperty


def WriteNumber( Writer, Number, Length ) :
    Result = Number.to_bytes( Length, 'little' )

    for i in range( 0, Length ) :
        Writer.append( Result[ i ] )

def WriteFloat( Writer, Float ) :
    Result = bytearray( struct.pack( 'f', Float ) )

    for i in range( 0, 4 ) :
        Writer.append( Result[ i ] )

def WriteStrRaw( Writer, String ) :
    for i in range( 0, len( String ) ) :
        Writer.append( ord( String[ i ] ) )

def WriteStrLen( Writer, String ) :
    WriteNumber( Writer, len( String ), 4 )
    WriteStrRaw( Writer, String )

def GetEvaluatedMesh( Object ) :
    depsgraph = bpy.context.evaluated_depsgraph_get()
    object_eval = Object.evaluated_get(depsgraph)
    mesh_from_eval = object_eval.to_mesh()
    return mesh_from_eval

# 0 - Nothing
# 1 - prev UV+1 - UV Zero fill
# 2 - prev UV+1 - UV Zero fill
# 4 - post UV+1 - UV Zero fill
# 8 - post UV+1 - UV Zero fill
def GetShaderFlags( ShaderID ) :
    if ShaderID == 'StadiumGrass' :
        return 0
    elif ShaderID == 'StadiumWater' :
        return 0
    elif ShaderID == 'StadiumDirt' :
        return 1
    elif ShaderID == 'StadiumRoad' :
        return 12
    elif ShaderID == 'StadiumRoadDetails' :
        return 12
    elif ShaderID == 'Dev5' :
        return 12
    elif ShaderID == 'Dev7' :
        return 0

    return 4

def GetSurfaceIndex( CollisionMaterial ) :
    CollisionMaterials = [
        'Concrete', 'Pavement',
        'Grass', 'Ice',
        'Metal', 'Sand',
        'Dirt', 'Turbo',
        'DirtRoad', 'Rubber',
        'SlidingRubber', 'Test',
        'Rock', 'Water',
        'Wood', 'Danger',
        'Asphalt', 'WetDirtRoad',
        'WetAsphalt', 'WetPavement',
        'WetGrass', 'Snow',
        'ResonantMetal', 'GolfBall',
        'GolfWall', 'GolfGround',
        'TurboRed', 'Bumper',
        'NotCollidable', 'FreeWheeling',
        'TurboRoulette'
    ]

    try :
        return CollisionMaterials.index( CollisionMaterial )
    except :
        return -1

#
# This function writes single CPlugTree
# Only the tris with the given material slot index are included
#
def DoWriteTree ( Writer, Object, ObjectMesh, SlotIndex, MaterialInfo, InstancesNb ) :
    InstancesNb += 1

    WriteNumber( Writer, 0x0904F000, 4 )

    if MaterialInfo != None :
        WriteNumber( Writer, 0x0904F00D, 4 )

        if SlotIndex == 0 :
            WriteNumber( Writer, 0x00000003, 4 )

        WriteNumber( Writer, 0x40000000, 4 )
        WriteStrLen( Writer, MaterialInfo[ 'ExtName' ] )

        WriteNumber( Writer, 0xFFFFFFFF, 4 )

    WriteNumber( Writer, 0x0904F016, 4 )
    WriteNumber( Writer, InstancesNb, 4 )

    # 09 01E 000 -- Start, CPlugVisualIndexedTriangles
    WriteNumber( Writer, 0x0901E000, 4 )

    LayerUVs = []
    Vertices = []
    Loops = []

    ObjectMesh.calc_loop_triangles()

    if len( ObjectMesh.uv_layers ) == 0 :
        DictionaryVerts = {}

        for Tri in ObjectMesh.loop_triangles :
            if Tri.material_index != SlotIndex :
                continue

            for VertexIndex in Tri.vertices:
                Value = DictionaryVerts.get( VertexIndex )

                if Value is None :
                    Value = DictionaryVerts[ VertexIndex ] = len( Vertices )
                    Vertices.append( ObjectMesh.vertices[ VertexIndex ] )

                Loops.append( Value )

        del DictionaryVerts
    else :
        DictionaryUVs = {}
        LayerUV = []

        for Tri in ObjectMesh.loop_triangles :
            if Tri.material_index != SlotIndex :
                continue

            for LoopIndex in Tri.loops :
                MapData = ObjectMesh.uv_layers.active.data[ LoopIndex ].uv

                Key = ObjectMesh.loops[ LoopIndex ].vertex_index, ( round( MapData.x, 4 ), round( MapData.y, 4 ) )
                Value = DictionaryUVs.get( Key )

                if Value is None :
                    Value = DictionaryUVs[ Key ] = len( Vertices )
                    Vertices.append( ObjectMesh.vertices[ ObjectMesh.loops[ LoopIndex ].vertex_index ] )
                    LayerUV.append( MapData )

                Loops.append( Value )

        MaterialIntFlags = 0

        if MaterialInfo != None :
            MaterialIntFlags = MaterialInfo[ 'IntFlags' ]

        if MaterialIntFlags & 1 :
            LayerUVs.append( [ Vector( [ 0, 0 ] ) for x in range( len( LayerUV ) ) ] )

        if MaterialIntFlags & 2 :
            LayerUVs.append( [ Vector( [ 0, 0 ] ) for x in range( len( LayerUV ) ) ] )

        LayerUVs.append( LayerUV )

        if MaterialIntFlags & 4 :
            LayerUVs.append( [ Vector( [ 0, 0 ] ) for x in range( len( LayerUV ) ) ] )

        if MaterialIntFlags & 8 :
            LayerUVs.append( [ Vector( [ 0, 0 ] ) for x in range( len( LayerUV ) ) ] )

        del DictionaryUVs

    # 09 006 00E -- Start
    WriteNumber( Writer, 0x0900600E, 4 )
    WriteNumber( Writer, 0x00000038, 4 )                                # VisualFlags
    WriteNumber( Writer, len( LayerUVs ), 4 )                           # UVsCount
    WriteNumber( Writer, len( Vertices ), 4 )                           # VertexNb
    WriteNumber( Writer, 0x00000000, 4 )                                # Unknown

    for MapLayer in LayerUVs :
        WriteNumber( Writer, 0x00000000, 4 )

        for LayerData in MapLayer :
            WriteFloat( Writer, LayerData.x )
            WriteFloat( Writer, LayerData.y )

    # Note: takes into account the whole object, not just
    # the tris in this material slot. Correct or not?
    WriteFloat( Writer, Object.dimensions.x / 2 )                       # GlobalHalfDiagX?
    WriteFloat( Writer, Object.dimensions.z / 2 )                       # GlobalHalfDiagY?
    WriteFloat( Writer, Object.dimensions.y / 2 )                       # GlobalHalfDiagZ?
    WriteFloat( Writer, Object.dimensions.x / 2 )                       # LocalHalfDiagX?
    WriteFloat( Writer, Object.dimensions.z / 2 )                       # LocalHalfDiagY?
    WriteFloat( Writer, Object.dimensions.y / 2 )                       # LocalHalfDiagZ?
    WriteNumber( Writer, 0x00000000, 4 )                                # Unknown

    # 09 02C 004 -- Start, VerticesData
    WriteNumber( Writer, 0x0902C004, 4 )

    for VertexData in Vertices :
        #VertexPos = Object.matrix_world * VertexData.co
        #VertexPos.y -= OriginObject.dimensions.y
        VertexPos = Object.matrix_local @ VertexData.co

        WriteFloat( Writer, VertexPos.x )                               # Vertex X
        WriteFloat( Writer, VertexPos.z )                               # Vertex Y
        WriteFloat( Writer, -VertexPos.y )                              # Vertex Z
        WriteFloat( Writer, VertexData.normal.x )                       # Normal X
        WriteFloat( Writer, VertexData.normal.z )                       # Normal Y
        WriteFloat( Writer, -VertexData.normal.y )                      # Normal Z
        WriteFloat( Writer, Object.color[ 0 ] )                         # Color R
        WriteFloat( Writer, Object.color[ 1 ] )                         # Color G
        WriteFloat( Writer, Object.color[ 2 ] )                         # Color B
        WriteFloat( Writer, Object.color[ 3 ] )                         # Color A

    WriteNumber( Writer, 0x00000000, 4 )                                # Unknown
    WriteNumber( Writer, 0x00000000, 4 )                                # Unknown

    # 09 06A 001 -- Start
    WriteNumber( Writer, 0x0906A001, 4 )
    WriteNumber( Writer, 0x00000001, 4 )                                # Unknown

    # 09 057 000 -- Start
    WriteNumber( Writer, 0x09057000, 4 )
    WriteNumber( Writer, 0x00000002, 4 )                                # Unknown
    WriteNumber( Writer, len( Loops ), 4 )                              # List size

    for Loop in Loops  :
        WriteNumber( Writer, Loop, 2 )

    WriteNumber( Writer, 0xFACADE01, 4 )
    # 09 057 000 -- End
    # 09 06A 001 -- End
    # 09 02C 004 -- End
    # 09 006 00E -- End

    WriteNumber( Writer, 0xFACADE01, 4 )
    # 09 01E 000 -- End

    WriteNumber( Writer, 0xFFFFFFFF, 4 )
    WriteNumber( Writer, 0xFFFFFFFF, 4 )
    WriteNumber( Writer, 0xFFFFFFFF, 4 )
    WriteNumber( Writer, 0xFACADE01, 4 )

    del Vertices, LayerUVs, Loops
    return InstancesNb

#
# This function writes a couple of CPlugTrees basing on Objects argument
# One tree for each material slot
#
def DoWriteObject ( Writer, Object, MaterialInfos, InstancesNb ) :
    ObjectMesh = GetEvaluatedMesh( Object )
    NumSlots = max( 1, len( Object.data.materials ) )

    WriteNumber( Writer, 0x0904F000, 4 )

    WriteNumber( Writer, 0x0904F006, 4 )
    WriteNumber( Writer, 0x0000000A, 4 )        # Unknown
    WriteNumber( Writer, NumSlots, 4 )          # Childs

    for SlotIndex in range( 0, NumSlots ) :
        MaterialInfo = None
        if len( Object.data.materials ) != 0 :
            MaterialInfo = MaterialInfos[ SlotIndex ]

        InstancesNb += 1
        WriteNumber( Writer, InstancesNb, 4 )
        InstancesNb = DoWriteTree( Writer, Object, ObjectMesh, SlotIndex, MaterialInfo, InstancesNb )

    WriteNumber( Writer, 0xFACADE01, 4 )

    Object.to_mesh_clear()
    return InstancesNb

def DoWriteBlock ( Objects, Context, FilePath, FileName, SpawnX, SpawnY, SpawnZ, BlockIdentifier, BlockAuthor ) :
    if not bpy.ops.object.mode_set.poll() :
        return { 'CANCELLED' }

    if len( BlockIdentifier ) == 0 or len( BlockAuthor ) == 0 :
        return { 'CANCELLED' }

    bpy.ops.object.mode_set( mode = 'OBJECT' )

    # Remove unused slots so we don't write empty trees
    bpy.ops.object.material_slot_remove_unused()

    MaterialInfos = []
    MaterialsNb = 0

    for Object in Objects :
        Materials = Object.data.materials
        ObjectMaterials = []

        for Index in range( 0, len( Materials ) ) :
            Material = Materials[ Index ]
            MaterialInfo = {
                'ExtFlags' : 0,
                'IntFlags': 0,
            }

            if 'TextureGame' in Material :
                MaterialInfo[ 'IntFlags' ] = GetShaderFlags( Material[ 'TextureGame' ] )
                MaterialInfo[ 'TextureID' ] = Material[ 'TextureGame' ]
                MaterialInfo[ 'ExtFlags' ] |= 1
            elif 'TextureCustom' in Material :
                MaterialInfo[ 'TextureID' ] = Material[ 'TextureCustom' ]
                MaterialInfo[ 'ExtFlags' ] |= 2

            if 'Collision' in Material :
                SurfaceIndex = GetSurfaceIndex( Material[ 'Collision' ] )

                if SurfaceIndex != -1 and SurfaceIndex != 27 :
                    MaterialInfo[ 'SurfaceID' ] = SurfaceIndex
                    MaterialInfo[ 'ExtFlags' ] |= 4

            if not Material.use_backface_culling :
                MaterialInfo[ 'ExtFlags' ] |= 8

            if 'NoTrails' in Material :
                MaterialInfo[ 'ExtFlags' ] |= 16

            if 'NoShadows' in Material :
                MaterialInfo[ 'ExtFlags' ] |= 32

            if 'IsTransparent' in Material :
                MaterialInfo[ 'ExtFlags' ] |= 64

            if MaterialInfo[ 'ExtFlags' ] == 0 :
                continue

            MaterialInfo[ 'ExtName' ] = 'm' + str( Index )
            MaterialInfo[ 'IntName' ] = Material.name
            ObjectMaterials.append( MaterialInfo )

        MaterialInfos.append( ObjectMaterials )
        MaterialsNb += len( ObjectMaterials )
    #

    Content = bytearray()
    Header = bytearray()
    Instances = 1

    # MainNode
    WriteNumber( Content, 0x3F004000, 4 )

    WriteFloat( Content, SpawnX )
    WriteFloat( Content, SpawnY )
    WriteFloat( Content, SpawnZ )

    WriteStrLen( Content, BlockIdentifier )
    WriteStrLen( Content, BlockAuthor )

    WriteNumber( Content, MaterialsNb, 4 )

    for ObjectMaterials in MaterialInfos :

        for Material in ObjectMaterials :
            WriteNumber( Content, Material[ 'ExtFlags' ], 1 )
            WriteStrLen( Content, Material[ 'ExtName' ] )

            if Material[ 'ExtFlags' ] & 3 :
                WriteStrLen( Content, Material[ 'TextureID' ] )

            if Material[ 'ExtFlags' ] & 4 :
                WriteNumber( Content, Material[ 'SurfaceID' ], 1 )

    # Writing x000 chunk
    WriteNumber( Content, 0x09005000, 4 )
    WriteNumber( Content, 0x00000001, 4 )

    # Writing x011 chunk
    WriteNumber( Content, 0x09005011, 4 )
    WriteNumber( Content, 0x00000000, 4 )
    WriteNumber( Content, 0x00000000, 4 )
    WriteNumber( Content, 0x00000001, 4 )

    for Index in range( 0, len( Objects ) ) :
        Instances = DoWriteObject( Content, Objects[ Index ], MaterialInfos[ Index ], Instances )
    #

    # Writing Header
    WriteStrRaw( Header, 'GBX' )
    WriteNumber( Header, 6, 2 )
    WriteStrRaw( Header, 'BUUR' )

    WriteNumber( Header, 0x3F004000, 4 )
    WriteNumber( Header, 0x00000000, 4 )

    WriteNumber( Header, Instances + 2, 4 )
    WriteNumber( Header, 0x00000000, 4 )
    WriteNumber( Content, 0xFACADE01, 4 )

    os.makedirs( FilePath, exist_ok = True )
    exp = os.path.join( FilePath, FileName )
    with open( exp, 'wb' ) as File :
        File.write( Header )
        File.write( Content )

    return { 'FINISHED' }


class GBX_OT_ExportBatch ( bpy.types.Operator ) :
    '''Save scene as TrackMania Infinity custom block'''
    bl_idname = 'opr.gbx_export_batch'
    bl_label = 'Export'
    bl_options = { 'UNDO' }

    def execute ( Self, Context ) :
        sc = Context.scene
        objects = Context.visible_objects
        exp_dir = os.path.realpath(bpy.path.abspath(sc.gbx_exp_dir))
        for obj in objects:
            path = os.path.join(exp_dir, obj.name)
            DoWriteBlock([obj], Context, path, 'Model.Block.Gbx', sc.gbx_spawn_x, sc.gbx_spawn_y, sc.gbx_spawn_z, obj.name, sc.gbx_author )
        return { 'FINISHED' }


classes = (
    GBX_OT_ExportBatch,
)


scene_props = (
    ('gbx_author', StringProperty(name='Author', default='Nadeo')),
    ('gbx_spawn_x', FloatProperty(name='Spawn X', default=0.0)),
    ('gbx_spawn_y', FloatProperty(name='Spawn Y', default=0.0)),
    ('gbx_spawn_z', FloatProperty(name='Spawn Z', default=0.0)),
    ('gbx_exp_dir', StringProperty(name='Export Directory', default='', subtype='DIR_PATH')),
)
