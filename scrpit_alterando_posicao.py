# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
duto3mOpenFOAM = FindSource('duto3m.OpenFOAM')

# get active source.
plotOverLine1 = GetActiveSource()

# Properties modified on plotOverLine1
plotOverLine1.Point1 = [2.0, 0.0, 0.004999999888241291]
plotOverLine1.Point2 = [2.0, 0.10000000149011612, 0.004999999888241291]

# find view
renderView1 = FindViewOrCreate('RenderView1', viewtype='RenderView')

# update the view to ensure updated data information
renderView1.Update()

# get active view
lineChartView1 = GetActiveViewOrCreate('XYChartView')

# update the view to ensure updated data information
lineChartView1.Update()

# get display properties
plotOverLine1Display = GetDisplayProperties(plotOverLine1, view=lineChartView1)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

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