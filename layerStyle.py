from qgis.PyQt.QtXml import QDomDocument

def smhiLayerStyle(ws):
        
    def get_filename_from_value(value):
      value = int(value)
      svg_files = ['0-1.svg', '102-103.svg', '104-106.svg', 
                   '107-109.svg', '110-111.svg', '112-114.svg', 
                   '115-116.svg', '117-119.svg', '12-13.svg', 
                   '120-121.svg', '122-124.svg', '125-127.svg', 
                   '128-130.svg', '14-16.svg', '17-19.svg', '2-3.svg', 
                   '20-21.svg', '22-24.svg', '25-26.svg', '27-29.svg', 
                   '30-31.svg', '32-34.svg', '35-37.svg', '38-39.svg', 
                   '4-6.svg', '40-42.svg', '43-44.svg', '45-47.svg', 
                   '48-49.svg', '50-51.svg', '52-55.svg', '56-57.svg', 
                   '58-60.svg', '61-62.svg', '63-65.svg', '66-67.svg', 
                   '68-70.svg', '7-8.svg', '71-73.svg', '74-75.svg', 
                   '76-78.svg', '79-80.svg', '81-83.svg', '84-85.svg', 
                   '86-88.svg', '89-91.svg', '9-11.svg', '92-93.svg', 
                   '94-96.svg', '97-98.svg', '99-101.svg', 
                   'unknown.svg']
      
      for filename in svg_files:
          parts = filename.split('.')[0].split('-')
          if len(parts) == 2:
              start, end = map(int, parts)
              if start <= value <= end:
                  return filename
      return 'unknown.svg'

    document = QDomDocument()

    p2 = get_filename_from_value(ws)
    
    p1 ='''<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis labelsEnabled="1" styleCategories="Symbology|Labeling" version="3.34.4-Prizren">
  <renderer-v2 symbollevels="0" forceraster="0" enableorderby="0" type="singleSymbol" referencescale="-1">
    <symbols>
      <symbol force_rhr="0" is_animated="0" frame_rate="10" name="0" clip_to_extent="1" type="marker" alpha="1">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer locked="0" id="{5c67571c-0f6e-47ae-a68f-dedf761f770d}" class="SvgMarker" enabled="1" pass="0">
          <Option type="Map">
            <Option value="0" name="angle" type="QString"/>
            <Option value="232,113,141,255" name="color" type="QString"/>
            <Option value="0" name="fixedAspectRatio" type="QString"/>
            <Option value="1" name="horizontal_anchor_point" type="QString"/>
            <Option value="WMO Wind Barbs/mask.svg" name="name" type="QString"/>
            <Option value="0,0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="Point" name="offset_unit" type="QString"/>
            <Option value="35,35,35,255" name="outline_color" type="QString"/>
            <Option value="0" name="outline_width" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
            <Option value="Point" name="outline_width_unit" type="QString"/>
            <Option name="parameters"/>
            <Option value="diameter" name="scale_method" type="QString"/>
            <Option value="50" name="size" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
            <Option value="Point" name="size_unit" type="QString"/>
            <Option value="1" name="vertical_anchor_point" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="to_int(&quot;wd&quot; )+90" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
                <Option name="enabled" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="case&#xd;&#xa; when @B_maska_symoler = 'ja' then 1&#xd;&#xa; else 0&#xd;&#xa; end" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer locked="0" id="{ce618e36-cdeb-4abd-9564-6f57b3ec43e1}" class="SvgMarker" enabled="1" pass="0">
          <Option type="Map">
            <Option value="0" name="angle" type="QString"/>
            <Option value="232,113,141,255" name="color" type="QString"/>
            <Option value="0" name="fixedAspectRatio" type="QString"/>
            <Option value="1" name="horizontal_anchor_point" type="QString"/>
            <Option value="WMO Wind Barbs/'''
    p3 = '''" name="name" type="QString"/>
            <Option value="0,0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="Point" name="offset_unit" type="QString"/>
            <Option value="35,35,35,255" name="outline_color" type="QString"/>
            <Option value="0" name="outline_width" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
            <Option value="Point" name="outline_width_unit" type="QString"/>
            <Option name="parameters"/>
            <Option value="diameter" name="scale_method" type="QString"/>
            <Option value="50" name="size" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
            <Option value="Point" name="size_unit" type="QString"/>
            <Option value="1" name="vertical_anchor_point" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="to_int(&quot;wd&quot; )+90" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <selection mode="Default">
    <selectionColor invalid="1"/>
    <selectionSymbol>
      <symbol force_rhr="0" is_animated="0" frame_rate="10" name="" clip_to_extent="1" type="marker" alpha="1">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer locked="0" id="{8ba9f60a-5c1d-4b79-b8ed-8b6afc6639df}" class="SimpleMarker" enabled="1" pass="0">
          <Option type="Map">
            <Option value="0" name="angle" type="QString"/>
            <Option value="square" name="cap_style" type="QString"/>
            <Option value="255,0,0,255" name="color" type="QString"/>
            <Option value="1" name="horizontal_anchor_point" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="circle" name="name" type="QString"/>
            <Option value="0,0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="35,35,35,255" name="outline_color" type="QString"/>
            <Option value="solid" name="outline_style" type="QString"/>
            <Option value="0" name="outline_width" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
            <Option value="MM" name="outline_width_unit" type="QString"/>
            <Option value="diameter" name="scale_method" type="QString"/>
            <Option value="2" name="size" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
            <Option value="MM" name="size_unit" type="QString"/>
            <Option value="1" name="vertical_anchor_point" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </selectionSymbol>
  </selection>
  <labeling type="simple">
    <settings calloutType="simple">
      <text-style fontItalic="0" capitalization="0" isExpression="1" legendString="Aa" fontFamily="Open Sans" fontUnderline="0" namedStyle="Regular" fontWeight="50" textOrientation="horizontal" blendMode="0" fontLetterSpacing="0" fontWordSpacing="0" allowHtml="0" multilineHeightUnit="Percentage" textOpacity="1" textColor="50,50,50,255" fieldName="'Vindprognos avser: ' || '&#xa;'  ||   &quot;validTime&quot;  ||  '&#xa;'   ||  &quot;vindtext&quot;  || ' m/s ' || &quot;vindriktning&quot; " forcedItalic="0" fontStrikeout="0" multilineHeight="1" fontSizeMapUnitScale="3x:0,0,0,0,0,0" useSubstitutions="0" previewBkgrdColor="255,255,255,255" fontKerning="1" forcedBold="0" fontSizeUnit="Point" fontSize="10">
        <families/>
        <text-buffer bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferBlendMode="0" bufferDraw="0" bufferJoinStyle="128" bufferSize="1" bufferColor="250,250,250,255" bufferSizeUnits="MM" bufferNoFill="1" bufferOpacity="1"/>
        <text-mask maskSize="0" maskOpacity="1" maskType="0" maskJoinStyle="128" maskSizeMapUnitScale="3x:0,0,0,0,0,0" maskedSymbolLayers="" maskEnabled="0" maskSizeUnits="MM"/>
        <background shapeSizeY="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeRotation="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeSizeType="0" shapeOffsetUnit="Point" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiUnit="Point" shapeRotationType="0" shapeBorderWidthUnit="Point" shapeBlendMode="0" shapeBorderColor="128,128,128,255" shapeType="0" shapeRadiiY="0" shapeOpacity="1" shapeSVGFile="" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeSizeUnit="Point" shapeRadiiX="0" shapeDraw="1" shapeOffsetX="0" shapeBorderWidth="0" shapeOffsetY="0" shapeSizeX="0" shapeFillColor="255,255,255,255" shapeJoinStyle="64">
          <symbol force_rhr="0" is_animated="0" frame_rate="10" name="markerSymbol" clip_to_extent="1" type="marker" alpha="1">
            <data_defined_properties>
              <Option type="Map">
                <Option value="" name="name" type="QString"/>
                <Option name="properties"/>
                <Option value="collection" name="type" type="QString"/>
              </Option>
            </data_defined_properties>
            <layer locked="0" id="" class="SimpleMarker" enabled="1" pass="0">
              <Option type="Map">
                <Option value="0" name="angle" type="QString"/>
                <Option value="square" name="cap_style" type="QString"/>
                <Option value="255,158,23,255" name="color" type="QString"/>
                <Option value="1" name="horizontal_anchor_point" type="QString"/>
                <Option value="bevel" name="joinstyle" type="QString"/>
                <Option value="circle" name="name" type="QString"/>
                <Option value="0,0" name="offset" type="QString"/>
                <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
                <Option value="MM" name="offset_unit" type="QString"/>
                <Option value="35,35,35,255" name="outline_color" type="QString"/>
                <Option value="solid" name="outline_style" type="QString"/>
                <Option value="0" name="outline_width" type="QString"/>
                <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
                <Option value="MM" name="outline_width_unit" type="QString"/>
                <Option value="diameter" name="scale_method" type="QString"/>
                <Option value="2" name="size" type="QString"/>
                <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
                <Option value="MM" name="size_unit" type="QString"/>
                <Option value="1" name="vertical_anchor_point" type="QString"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option value="" name="name" type="QString"/>
                  <Option name="properties"/>
                  <Option value="collection" name="type" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
          <symbol force_rhr="0" is_animated="0" frame_rate="10" name="fillSymbol" clip_to_extent="1" type="fill" alpha="1">
            <data_defined_properties>
              <Option type="Map">
                <Option value="" name="name" type="QString"/>
                <Option name="properties"/>
                <Option value="collection" name="type" type="QString"/>
              </Option>
            </data_defined_properties>
            <layer locked="0" id="" class="SimpleFill" enabled="1" pass="0">
              <Option type="Map">
                <Option value="3x:0,0,0,0,0,0" name="border_width_map_unit_scale" type="QString"/>
                <Option value="255,255,255,255" name="color" type="QString"/>
                <Option value="bevel" name="joinstyle" type="QString"/>
                <Option value="0,0" name="offset" type="QString"/>
                <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
                <Option value="MM" name="offset_unit" type="QString"/>
                <Option value="128,128,128,255" name="outline_color" type="QString"/>
                <Option value="no" name="outline_style" type="QString"/>
                <Option value="0" name="outline_width" type="QString"/>
                <Option value="Point" name="outline_width_unit" type="QString"/>
                <Option value="solid" name="style" type="QString"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option value="" name="name" type="QString"/>
                  <Option name="properties"/>
                  <Option value="collection" name="type" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </background>
        <shadow shadowDraw="0" shadowColor="0,0,0,255" shadowOffsetUnit="MM" shadowRadiusAlphaOnly="0" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetGlobal="1" shadowRadius="1.5" shadowRadiusUnit="MM" shadowOpacity="0.69999999999999996" shadowScale="100" shadowOffsetAngle="135" shadowUnder="0" shadowBlendMode="6" shadowOffsetDist="1"/>
        <dd_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format wrapChar="" useMaxLineLengthForAutoWrap="1" rightDirectionSymbol=">" reverseDirectionSymbol="0" addDirectionSymbol="0" multilineAlign="3" decimals="3" placeDirectionSymbol="0" autoWrapLength="0" leftDirectionSymbol="&lt;" plussign="0" formatNumbers="0"/>
      <placement geometryGenerator="" maxCurvedCharAngleOut="-25" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" allowDegraded="0" xOffset="0" centroidWhole="0" distMapUnitScale="3x:0,0,0,0,0,0" centroidInside="0" fitInPolygonOnly="0" lineAnchorType="0" priority="5" rotationUnit="AngleDegrees" geometryGeneratorEnabled="0" placement="6" lineAnchorPercent="0.5" yOffset="0" offsetUnits="MM" lineAnchorTextPoint="FollowPlacement" maxCurvedCharAngleIn="25" preserveRotation="1" overrunDistance="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" dist="0" polygonPlacementFlags="2" lineAnchorClipping="0" overlapHandling="PreventOverlap" placementFlags="10" geometryGeneratorType="PointGeometry" quadOffset="4" layerType="PointGeometry" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" offsetType="1" repeatDistanceUnits="MM" rotationAngle="0" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" overrunDistanceUnit="MM" distUnits="MM" repeatDistance="0"/>
      <rendering scaleMin="0" limitNumLabels="0" scaleMax="0" unplacedVisibility="0" drawLabels="1" fontLimitPixelSize="0" obstacleFactor="1" scaleVisibility="0" labelPerPart="0" zIndex="0" minFeatureSize="0" mergeLines="0" obstacle="1" maxNumLabels="2000" fontMaxPixelSize="10000" obstacleType="1" fontMinPixelSize="3" upsidedownLabels="0"/>
      <dd_properties>
        <Option type="Map">
          <Option value="" name="name" type="QString"/>
          <Option name="properties"/>
          <Option value="collection" name="type" type="QString"/>
        </Option>
      </dd_properties>
      <callout type="simple">
        <Option type="Map">
          <Option value="pole_of_inaccessibility" name="anchorPoint" type="QString"/>
          <Option value="0" name="blendMode" type="int"/>
          <Option name="ddProperties" type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
          <Option value="false" name="drawToAllParts" type="bool"/>
          <Option value="0" name="enabled" type="QString"/>
          <Option value="point_on_exterior" name="labelAnchorPoint" type="QString"/>
          <Option value="&lt;symbol force_rhr=&quot;0&quot; is_animated=&quot;0&quot; frame_rate=&quot;10&quot; name=&quot;symbol&quot; clip_to_extent=&quot;1&quot; type=&quot;line&quot; alpha=&quot;1&quot;>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option value=&quot;&quot; name=&quot;name&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option value=&quot;collection&quot; name=&quot;type&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;layer locked=&quot;0&quot; id=&quot;{0d536ada-245d-40b3-af30-ab70122d7e39}&quot; class=&quot;SimpleLine&quot; enabled=&quot;1&quot; pass=&quot;0&quot;>&lt;Option type=&quot;Map&quot;>&lt;Option value=&quot;0&quot; name=&quot;align_dash_pattern&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;square&quot; name=&quot;capstyle&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;5;2&quot; name=&quot;customdash&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;customdash_map_unit_scale&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;MM&quot; name=&quot;customdash_unit&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;dash_pattern_offset&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;dash_pattern_offset_map_unit_scale&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;MM&quot; name=&quot;dash_pattern_offset_unit&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;draw_inside_polygon&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;bevel&quot; name=&quot;joinstyle&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;60,60,60,255&quot; name=&quot;line_color&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;solid&quot; name=&quot;line_style&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0.3&quot; name=&quot;line_width&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;MM&quot; name=&quot;line_width_unit&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;offset&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;offset_map_unit_scale&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;MM&quot; name=&quot;offset_unit&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;ring_filter&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;trim_distance_end&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;trim_distance_end_map_unit_scale&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;MM&quot; name=&quot;trim_distance_end_unit&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;trim_distance_start&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;trim_distance_start_map_unit_scale&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;MM&quot; name=&quot;trim_distance_start_unit&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;tweak_dash_pattern_on_corners&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;use_custom_dash&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;width_map_unit_scale&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option value=&quot;&quot; name=&quot;name&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option value=&quot;collection&quot; name=&quot;type&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" name="lineSymbol" type="QString"/>
          <Option value="0" name="minLength" type="double"/>
          <Option value="3x:0,0,0,0,0,0" name="minLengthMapUnitScale" type="QString"/>
          <Option value="MM" name="minLengthUnit" type="QString"/>
          <Option value="0" name="offsetFromAnchor" type="double"/>
          <Option value="3x:0,0,0,0,0,0" name="offsetFromAnchorMapUnitScale" type="QString"/>
          <Option value="MM" name="offsetFromAnchorUnit" type="QString"/>
          <Option value="0" name="offsetFromLabel" type="double"/>
          <Option value="3x:0,0,0,0,0,0" name="offsetFromLabelMapUnitScale" type="QString"/>
          <Option value="MM" name="offsetFromLabelUnit" type="QString"/>
        </Option>
      </callout>
    </settings>
  </labeling>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerGeometryType>0</layerGeometryType>
</qgis>
    '''

    document.setContent(f'{p1}{p2}{p3}')
    print(p2)
        
    return document

def wedgeLayerStyle():

    document = QDomDocument()
    
    styleXml ='''
    <!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyLocal="1" readOnly="0" simplifyDrawingTol="1" version="3.34.4-Prizren" simplifyDrawingHints="1" symbologyReferenceScale="-1" styleCategories="AllStyleCategories" hasScaleBasedVisibilityFlag="0" maxScale="0" minScale="100000000" labelsEnabled="1" simplifyAlgorithm="0" simplifyMaxScale="1">
<flags>
<Identifiable>1</Identifiable>
<Removable>1</Removable>
<Searchable>1</Searchable>
<Private>0</Private>
</flags>
<temporal endExpression="" durationField="" startField="" durationUnit="min" fixedDuration="0" accumulate="0" limitMode="0" mode="0" enabled="0" endField="" startExpression="">
<fixedRange>
    <start></start>
    <end></end>
</fixedRange>
</temporal>
<elevation showMarkerSymbolInSurfacePlots="0" zscale="1" symbology="Line" clamping="Terrain" type="IndividualFeatures" respectLayerSymbol="1" binding="Centroid" zoffset="0" extrusion="0" extrusionEnabled="0">
<data-defined-properties>
    <Option type="Map">
    <Option value="" name="name" type="QString"/>
    <Option name="properties"/>
    <Option value="collection" name="type" type="QString"/>
    </Option>
</data-defined-properties>
<profileLineSymbol>
    <symbol name="" clip_to_extent="1" frame_rate="10" type="line" alpha="1" is_animated="0" force_rhr="0">
    <data_defined_properties>
        <Option type="Map">
        <Option value="" name="name" type="QString"/>
        <Option name="properties"/>
        <Option value="collection" name="type" type="QString"/>
        </Option>
    </data_defined_properties>
    <layer id="{312120a8-8c79-4ee7-8eea-e404f10685a6}" pass="0" class="SimpleLine" locked="0" enabled="1">
        <Option type="Map">
        <Option value="0" name="align_dash_pattern" type="QString"/>
        <Option value="square" name="capstyle" type="QString"/>
        <Option value="5;2" name="customdash" type="QString"/>
        <Option value="3x:0,0,0,0,0,0" name="customdash_map_unit_scale" type="QString"/>
        <Option value="MM" name="customdash_unit" type="QString"/>
        <Option value="0" name="dash_pattern_offset" type="QString"/>
        <Option value="3x:0,0,0,0,0,0" name="dash_pattern_offset_map_unit_scale" type="QString"/>
        <Option value="MM" name="dash_pattern_offset_unit" type="QString"/>
        <Option value="0" name="draw_inside_polygon" type="QString"/>
        <Option value="bevel" name="joinstyle" type="QString"/>
        <Option value="145,82,45,255" name="line_color" type="QString"/>
        <Option value="solid" name="line_style" type="QString"/>
        <Option value="0.6" name="line_width" type="QString"/>
        <Option value="MM" name="line_width_unit" type="QString"/>
        <Option value="0" name="offset" type="QString"/>
        <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
        <Option value="MM" name="offset_unit" type="QString"/>
        <Option value="0" name="ring_filter" type="QString"/>
        <Option value="0" name="trim_distance_end" type="QString"/>
        <Option value="3x:0,0,0,0,0,0" name="trim_distance_end_map_unit_scale" type="QString"/>
        <Option value="MM" name="trim_distance_end_unit" type="QString"/>
        <Option value="0" name="trim_distance_start" type="QString"/>
        <Option value="3x:0,0,0,0,0,0" name="trim_distance_start_map_unit_scale" type="QString"/>
        <Option value="MM" name="trim_distance_start_unit" type="QString"/>
        <Option value="0" name="tweak_dash_pattern_on_corners" type="QString"/>
        <Option value="0" name="use_custom_dash" type="QString"/>
        <Option value="3x:0,0,0,0,0,0" name="width_map_unit_scale" type="QString"/>
        </Option>
        <data_defined_properties>
        <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
        </Option>
        </data_defined_properties>
    </layer>
    </symbol>
</profileLineSymbol>
<profileFillSymbol>
    <symbol name="" clip_to_extent="1" frame_rate="10" type="fill" alpha="1" is_animated="0" force_rhr="0">
    <data_defined_properties>
        <Option type="Map">
        <Option value="" name="name" type="QString"/>
        <Option name="properties"/>
        <Option value="collection" name="type" type="QString"/>
        </Option>
    </data_defined_properties>
    <layer id="{121d0e51-3311-48e9-a862-f7ae3d8f0c90}" pass="0" class="SimpleFill" locked="0" enabled="1">
        <Option type="Map">
        <Option value="3x:0,0,0,0,0,0" name="border_width_map_unit_scale" type="QString"/>
        <Option value="145,82,45,255" name="color" type="QString"/>
        <Option value="bevel" name="joinstyle" type="QString"/>
        <Option value="0,0" name="offset" type="QString"/>
        <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
        <Option value="MM" name="offset_unit" type="QString"/>
        <Option value="104,59,32,255" name="outline_color" type="QString"/>
        <Option value="solid" name="outline_style" type="QString"/>
        <Option value="0.2" name="outline_width" type="QString"/>
        <Option value="MM" name="outline_width_unit" type="QString"/>
        <Option value="solid" name="style" type="QString"/>
        </Option>
        <data_defined_properties>
        <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
        </Option>
        </data_defined_properties>
    </layer>
    </symbol>
</profileFillSymbol>
<profileMarkerSymbol>
    <symbol name="" clip_to_extent="1" frame_rate="10" type="marker" alpha="1" is_animated="0" force_rhr="0">
    <data_defined_properties>
        <Option type="Map">
        <Option value="" name="name" type="QString"/>
        <Option name="properties"/>
        <Option value="collection" name="type" type="QString"/>
        </Option>
    </data_defined_properties>
    <layer id="{0a1316bc-d2c2-48ab-aa94-e9aa3df96c42}" pass="0" class="SimpleMarker" locked="0" enabled="1">
        <Option type="Map">
        <Option value="0" name="angle" type="QString"/>
        <Option value="square" name="cap_style" type="QString"/>
        <Option value="145,82,45,255" name="color" type="QString"/>
        <Option value="1" name="horizontal_anchor_point" type="QString"/>
        <Option value="bevel" name="joinstyle" type="QString"/>
        <Option value="diamond" name="name" type="QString"/>
        <Option value="0,0" name="offset" type="QString"/>
        <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
        <Option value="MM" name="offset_unit" type="QString"/>
        <Option value="104,59,32,255" name="outline_color" type="QString"/>
        <Option value="solid" name="outline_style" type="QString"/>
        <Option value="0.2" name="outline_width" type="QString"/>
        <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
        <Option value="MM" name="outline_width_unit" type="QString"/>
        <Option value="diameter" name="scale_method" type="QString"/>
        <Option value="3" name="size" type="QString"/>
        <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
        <Option value="MM" name="size_unit" type="QString"/>
        <Option value="1" name="vertical_anchor_point" type="QString"/>
        </Option>
        <data_defined_properties>
        <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
        </Option>
        </data_defined_properties>
    </layer>
    </symbol>
</profileMarkerSymbol>
</elevation>
<renderer-v2 enableorderby="0" type="singleSymbol" forceraster="0" referencescale="-1" symbollevels="0">
<symbols>
    <symbol name="0" clip_to_extent="1" frame_rate="10" type="fill" alpha="1" is_animated="0" force_rhr="0">
    <data_defined_properties>
        <Option type="Map">
        <Option value="" name="name" type="QString"/>
        <Option name="properties"/>
        <Option value="collection" name="type" type="QString"/>
        </Option>
    </data_defined_properties>
    <layer id="{0422a3b9-8469-4fdf-b250-51c9a4ec9640}" pass="0" class="PointPatternFill" locked="0" enabled="1">
        <Option type="Map">
        <Option value="0" name="angle" type="double"/>
        <Option value="shape" name="clip_mode" type="QString"/>
        <Option value="feature" name="coordinate_reference" type="QString"/>
        <Option value="1.2" name="displacement_x" type="QString"/>
        <Option value="3x:0,0,0,0,0,0" name="displacement_x_map_unit_scale" type="QString"/>
        <Option value="Point" name="displacement_x_unit" type="QString"/>
        <Option value="0" name="displacement_y" type="QString"/>
        <Option value="3x:0,0,0,0,0,0" name="displacement_y_map_unit_scale" type="QString"/>
        <Option value="Point" name="displacement_y_unit" type="QString"/>
        <Option value="5" name="distance_x" type="QString"/>
        <Option value="3x:0,0,0,0,0,0" name="distance_x_map_unit_scale" type="QString"/>
        <Option value="Point" name="distance_x_unit" type="QString"/>
        <Option value="5" name="distance_y" type="QString"/>
        <Option value="3x:0,0,0,0,0,0" name="distance_y_map_unit_scale" type="QString"/>
        <Option value="Point" name="distance_y_unit" type="QString"/>
        <Option value="0" name="offset_x" type="QString"/>
        <Option value="3x:0,0,0,0,0,0" name="offset_x_map_unit_scale" type="QString"/>
        <Option value="Point" name="offset_x_unit" type="QString"/>
        <Option value="0" name="offset_y" type="QString"/>
        <Option value="3x:0,0,0,0,0,0" name="offset_y_map_unit_scale" type="QString"/>
        <Option value="Point" name="offset_y_unit" type="QString"/>
        <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
        <Option value="Point" name="outline_width_unit" type="QString"/>
        <Option value="0" name="random_deviation_x" type="QString"/>
        <Option value="3x:0,0,0,0,0,0" name="random_deviation_x_map_unit_scale" type="QString"/>
        <Option value="Point" name="random_deviation_x_unit" type="QString"/>
        <Option value="0" name="random_deviation_y" type="QString"/>
        <Option value="3x:0,0,0,0,0,0" name="random_deviation_y_map_unit_scale" type="QString"/>
        <Option value="Point" name="random_deviation_y_unit" type="QString"/>
        <Option value="301756345" name="seed" type="QString"/>
        </Option>
        <data_defined_properties>
        <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
        </Option>
        </data_defined_properties>
        <symbol name="@0@0" clip_to_extent="1" frame_rate="10" type="marker" alpha="1" is_animated="0" force_rhr="0">
        <data_defined_properties>
            <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
            </Option>
        </data_defined_properties>
        <layer id="{7fab0b45-e402-43e0-b699-387f594e7592}" pass="0" class="SimpleMarker" locked="0" enabled="1">
            <Option type="Map">
            <Option value="0" name="angle" type="QString"/>
            <Option value="square" name="cap_style" type="QString"/>
            <Option value="0,0,0,163" name="color" type="QString"/>
            <Option value="1" name="horizontal_anchor_point" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="circle" name="name" type="QString"/>
            <Option value="0,0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="Point" name="offset_unit" type="QString"/>
            <Option value="0,0,0,255" name="outline_color" type="QString"/>
            <Option value="solid" name="outline_style" type="QString"/>
            <Option value="0.2" name="outline_width" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
            <Option value="Point" name="outline_width_unit" type="QString"/>
            <Option value="diameter" name="scale_method" type="QString"/>
            <Option value="1" name="size" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
            <Option value="Point" name="size_unit" type="QString"/>
            <Option value="1" name="vertical_anchor_point" type="QString"/>
            </Option>
            <data_defined_properties>
            <Option type="Map">
                <Option value="" name="name" type="QString"/>
                <Option name="properties"/>
                <Option value="collection" name="type" type="QString"/>
            </Option>
            </data_defined_properties>
        </layer>
        </symbol>
    </layer>
    <layer id="{68142315-d699-4b5e-859b-eb2007f9f98a}" pass="0" class="SimpleLine" locked="0" enabled="1">
        <Option type="Map">
        <Option value="1" name="align_dash_pattern" type="QString"/>
        <Option value="square" name="capstyle" type="QString"/>
        <Option value="5;5" name="customdash" type="QString"/>
        <Option value="3x:0,0,0,0,0,0" name="customdash_map_unit_scale" type="QString"/>
        <Option value="Point" name="customdash_unit" type="QString"/>
        <Option value="0" name="dash_pattern_offset" type="QString"/>
        <Option value="3x:0,0,0,0,0,0" name="dash_pattern_offset_map_unit_scale" type="QString"/>
        <Option value="Point" name="dash_pattern_offset_unit" type="QString"/>
        <Option value="0" name="draw_inside_polygon" type="QString"/>
        <Option value="bevel" name="joinstyle" type="QString"/>
        <Option value="0,0,0,163" name="line_color" type="QString"/>
        <Option value="dash" name="line_style" type="QString"/>
        <Option value="1" name="line_width" type="QString"/>
        <Option value="Point" name="line_width_unit" type="QString"/>
        <Option value="0" name="offset" type="QString"/>
        <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
        <Option value="Point" name="offset_unit" type="QString"/>
        <Option value="0" name="ring_filter" type="QString"/>
        <Option value="0" name="trim_distance_end" type="QString"/>
        <Option value="3x:0,0,0,0,0,0" name="trim_distance_end_map_unit_scale" type="QString"/>
        <Option value="Point" name="trim_distance_end_unit" type="QString"/>
        <Option value="0" name="trim_distance_start" type="QString"/>
        <Option value="3x:0,0,0,0,0,0" name="trim_distance_start_map_unit_scale" type="QString"/>
        <Option value="Point" name="trim_distance_start_unit" type="QString"/>
        <Option value="1" name="tweak_dash_pattern_on_corners" type="QString"/>
        <Option value="1" name="use_custom_dash" type="QString"/>
        <Option value="3x:0,0,0,0,0,0" name="width_map_unit_scale" type="QString"/>
        </Option>
        <data_defined_properties>
        <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
        </Option>
        </data_defined_properties>
    </layer>
    <layer id="{2790303b-4dc1-464b-9536-4d24aeacea9f}" pass="0" class="GeometryGenerator" locked="0" enabled="1">
        <Option type="Map">
        <Option value="Marker" name="SymbolType" type="QString"/>
        <Option value=" geom_from_wkt(&quot;startPoint&quot;)" name="geometryModifier" type="QString"/>
        <Option value="MapUnit" name="units" type="QString"/>
        </Option>
        <data_defined_properties>
        <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
        </Option>
        </data_defined_properties>
        <symbol name="@0@2" clip_to_extent="1" frame_rate="10" type="marker" alpha="1" is_animated="0" force_rhr="0">
        <data_defined_properties>
            <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
            </Option>
        </data_defined_properties>
        <layer id="{7b1325ff-3f90-4842-8ace-cc593fb99f40}" pass="0" class="SimpleMarker" locked="0" enabled="1">
            <Option type="Map">
            <Option value="0" name="angle" type="QString"/>
            <Option value="square" name="cap_style" type="QString"/>
            <Option value="255,0,0,255" name="color" type="QString"/>
            <Option value="1" name="horizontal_anchor_point" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="circle" name="name" type="QString"/>
            <Option value="0,0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="Point" name="offset_unit" type="QString"/>
            <Option value="35,35,35,255" name="outline_color" type="QString"/>
            <Option value="solid" name="outline_style" type="QString"/>
            <Option value="0" name="outline_width" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
            <Option value="Point" name="outline_width_unit" type="QString"/>
            <Option value="diameter" name="scale_method" type="QString"/>
            <Option value="5" name="size" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
            <Option value="Point" name="size_unit" type="QString"/>
            <Option value="1" name="vertical_anchor_point" type="QString"/>
            </Option>
            <data_defined_properties>
            <Option type="Map">
                <Option value="" name="name" type="QString"/>
                <Option name="properties"/>
                <Option value="collection" name="type" type="QString"/>
            </Option>
            </data_defined_properties>
        </layer>
        </symbol>
    </layer>
    </symbol>
</symbols>
<rotation/>
<sizescale/>
</renderer-v2>
<selection mode="Default">
<selectionColor invalid="1"/>
<selectionSymbol>
    <symbol name="" clip_to_extent="1" frame_rate="10" type="fill" alpha="1" is_animated="0" force_rhr="0">
    <data_defined_properties>
        <Option type="Map">
        <Option value="" name="name" type="QString"/>
        <Option name="properties"/>
        <Option value="collection" name="type" type="QString"/>
        </Option>
    </data_defined_properties>
    <layer id="{d1c6af7a-75e8-4ec3-923f-0550f60c7aca}" pass="0" class="SimpleFill" locked="0" enabled="1">
        <Option type="Map">
        <Option value="3x:0,0,0,0,0,0" name="border_width_map_unit_scale" type="QString"/>
        <Option value="0,0,255,255" name="color" type="QString"/>
        <Option value="bevel" name="joinstyle" type="QString"/>
        <Option value="0,0" name="offset" type="QString"/>
        <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
        <Option value="MM" name="offset_unit" type="QString"/>
        <Option value="35,35,35,255" name="outline_color" type="QString"/>
        <Option value="solid" name="outline_style" type="QString"/>
        <Option value="0.26" name="outline_width" type="QString"/>
        <Option value="MM" name="outline_width_unit" type="QString"/>
        <Option value="solid" name="style" type="QString"/>
        </Option>
        <data_defined_properties>
        <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
        </Option>
        </data_defined_properties>
    </layer>
    </symbol>
</selectionSymbol>
</selection>
<labeling type="simple">
<settings calloutType="curved">
    <text-style blendMode="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" useSubstitutions="0" fontFamily="Open Sans" multilineHeightUnit="Percentage" multilineHeight="1" fontItalic="0" forcedBold="0" allowHtml="0" capitalization="0" fontWeight="50" legendString="Aa" fontKerning="1" isExpression="1" textColor="50,50,50,255" textOpacity="1" textOrientation="horizontal" fontStrikeout="0" fontSizeUnit="Point" fontUnderline="0" forcedItalic="0" fontSize="12" fieldName="'Uppskattad brandspridning kl: ' || &quot;frontFireTime&quot;" fontLetterSpacing="0" previewBkgrdColor="255,255,255,255" namedStyle="Regular" fontWordSpacing="0">
    <families/>
    <text-buffer bufferOpacity="1" bufferSizeUnits="MM" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferNoFill="1" bufferSize="1" bufferDraw="1" bufferBlendMode="0" bufferColor="250,250,250,255" bufferJoinStyle="128"/>
    <text-mask maskedSymbolLayers="" maskJoinStyle="128" maskOpacity="1" maskSizeUnits="MM" maskSizeMapUnitScale="3x:0,0,0,0,0,0" maskEnabled="1" maskSize="0" maskType="0"/>
    <background shapeOffsetY="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeBorderColor="128,128,128,255" shapeSizeY="0" shapeRotationType="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeSizeType="0" shapeSVGFile="" shapeFillColor="255,255,255,255" shapeSizeX="0" shapeType="0" shapeRadiiX="0" shapeBorderWidth="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiUnit="Point" shapeRadiiY="0" shapeSizeUnit="Point" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetUnit="Point" shapeBorderWidthUnit="Point" shapeRotation="0" shapeDraw="0" shapeBlendMode="0" shapeOffsetX="0" shapeJoinStyle="64" shapeOpacity="1">
        <symbol name="markerSymbol" clip_to_extent="1" frame_rate="10" type="marker" alpha="1" is_animated="0" force_rhr="0">
        <data_defined_properties>
            <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
            </Option>
        </data_defined_properties>
        <layer id="" pass="0" class="SimpleMarker" locked="0" enabled="1">
            <Option type="Map">
            <Option value="0" name="angle" type="QString"/>
            <Option value="square" name="cap_style" type="QString"/>
            <Option value="190,207,80,255" name="color" type="QString"/>
            <Option value="1" name="horizontal_anchor_point" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="circle" name="name" type="QString"/>
            <Option value="0,0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="35,35,35,255" name="outline_color" type="QString"/>
            <Option value="solid" name="outline_style" type="QString"/>
            <Option value="0" name="outline_width" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
            <Option value="MM" name="outline_width_unit" type="QString"/>
            <Option value="diameter" name="scale_method" type="QString"/>
            <Option value="2" name="size" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
            <Option value="MM" name="size_unit" type="QString"/>
            <Option value="1" name="vertical_anchor_point" type="QString"/>
            </Option>
            <data_defined_properties>
            <Option type="Map">
                <Option value="" name="name" type="QString"/>
                <Option name="properties"/>
                <Option value="collection" name="type" type="QString"/>
            </Option>
            </data_defined_properties>
        </layer>
        </symbol>
        <symbol name="fillSymbol" clip_to_extent="1" frame_rate="10" type="fill" alpha="1" is_animated="0" force_rhr="0">
        <data_defined_properties>
            <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
            </Option>
        </data_defined_properties>
        <layer id="" pass="0" class="SimpleFill" locked="0" enabled="1">
            <Option type="Map">
            <Option value="3x:0,0,0,0,0,0" name="border_width_map_unit_scale" type="QString"/>
            <Option value="255,255,255,255" name="color" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="0,0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="128,128,128,255" name="outline_color" type="QString"/>
            <Option value="no" name="outline_style" type="QString"/>
            <Option value="0" name="outline_width" type="QString"/>
            <Option value="Point" name="outline_width_unit" type="QString"/>
            <Option value="solid" name="style" type="QString"/>
            </Option>
            <data_defined_properties>
            <Option type="Map">
                <Option value="" name="name" type="QString"/>
                <Option name="properties"/>
                <Option value="collection" name="type" type="QString"/>
            </Option>
            </data_defined_properties>
        </layer>
        </symbol>
    </background>
    <shadow shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowUnder="0" shadowOffsetAngle="135" shadowBlendMode="6" shadowOffsetDist="1" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusAlphaOnly="0" shadowOpacity="0.69999999999999996" shadowColor="0,0,0,255" shadowRadius="1.5" shadowRadiusUnit="MM" shadowScale="100" shadowOffsetUnit="MM" shadowDraw="0" shadowOffsetGlobal="1"/>
    <dd_properties>
        <Option type="Map">
        <Option value="" name="name" type="QString"/>
        <Option name="properties"/>
        <Option value="collection" name="type" type="QString"/>
        </Option>
    </dd_properties>
    <substitutions/>
    </text-style>
    <text-format multilineAlign="3" formatNumbers="0" reverseDirectionSymbol="0" useMaxLineLengthForAutoWrap="1" placeDirectionSymbol="0" addDirectionSymbol="0" plussign="0" leftDirectionSymbol="&lt;" wrapChar="" rightDirectionSymbol=">" autoWrapLength="0" decimals="3"/>
    <placement labelOffsetMapUnitScale="3x:0,0,0,0,0,0" rotationAngle="0" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" lineAnchorTextPoint="FollowPlacement" maxCurvedCharAngleIn="25" offsetType="0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" geometryGeneratorType="PointGeometry" offsetUnits="MM" geometryGeneratorEnabled="0" geometryGenerator="" priority="5" distMapUnitScale="3x:0,0,0,0,0,0" overlapHandling="PreventOverlap" overrunDistanceUnit="MM" yOffset="0" distUnits="MM" polygonPlacementFlags="2" overrunDistance="0" rotationUnit="AngleDegrees" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" layerType="PolygonGeometry" dist="3" quadOffset="4" xOffset="0" lineAnchorClipping="0" preserveRotation="1" repeatDistance="0" allowDegraded="0" fitInPolygonOnly="0" lineAnchorPercent="0.5" placement="7" maxCurvedCharAngleOut="-25" centroidInside="0" placementFlags="9" centroidWhole="0" repeatDistanceUnits="MM" lineAnchorType="0"/>
    <rendering labelPerPart="0" minFeatureSize="0" limitNumLabels="0" fontMinPixelSize="3" obstacle="0" zIndex="0" obstacleType="1" mergeLines="0" unplacedVisibility="0" scaleMax="0" obstacleFactor="1" maxNumLabels="2000" scaleMin="0" scaleVisibility="0" fontMaxPixelSize="10000" upsidedownLabels="0" drawLabels="1" fontLimitPixelSize="0"/>
    <dd_properties>
    <Option type="Map">
        <Option value="" name="name" type="QString"/>
        <Option name="properties"/>
        <Option value="collection" name="type" type="QString"/>
    </Option>
    </dd_properties>
    <callout type="curved">
    <Option type="Map">
        <Option value="pole_of_inaccessibility" name="anchorPoint" type="QString"/>
        <Option value="0" name="blendMode" type="int"/>
        <Option value="0.1" name="curvature" type="double"/>
        <Option name="ddProperties" type="Map">
        <Option value="" name="name" type="QString"/>
        <Option name="properties"/>
        <Option value="collection" name="type" type="QString"/>
        </Option>
        <Option value="false" name="drawToAllParts" type="bool"/>
        <Option value="0" name="enabled" type="QString"/>
        <Option value="point_on_exterior" name="labelAnchorPoint" type="QString"/>
        <Option value="&lt;symbol name=&quot;symbol&quot; clip_to_extent=&quot;1&quot; frame_rate=&quot;10&quot; type=&quot;line&quot; alpha=&quot;1&quot; is_animated=&quot;0&quot; force_rhr=&quot;0&quot;>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option value=&quot;&quot; name=&quot;name&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option value=&quot;collection&quot; name=&quot;type&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;layer id=&quot;{b76d8884-79eb-475d-b291-d7b07b940843}&quot; pass=&quot;0&quot; class=&quot;SimpleLine&quot; locked=&quot;0&quot; enabled=&quot;1&quot;>&lt;Option type=&quot;Map&quot;>&lt;Option value=&quot;0&quot; name=&quot;align_dash_pattern&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;square&quot; name=&quot;capstyle&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;5;2&quot; name=&quot;customdash&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;customdash_map_unit_scale&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;MM&quot; name=&quot;customdash_unit&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;dash_pattern_offset&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;dash_pattern_offset_map_unit_scale&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;MM&quot; name=&quot;dash_pattern_offset_unit&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;draw_inside_polygon&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;bevel&quot; name=&quot;joinstyle&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;60,60,60,255&quot; name=&quot;line_color&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;solid&quot; name=&quot;line_style&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0.3&quot; name=&quot;line_width&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;MM&quot; name=&quot;line_width_unit&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;offset&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;offset_map_unit_scale&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;MM&quot; name=&quot;offset_unit&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;ring_filter&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;trim_distance_end&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;trim_distance_end_map_unit_scale&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;MM&quot; name=&quot;trim_distance_end_unit&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;trim_distance_start&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;trim_distance_start_map_unit_scale&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;MM&quot; name=&quot;trim_distance_start_unit&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;tweak_dash_pattern_on_corners&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;use_custom_dash&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;width_map_unit_scale&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option value=&quot;&quot; name=&quot;name&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option value=&quot;collection&quot; name=&quot;type&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" name="lineSymbol" type="QString"/>
        <Option value="0" name="minLength" type="double"/>
        <Option value="3x:0,0,0,0,0,0" name="minLengthMapUnitScale" type="QString"/>
        <Option value="MM" name="minLengthUnit" type="QString"/>
        <Option value="0" name="offsetFromAnchor" type="double"/>
        <Option value="3x:0,0,0,0,0,0" name="offsetFromAnchorMapUnitScale" type="QString"/>
        <Option value="MM" name="offsetFromAnchorUnit" type="QString"/>
        <Option value="0" name="offsetFromLabel" type="double"/>
        <Option value="3x:0,0,0,0,0,0" name="offsetFromLabelMapUnitScale" type="QString"/>
        <Option value="MM" name="offsetFromLabelUnit" type="QString"/>
        <Option value="auto" name="orientation" type="QString"/>
    </Option>
    </callout>
</settings>
</labeling>
<customproperties>
<Option type="Map">
    <Option name="dualview/previewExpressions" type="List">
    <Option value="&quot;frontFireTime&quot;" type="QString"/>
    </Option>
    <Option value="0" name="embeddedWidgets/count" type="int"/>
    <Option name="variableNames"/>
    <Option name="variableValues"/>
</Option>
</customproperties>
<blendMode>0</blendMode>
<featureBlendMode>0</featureBlendMode>
<layerOpacity>1</layerOpacity>
<SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
<DiagramCategory backgroundAlpha="255" scaleBasedVisibility="0" spacing="5" lineSizeScale="3x:0,0,0,0,0,0" height="15" spacingUnit="MM" maxScaleDenominator="1e+08" showAxis="1" scaleDependency="Area" enabled="0" spacingUnitScale="3x:0,0,0,0,0,0" minimumSize="0" penAlpha="255" rotationOffset="270" lineSizeType="MM" width="15" backgroundColor="#ffffff" penColor="#000000" minScaleDenominator="0" opacity="1" direction="0" penWidth="0" diagramOrientation="Up" sizeType="MM" barWidth="5" sizeScale="3x:0,0,0,0,0,0" labelPlacementMethod="XHeight">
    <fontProperties italic="0" description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" strikethrough="0" bold="0" style="" underline="0"/>
    <attribute label="" field="" colorOpacity="1" color="#000000"/>
    <axisSymbol>
    <symbol name="" clip_to_extent="1" frame_rate="10" type="line" alpha="1" is_animated="0" force_rhr="0">
        <data_defined_properties>
        <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
        </Option>
        </data_defined_properties>
        <layer id="{6ba6c277-60cb-4fd4-8c3c-9d92a252e687}" pass="0" class="SimpleLine" locked="0" enabled="1">
        <Option type="Map">
            <Option value="0" name="align_dash_pattern" type="QString"/>
            <Option value="square" name="capstyle" type="QString"/>
            <Option value="5;2" name="customdash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="customdash_map_unit_scale" type="QString"/>
            <Option value="MM" name="customdash_unit" type="QString"/>
            <Option value="0" name="dash_pattern_offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="dash_pattern_offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="dash_pattern_offset_unit" type="QString"/>
            <Option value="0" name="draw_inside_polygon" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="35,35,35,255" name="line_color" type="QString"/>
            <Option value="solid" name="line_style" type="QString"/>
            <Option value="0.26" name="line_width" type="QString"/>
            <Option value="MM" name="line_width_unit" type="QString"/>
            <Option value="0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="0" name="ring_filter" type="QString"/>
            <Option value="0" name="trim_distance_end" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_end_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_end_unit" type="QString"/>
            <Option value="0" name="trim_distance_start" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_start_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_start_unit" type="QString"/>
            <Option value="0" name="tweak_dash_pattern_on_corners" type="QString"/>
            <Option value="0" name="use_custom_dash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="width_map_unit_scale" type="QString"/>
        </Option>
        <data_defined_properties>
            <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
            </Option>
        </data_defined_properties>
        </layer>
    </symbol>
    </axisSymbol>
</DiagramCategory>
</SingleCategoryDiagramRenderer>
<DiagramLayerSettings showAll="1" placement="1" obstacle="0" priority="0" dist="0" linePlacementFlags="18" zIndex="0">
<properties>
    <Option type="Map">
    <Option value="" name="name" type="QString"/>
    <Option name="properties"/>
    <Option value="collection" name="type" type="QString"/>
    </Option>
</properties>
</DiagramLayerSettings>
<geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
<activeChecks/>
<checkConfiguration type="Map">
    <Option name="QgsGeometryGapCheck" type="Map">
    <Option value="0" name="allowedGapsBuffer" type="double"/>
    <Option value="false" name="allowedGapsEnabled" type="bool"/>
    <Option value="" name="allowedGapsLayer" type="QString"/>
    </Option>
</checkConfiguration>
</geometryOptions>
<legend type="default-vector" showLabelLegend="0"/>
<referencedLayers/>
<fieldConfiguration>
<field name="text" configurationFlags="NoFlag">
    <editWidget type="TextEdit">
    <config>
        <Option/>
    </config>
    </editWidget>
</field>
<field name="spridning längd" configurationFlags="NoFlag">
    <editWidget type="TextEdit">
    <config>
        <Option/>
    </config>
    </editWidget>
</field>
<field name="frontFireTime" configurationFlags="NoFlag">
    <editWidget type="TextEdit">
    <config>
        <Option/>
    </config>
    </editWidget>
</field>
<field name="createTime" configurationFlags="NoFlag">
    <editWidget type="TextEdit">
    <config>
        <Option/>
    </config>
    </editWidget>
</field>
<field name="startPoint" configurationFlags="NoFlag">
    <editWidget type="TextEdit">
    <config>
        <Option/>
    </config>
    </editWidget>
</field>
</fieldConfiguration>
<aliases>
<alias name="" field="text" index="0"/>
<alias name="" field="spridning längd" index="1"/>
<alias name="" field="frontFireTime" index="2"/>
<alias name="" field="createTime" index="3"/>
<alias name="" field="startPoint" index="4"/>
</aliases>
<splitPolicies>
<policy field="text" policy="Duplicate"/>
<policy field="spridning längd" policy="Duplicate"/>
<policy field="frontFireTime" policy="Duplicate"/>
<policy field="createTime" policy="Duplicate"/>
<policy field="startPoint" policy="Duplicate"/>
</splitPolicies>
<defaults>
<default field="text" expression="" applyOnUpdate="0"/>
<default field="spridning längd" expression="" applyOnUpdate="0"/>
<default field="frontFireTime" expression="" applyOnUpdate="0"/>
<default field="createTime" expression="" applyOnUpdate="0"/>
<default field="startPoint" expression="" applyOnUpdate="0"/>
</defaults>
<constraints>
<constraint constraints="0" notnull_strength="0" field="text" exp_strength="0" unique_strength="0"/>
<constraint constraints="0" notnull_strength="0" field="spridning längd" exp_strength="0" unique_strength="0"/>
<constraint constraints="0" notnull_strength="0" field="frontFireTime" exp_strength="0" unique_strength="0"/>
<constraint constraints="0" notnull_strength="0" field="createTime" exp_strength="0" unique_strength="0"/>
<constraint constraints="0" notnull_strength="0" field="startPoint" exp_strength="0" unique_strength="0"/>
</constraints>
<constraintExpressions>
<constraint exp="" field="text" desc=""/>
<constraint exp="" field="spridning längd" desc=""/>
<constraint exp="" field="frontFireTime" desc=""/>
<constraint exp="" field="createTime" desc=""/>
<constraint exp="" field="startPoint" desc=""/>
</constraintExpressions>
<expressionfields/>
<attributeactions>
<defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
</attributeactions>
<attributetableconfig sortExpression="" actionWidgetStyle="dropDown" sortOrder="0">
<columns>
    <column name="frontFireTime" type="field" hidden="0" width="-1"/>
    <column name="createTime" type="field" hidden="0" width="-1"/>
    <column name="startPoint" type="field" hidden="0" width="-1"/>
    <column name="text" type="field" hidden="0" width="-1"/>
    <column name="spridning längd" type="field" hidden="0" width="-1"/>
    <column type="actions" hidden="1" width="-1"/>
</columns>
</attributetableconfig>
<conditionalstyles>
<rowstyles/>
<fieldstyles/>
</conditionalstyles>
<storedexpressions/>
<editform tolerant="1"></editform>
<editforminit/>
<editforminitcodesource>0</editforminitcodesource>
<editforminitfilepath></editforminitfilepath>
<editforminitcode><![CDATA[# -*- coding: utf-8 -*-
                """
                QGIS formulär kan ha en Pythonfunktion som anropas när formuläret öppnas.

                Använd denna funktion för att lägga till extra logik till dina formulär.

                Skriv in namnet på funktionen i fältet "Python Init function".
                Ett exempel nedan:
                """
                from qgis.PyQt.QtWidgets import QWidget

                def my_form_open(dialog, layer, feature):
                    geom = feature.geometry()
                    control = dialog.findChild(QWidget, "MyLineEdit")
                ]]></editforminitcode>
<featformsuppress>0</featformsuppress>
<editorlayout>generatedlayout</editorlayout>
<editable>
<field name="Text" editable="1"/>
<field name="createTime" editable="1"/>
<field name="frontFireTime" editable="1"/>
<field name="spridning längd" editable="1"/>
<field name="startPoint" editable="1"/>
<field name="text" editable="1"/>
</editable>
<labelOnTop>
<field name="Text" labelOnTop="0"/>
<field name="createTime" labelOnTop="0"/>
<field name="frontFireTime" labelOnTop="0"/>
<field name="spridning längd" labelOnTop="0"/>
<field name="startPoint" labelOnTop="0"/>
<field name="text" labelOnTop="0"/>
</labelOnTop>
<reuseLastValue>
<field name="Text" reuseLastValue="0"/>
<field name="createTime" reuseLastValue="0"/>
<field name="frontFireTime" reuseLastValue="0"/>
<field name="spridning längd" reuseLastValue="0"/>
<field name="startPoint" reuseLastValue="0"/>
<field name="text" reuseLastValue="0"/>
</reuseLastValue>
<dataDefinedFieldProperties/>
<widgets/>
<previewExpression>"frontFireTime"</previewExpression>
<mapTip enabled="1"></mapTip>
<layerGeometryType>2</layerGeometryType>
</qgis>

'''
    document.setContent(styleXml)
        
    return document