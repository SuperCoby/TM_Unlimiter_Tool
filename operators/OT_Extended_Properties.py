import bpy
from bpy.props import EnumProperty


items_mat_category = [
    ('Stadium','Stadium',''),
    ('Island','Island',''),
    ('Speed','Speed',''),
    ('Rally','Rally',''),
    ('Alpine','Alpine',''),
    ('Coast','Coast',''),
    ('Bay','Bay',''),
    ('Collision','Collision',''),
    ('TextureCustom', 'TextureCustom', ''),
    ('IsTransparent', 'IsTransparent', ''),
    ('NoTrails', 'NoTrails', ''),
    ('NoShadows', 'NoShadows', ''),
]

items_stadium = [
    ('StadiumAirship','StadiumAirship',''),
    ('StadiumCircuit','StadiumCircuit',''),
    ('StadiumCircuitLogo','StadiumCircuitLogo',''),
    ('StadiumCircuitScreen','StadiumCircuitScreen',''),
    ('StadiumControlGlass','StadiumControlGlass',''),
    ('StadiumControlInterior','StadiumControlInterior',''),
    ('StadiumControlLogos','StadiumControlLogos',''),
    ('StadiumControlStands','StadiumControlStands',''),
    ('StadiumDirt','StadiumDirt',''),
    ('StadiumDirtGrid','StadiumDirtGrid',''),
    ('StadiumDirtRoad','StadiumDirtRoad',''),
    ('StadiumDirtToRoad','StadiumDirtToRoad',''),
    ('StadiumFabric','StadiumFabric',''),
    ('StadiumFabricAuvent2','StadiumFabricAuvent2',''),
    ('StadiumFabricBorderRubber','StadiumFabricBorderRubber',''),
    ('StadiumFabricPool','StadiumFabricPool',''),
    ('StadiumFabricStands2','StadiumFabricStands2',''),
    ('StadiumFabricStructure','StadiumFabricStructure',''),
    ('StadiumFan','StadiumFan',''),
    ('StadiumGrass','StadiumGrass',''),
    ('StadiumInflatable','StadiumInflatable',''),
    ('StadiumInflatable2','StadiumInflatable2',''),
    ('StadiumInflatableCactus','StadiumInflatableCactus',''),
    ('StadiumInflatableCastle','StadiumInflatableCastle',''),
    ('StadiumInflatablePalmTree','StadiumInflatablePalmTree',''),
    ('StadiumInflatableSnowTree','StadiumInflatableSnowTree',''),
    ('StadiumPillar','StadiumPillar',''),
    ('StadiumPlatform','StadiumPlatform',''),
    ('StadiumPlatformAuventAlpha','StadiumPlatformAuventAlpha',''),
    ('StadiumPlatformFloor','StadiumPlatformFloor',''),
    ('StadiumPlatformPillar','StadiumPlatformPillar',''),
    ('StadiumPlatformSoundSystem','StadiumPlatformSoundSystem',''),
    ('StadiumPubNvidiaWorldcup','StadiumPubNvidiaWorldcup',''),
    ('StadiumRaceSignsRubber','StadiumRaceSignsRubber',''),
    ('StadiumRoad','StadiumRoad',''),
    ('StadiumRoadCircuitBorder','StadiumRoadCircuitBorder',''),
    ('StadiumRoadDetails','StadiumRoadDetails',''),
    ('StadiumRoadFreeWheeling','StadiumRoadFreeWheeling',''),
    ('StadiumRoadGrid','StadiumRoadGrid',''),
    ('StadiumRoadRace','StadiumRoadRace',''),
    ('StadiumRoadTurbo','StadiumRoadTurbo',''),
    ('StadiumRoadTurboRoulette','StadiumRoadTurboRoulette',''),
    ('StadiumSculpt','StadiumSculpt',''),
    ('StadiumSculpt2','StadiumSculpt2',''),
    ('StadiumStartLogo','StadiumStartLogo',''),
    ('StadiumStructureAlpha','StadiumStructureAlpha',''),
    ('StadiumStructureGeneric','StadiumStructureGeneric',''),
    ('StadiumTurboSpots','StadiumTurboSpots',''),
    ('StadiumWarpGlass','StadiumWarpGlass',''),
    ('StadiumWarpParking','StadiumWarpParking',''),
    ('StadiumWarpParvis','StadiumWarpParvis',''),
    ('StadiumWarpRoute','StadiumWarpRoute',''),
    ('StadiumWater','StadiumWater',''),
]

items_island = [
    ('IslandBeach','IslandBeach',''),
    ('IslandBeachUnderSea','IslandBeachUnderSea',''),
    ('IslandBuilding','IslandBuilding',''),
    ('IslandConcrete','IslandConcrete',''),
    ('IslandCroisetteConcrete','IslandCroisetteConcrete',''),
    ('IslandCroisetteTransition','IslandCroisetteTransition',''),
    ('IslandDecorPlantesMip','IslandDecorPlantesMip',''),
    ('IslandGrass','IslandGrass',''),
    ('IslandHighway','IslandHighway',''),
    ('IslandHighWayBorders','IslandHighWayBorders',''),
    ('IslandHighWayTransitions','IslandHighWayTransitions',''),
    ('IslandPlateform','IslandPlateform',''),
    ('IslandPlateformAlpha','IslandPlateformAlpha',''),
    ('IslandPlateformFloor','IslandPlateformFloor',''),
    ('IslandRoadSigns','IslandRoadSigns',''),
    ('IslandRoadSigns2','IslandRoadSigns2',''),
    ('IslandSea','IslandSea',''),
    ('IslandTransitionBeach','IslandTransitionBeach',''),
    ('IslandTransitionGrass','IslandTransitionGrass',''),
    ('IslandTreesMip','IslandTreesMip',''),
    ('IslandVegetationMip','IslandVegetationMip',''),
]

items_speed = [
    ('SpeedAsphalt','SpeedAsphalt',''),
    ('SpeedBridgeAlpha','SpeedBridgeAlpha',''),
    ('SpeedBrushedMetal','SpeedBrushedMetal',''),
    ('SpeedCliff2','SpeedCliff2',''),
    ('SpeedCliff2Plant','SpeedCliff2Plant',''),
    ('SpeedCliff2Rock','SpeedCliff2Rock',''),
    ('SpeedCliff2Sand','SpeedCliff2Sand',''),
    ('SpeedConcrete','SpeedConcrete',''),
    ('SpeedConcreteBorder','SpeedConcreteBorder',''),
    ('SpeedCrashBarrier','SpeedCrashBarrier',''),
    ('SpeedDecors','SpeedDecors',''),
    ('SpeedDerrickAlphas','SpeedDerrickAlphas',''),
    ('SpeedFreeWheeling','SpeedFreeWheeling',''),
    ('SpeedMetalAlphas','SpeedMetalAlphas',''),
    ('SpeedMetalGrid','SpeedMetalGrid',''),
    ('SpeedParkingAsphalt','SpeedParkingAsphalt',''),
    ('SpeedParkingTurbo','SpeedParkingTurbo',''),
    ('SpeedRiver','SpeedRiver',''),
    ('SpeedRiverBeach','SpeedRiverBeach',''),
    ('SpeedRiverBeachUnderWater','SpeedRiverBeachUnderWater',''),
    ('SpeedRoadSigns','SpeedRoadSigns',''),
    ('SpeedRock','SpeedRock',''),
    ('SpeedSaguaro','SpeedSaguaro',''),
    ('SpeedSand','SpeedSand',''),
    ('SpeedSandBorder','SpeedSandBorder',''),
    ('SpeedTunnelAsphalt','SpeedTunnelAsphalt',''),
    ('SpeedTunnelConcrete','SpeedTunnelConcrete',''),
    ('SpeedTunnelDecors','SpeedTunnelDecors',''),
    ('SpeedTunnelRoadSigns','SpeedTunnelRoadSigns',''),
    ('SpeedTunnelTurbo','SpeedTunnelTurbo',''),
    ('SpeedTurbo','SpeedTurbo',''),
    ('SpeedTurboRoulette','SpeedTurboRoulette',''),
    ('SpeedWater','SpeedWater',''),
    ('SpeedWoodPlanks','SpeedWoodPlanks',''),
]

items_rally = [
    ('', '', ''),
]

items_alpine = [
    ('AlpineAsphalt','AlpineAsphalt',''),
    ('AlpineBark','AlpineBark',''),
    ('AlpineGreatWall','AlpineGreatWall',''),
    ('AlpineGreatWallCastle','AlpineGreatWallCastle',''),
    ('AlpineGreatWallRoad','AlpineGreatWallRoad',''),
    ('AlpineGreatWallToundra','AlpineGreatWallToundra',''),
    ('AlpineHill','AlpineHill',''),
    ('AlpineHillToundra','AlpineHillToundra',''),
    ('AlpineHillTree','AlpineHillTree',''),
    ('AlpineIce','AlpineIce',''),
    ('AlpineIceBorders','AlpineIceBorders',''),
    ('AlpineIceCanyon','AlpineIceCanyon',''),
    ('AlpineLamp','AlpineLamp',''),
    ('AlpineMetalGrid','AlpineMetalGrid',''),
    ('AlpinePylonsWood','AlpinePylonsWood',''),
    ('AlpineRaceFlags','AlpineRaceFlags',''),
    ('AlpineRoadChalet','AlpineRoadChalet',''),
    ('AlpineRoadWood','AlpineRoadWood',''),
    ('AlpineRoadWoodFreeWheeling','AlpineRoadWoodFreeWheeling',''),
    ('AlpineRoadWoodTurbo','AlpineRoadWoodTurbo',''),
    ('AlpineRoadWoodTurboRoulette','AlpineRoadWoodTurboRoulette',''),
    ('AlpineRocks','AlpineRocks',''),
    ('AlpineSigns','AlpineSigns',''),
    ('AlpineSnow','AlpineSnow',''),
    ('AlpineSnowBorders','AlpineSnowBorders',''),
    ('AlpineTemple','AlpineTemple',''),
    ('AlpineTempleAlpha','AlpineTempleAlpha',''),
    ('AlpineToundra','AlpineToundra',''),
    ('AlpineTrees','AlpineTrees',''),
    ('AlpineTunnelOutside','AlpineTunnelOutside',''),
    ('ApineGreatWallHillSnow','ApineGreatWallHillSnow',''),
    ('ApineGreatWallHillToundra','ApineGreatWallHillToundra',''),
]

items_coast = [
    ('CoastAsphalt','CoastAsphalt',''),
    ('CoastBoats','CoastBoats',''),
    ('CoastCircuit','CoastCircuit',''),
    ('CoastCircuitRumbleStrip','CoastCircuitRumbleStrip',''),
    ('CoastCircuitSigns','CoastCircuitSigns',''),
    ('CoastCircuitTransition','CoastCircuitTransition',''),
    ('CoastCircuitTransitionGrass','CoastCircuitTransitionGrass',''),
    ('CoastCircuitTurbo','CoastCircuitTurbo',''),
    ('CoastCircuitTurbo2','CoastCircuitTurbo2',''),
    ('CoastCliff','CoastCliff',''),
    ('CoastConcrete','CoastConcrete',''),
    ('CoastCorniche','CoastCorniche',''),
    ('CoastCornicheRoad','CoastCornicheRoad',''),
    ('CoastDecorBase','CoastDecorBase',''),
    ('CoastDirt','CoastDirt',''),
    ('CoastFoam','CoastFoam',''),
    ('CoastGrid','CoastGrid',''),
    ('CoastItemsAlpha','CoastItemsAlpha',''),
    ('CoastPlantes','CoastPlantes',''),
    ('CoastRedCobble','CoastRedCobble',''),
    ('CoastRoad','CoastRoad',''),
    ('CoastRoadBorder','CoastRoadBorder',''),
    ('CoastRoadMarks','CoastRoadMarks',''),
    ('CoastRoadSigns','CoastRoadSigns',''),
    ('CoastRoadSigns2','CoastRoadSigns2',''),
    ('CoastRoadTransition','CoastRoadTransition',''),
    ('CoastRoadTurbo','CoastRoadTurbo',''),
    ('CoastRoadTurbo2','CoastRoadTurbo2',''),
    ('CoastRoadTurboRoulette','CoastRoadTurboRoulette',''),
    ('CoastSea','CoastSea',''),
    ('CoastStone','CoastStone',''),
    ('CoastSubSea','CoastSubSea',''),
    ('CoastSubSeaTransition','CoastSubSeaTransition',''),
    ('CoastTunnel','CoastTunnel',''),
    ('CoastTunnelItemsAlpha','CoastTunnelItemsAlpha',''),
    ('CoastTunnelSigns','CoastTunnelSigns',''),
    ('CoastTunnelTurbo','CoastTunnelTurbo',''),
    ('CoastTunnelTurbo2','CoastTunnelTurbo2',''),
    ('CoastVegetation','CoastVegetation',''),
    ('CoastVegetation2','CoastVegetation2',''),
    ('CoastVillage','CoastVillage',''),
    ('CoastYacht','CoastYacht',''),
    ('CoastYachtAlpha','CoastYachtAlpha',''),
    ('CoastYachtFloor','CoastYachtFloor',''),
]

items_bay = [
    ('','',''),
]

items_col = [
    ('Concrete','Concrete',''),
    ('Pavement','Pavement',''),
    ('Grass','Grass',''),
    ('Ice','Ice',''),
    ('Metal','Metal',''),
    ('Sand','Sand',''),
    ('Dirt','Dirt',''),
    ('Turbo','Turbo',''),
    ('DirtRoad','DirtRoad',''),
    ('Rubber','Rubber',''),
    ('SlidingRubber','SlidingRubber',''),
    ('Test','Test',''),
    ('Rock','Rock',''),
    ('Water','Water',''),
    ('Wood','Wood',''),
    ('Danger','Danger',''),
    ('Asphalt','Asphalt',''),
    ('WetDirtRoad','WetDirtRoad',''),
    ('WetAsphalt','WetAsphalt',''),
    ('WetPavement','WetPavement',''),
    ('WetGrass','WetGrass',''),
    ('Snow','Snow',''),
    ('ResonantMetal','ResonantMetal',''),
    ('GolfBall','GolfBall',''),
    ('GolfWall','GolfWall',''),
    ('GolfGround','GolfGround',''),
    ('TurboRed','TurboRed',''),
    ('Bumper','Bumper',''),
    ('NotCollidable','NotCollidable',''),
    ('FreeWheeling','FreeWheeling',''),
    ('TurboRoulette','TurboRoulette',''),
]


class SNA_OT_AddCustomPropertyType(bpy.types.Operator):
    bl_idname = 'opr.add_custom_property_type'
    bl_label = 'Add Custom Property'

    @classmethod
    def poll(cls, context):
        if len(context.selected_objects) == 0:
            cls.poll_message_set('No selected objects')
            return False

        return True

    def execute(self, context):
        for ob in context.selected_objects:
            if ob.active_material:
                mat = ob.active_material
                sc = context.scene
                if sc.gbx_mat_cat == 'Stadium':
                    mat['TextureGame'] = sc.gbx_mat_stad
                if sc.gbx_mat_cat == 'Island':
                    mat['TextureGame'] = sc.gbx_mat_island
                if sc.gbx_mat_cat == 'Speed':
                    mat['TextureGame'] = sc.gbx_mat_speed
                if sc.gbx_mat_cat == 'Rally':
                    mat['TextureGame'] = sc.gbx_mat_rally
                if sc.gbx_mat_cat == 'Alpine':
                    mat['TextureGame'] = sc.gbx_mat_alpine
                if sc.gbx_mat_cat == 'Coast':
                    mat['TextureGame'] = sc.gbx_mat_coast
                if sc.gbx_mat_cat == 'Bay':
                    mat['TextureGame'] = sc.gbx_mat_bay
                if sc.gbx_mat_cat == 'Collision':
                    mat['Collision'] = sc.gbx_mat_col
                if sc.gbx_mat_cat in [
                    'TextureCustom',
                    'IsTransparent',
                    'NoTrails',
                    'NoShadows',
                ]:
                    mat[sc.gbx_mat_cat] = ''

        return { 'FINISHED' }


classes = (
    SNA_OT_AddCustomPropertyType,
)


scene_props = (
    ('gbx_mat_cat', EnumProperty(name='Mat Category', items = items_mat_category)),
    ('gbx_mat_stad', EnumProperty(name='Mat Stadium', items = items_stadium)),
    ('gbx_mat_island', EnumProperty(name='Mat Island', items = items_island)),
    ('gbx_mat_speed', EnumProperty(name='Mat Speed', items = items_speed)),
    ('gbx_mat_rally', EnumProperty(name='Mat Rally', items = items_rally)),
    ('gbx_mat_alpine', EnumProperty(name='Mat Alpine', items = items_alpine)),
    ('gbx_mat_coast', EnumProperty(name='Mat Coast', items = items_coast)),
    ('gbx_mat_bay', EnumProperty(name='Mat Bay', items = items_bay)),
    ('gbx_mat_col', EnumProperty(name='Collision', items = items_col)),
)
