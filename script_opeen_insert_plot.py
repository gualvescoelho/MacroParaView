# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active source.
duto3mOpenFOAM = GetActiveSource()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
duto3mOpenFOAMDisplay = Show(duto3mOpenFOAM, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
duto3mOpenFOAMDisplay.Representation = 'Surface'
duto3mOpenFOAMDisplay.ColorArrayName = [None, '']
duto3mOpenFOAMDisplay.SelectTCoordArray = 'None'
duto3mOpenFOAMDisplay.SelectNormalArray = 'None'
duto3mOpenFOAMDisplay.SelectTangentArray = 'None'
duto3mOpenFOAMDisplay.OSPRayScaleArray = 'U'
duto3mOpenFOAMDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
duto3mOpenFOAMDisplay.SelectOrientationVectors = 'None'
duto3mOpenFOAMDisplay.ScaleFactor = 0.30000000000000004
duto3mOpenFOAMDisplay.SelectScaleArray = 'None'
duto3mOpenFOAMDisplay.GlyphType = 'Arrow'
duto3mOpenFOAMDisplay.GlyphTableIndexArray = 'None'
duto3mOpenFOAMDisplay.GaussianRadius = 0.015
duto3mOpenFOAMDisplay.SetScaleArray = ['POINTS', 'U']
duto3mOpenFOAMDisplay.ScaleTransferFunction = 'PiecewiseFunction'
duto3mOpenFOAMDisplay.OpacityArray = ['POINTS', 'U']
duto3mOpenFOAMDisplay.OpacityTransferFunction = 'PiecewiseFunction'
duto3mOpenFOAMDisplay.DataAxesGrid = 'GridAxesRepresentation'
duto3mOpenFOAMDisplay.PolarAxes = 'PolarAxesRepresentation'

# reset view to fit data
renderView1.ResetCamera(False)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(duto3mOpenFOAMDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
duto3mOpenFOAMDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')

# set scalar coloring
ColorBy(duto3mOpenFOAMDisplay, ('POINTS', 'U', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
duto3mOpenFOAMDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
duto3mOpenFOAMDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')

# get opacity transfer function/opacity map for 'U'
uPWF = GetOpacityTransferFunction('U')

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(registrationName='PlotOverLine1', Input=duto3mOpenFOAM)
plotOverLine1.Point2 = [3.0, 0.10000000149011612, 0.009999999776482582]

# Properties modified on plotOverLine1
plotOverLine1.Point1 = [1.5, 0.0, 0.004999999888241291]
plotOverLine1.Point2 = [1.5, 0.10000000149011612, 0.004999999888241291]

# show data in view
plotOverLine1Display = Show(plotOverLine1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plotOverLine1Display.Representation = 'Surface'
plotOverLine1Display.ColorArrayName = ['POINTS', 'U']
plotOverLine1Display.LookupTable = uLUT
plotOverLine1Display.SelectTCoordArray = 'None'
plotOverLine1Display.SelectNormalArray = 'None'
plotOverLine1Display.SelectTangentArray = 'None'
plotOverLine1Display.OSPRayScaleArray = 'U'
plotOverLine1Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1Display.SelectOrientationVectors = 'None'
plotOverLine1Display.ScaleFactor = 0.010000000149011612
plotOverLine1Display.SelectScaleArray = 'None'
plotOverLine1Display.GlyphType = 'Arrow'
plotOverLine1Display.GlyphTableIndexArray = 'None'
plotOverLine1Display.GaussianRadius = 0.0005000000074505806
plotOverLine1Display.SetScaleArray = ['POINTS', 'U']
plotOverLine1Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.OpacityArray = ['POINTS', 'U']
plotOverLine1Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')

# show data in view
plotOverLine1Display_1 = Show(plotOverLine1, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1Display_1.UseIndexForXAxis = 0
plotOverLine1Display_1.XArrayName = 'arc_length'
plotOverLine1Display_1.SeriesVisibility = ['p', 'U_Magnitude']
plotOverLine1Display_1.SeriesLabel = ['arc_length', 'arc_length', 'p', 'p', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'p', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'U_X', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'U_Y', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'U_Z', '0.6', '0.3100022888532845', '0.6399938963912413', 'U_Magnitude', '1', '0.5000076295109483', '0', 'vtkValidPointMask', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_X', '0', '0', '0', 'Points_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Points_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155']
plotOverLine1Display_1.SeriesPlotCorner = ['arc_length', '0', 'p', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesLabelPrefix = ''
plotOverLine1Display_1.SeriesLineStyle = ['arc_length', '1', 'p', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display_1.SeriesLineThickness = ['arc_length', '2', 'p', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['arc_length', '0', 'p', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesMarkerSize = ['arc_length', '4', 'p', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'U_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'p', '1', 'vtkValidPointMask', '1']
plotOverLine1Display_1.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'p', '2', 'vtkValidPointMask', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'p', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'U_Magnitude', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'arc_length', '4', 'p', '4', 'vtkValidPointMask', '4']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['p']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = []

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['U_X']

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1316, 765)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [1.5, 0.05000000074505806, 5.80380599615781]
renderView1.CameraFocalPoint = [1.5, 0.05000000074505806, 0.004999999888241291]
renderView1.CameraParallelScale = 1.5008414306892612

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).