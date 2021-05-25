#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on May 24, 2021, at 22:32
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.4'
expName = 'AY_SymmetrySpanDraft'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Andre - Productivity\\OneDrive\\Desktop\\SymmetrySpanFix\\AY_SymmetrySpanDraft_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
instuctions_1 = visual.TextStim(win=win, name='instuctions_1',
    text='In this experiment you will try to memorize the position of colored squares you see on the screen while you make symmetry judgments about other pictures. In the next few minutes, we will explain how the experiment will work.\n\nPress Space to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Instructions_2"
Instructions_2Clock = core.Clock()
instuctions = visual.TextStim(win=win, name='instuctions',
    text='For this experiment, squares will appear on the screen one at a time between a symmetry task. Try to remember where each square was, in the order it was presented in. \n\nAfter 5 squares have been shown, you will see a grid of the 16 possible places the squares could have been. \n\nPress Space to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "trialsquare_pres"
trialsquare_presClock = core.Clock()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='grid.png', mask=None,
    ori=0, pos=(0, 0), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
polygon = visual.Rect(
    win=win, name='polygon',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=[-0.075, 0.075],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.804,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "trialsymmetry_pres"
trialsymmetry_presClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sym1.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
key_resp_5 = keyboard.Keyboard()
text_4 = visual.TextStim(win=win, name='text_4',
    text='<-    symmetrical  |  non-symmetrical ->',
    font='Arial',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Instructions_4"
Instructions_4Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Your job is to select each square in the order presented. \nTo do this, use the mouse to select the appropriate boxes. The squares you select will turn red. \n\nThis is a sample run, so you will only need to recall one box.\n\nPress Space to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "recalltrial"
recalltrialClock = core.Clock()
trialselect = visual.ImageStim(
    win=win,
    name='trialselect', 
    image='grid.png', mask=None,
    ori=0, pos=(0, 0), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Select square locations in order that you saw them',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Instructions_3"
Instructions_3Clock = core.Clock()
key_resp_3 = keyboard.Keyboard()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Before a square is presented, a picture will appear on the screen, and you will have to decide if it is symmetrical. A picture is symmetrical if you can fold it in half vertically and the picture on the left lines up with the picture on the right. \n\nAfter 5 symmetry-square loops, you will be asked to recall the order of the red squares on a 4x4 grid.\n\nPress space to start the experiment.\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Reset_sequence"
Reset_sequenceClock = core.Clock()

# Initialize components for Routine "Square_pres"
Square_presClock = core.Clock()
fixation_1 = visual.TextStim(win=win, name='fixation_1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
grid = visual.ImageStim(
    win=win,
    name='grid', 
    image='grid.png', mask=None,
    ori=0, pos=(0, 0), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
square = visual.Rect(
    win=win, name='square',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=[0.804,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)

# Initialize components for Routine "Sym_trials"
Sym_trialsClock = core.Clock()
symmetry_grid = visual.ImageStim(
    win=win,
    name='symmetry_grid', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
sym_resp = keyboard.Keyboard()
text = visual.TextStim(win=win, name='text',
    text='<-    symmetrical  |  non-symmetrical ->',
    font='Arial',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Square_recall_practice"
Square_recall_practiceClock = core.Clock()
recall_text = visual.TextStim(win=win, name='recall_text',
    text='Recall',
    font='Arial',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructions_2 = visual.TextStim(win=win, name='instructions_2',
    text='Select square locations in order that you saw them',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
fixation_2 = visual.TextStim(win=win, name='fixation_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
grid_2 = visual.ImageStim(
    win=win,
    name='grid_2', 
    image='grid.png', mask=None,
    ori=0, pos=(0, 0), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
square_resp = event.Mouse(win=win)
x, y = [None, None]
square_resp.mouseClock = core.Clock()
square_1 = visual.Rect(
    win=win, name='square_1',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=(-0.225, 0.225),
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=[1.000,0.004,0.004], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
square_2 = visual.Rect(
    win=win, name='square_2',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=(-0.075, 0.225),
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=[1.000,0.004,0.004], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
square_3 = visual.Rect(
    win=win, name='square_3',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=(0.075, 0.225),
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=[1.000,0.004,0.004], fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
square_4 = visual.Rect(
    win=win, name='square_4',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=(0.225, 0.225),
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=[1.000,0.004,0.004], fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
square_5 = visual.Rect(
    win=win, name='square_5',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=(-0.225, 0.075),
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=[1.000,0.004,0.004], fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
square_6 = visual.Rect(
    win=win, name='square_6',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=(-0.075, 0.075),
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=[1.000,0.004,0.004], fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
square_7 = visual.Rect(
    win=win, name='square_7',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=(0.075, 0.075),
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=[1.000,0.004,0.004], fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)
square_8 = visual.Rect(
    win=win, name='square_8',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=(0.225, 0.075),
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=[1.000,0.004,0.004], fillColorSpace='rgb',
    opacity=1, depth=-12.0, interpolate=True)
square_9 = visual.Rect(
    win=win, name='square_9',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=(-0.225, -0.075),
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=[1.000,0.004,0.004], fillColorSpace='rgb',
    opacity=1, depth=-13.0, interpolate=True)
square_10 = visual.Rect(
    win=win, name='square_10',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=(-0.075, -0.075),
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=[1.000,0.004,0.004], fillColorSpace='rgb',
    opacity=1, depth=-14.0, interpolate=True)
square_11 = visual.Rect(
    win=win, name='square_11',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=(0.075, -0.075),
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=[1.000,0.004,0.004], fillColorSpace='rgb',
    opacity=1, depth=-15.0, interpolate=True)
square_12 = visual.Rect(
    win=win, name='square_12',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=(0.225, -0.075),
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=[1.000,0.004,0.004], fillColorSpace='rgb',
    opacity=1, depth=-16.0, interpolate=True)
square_13 = visual.Rect(
    win=win, name='square_13',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=(-0.225, -0.225),
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=[1.000,0.004,0.004], fillColorSpace='rgb',
    opacity=1, depth=-17.0, interpolate=True)
square_14 = visual.Rect(
    win=win, name='square_14',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=(-0.075, -0.225),
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=[1.000,0.004,0.004], fillColorSpace='rgb',
    opacity=1, depth=-18.0, interpolate=True)
square_15 = visual.Rect(
    win=win, name='square_15',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=(0.075, -0.225),
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=[1.000,0.004,0.004], fillColorSpace='rgb',
    opacity=1, depth=-19.0, interpolate=True)
square_16 = visual.Rect(
    win=win, name='square_16',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0, pos=(0.225, -0.225),
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=[1.000,0.004,0.004], fillColorSpace='rgb',
    opacity=1, depth=-20.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
InstructionsComponents = [instuctions_1, key_resp]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instuctions_1* updates
    if instuctions_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        instuctions_1.frameNStart = frameN  # exact frame index
        instuctions_1.tStart = t  # local t and not account for scr refresh
        instuctions_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instuctions_1, 'tStartRefresh')  # time at next scr refresh
        instuctions_1.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instuctions_1.started', instuctions_1.tStartRefresh)
thisExp.addData('instuctions_1.stopped', instuctions_1.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions_2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
Instructions_2Components = [instuctions, key_resp_2]
for thisComponent in Instructions_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instructions_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions_2"-------
while continueRoutine:
    # get current time
    t = Instructions_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instructions_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instuctions* updates
    if instuctions.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        instuctions.frameNStart = frameN  # exact frame index
        instuctions.tStart = t  # local t and not account for scr refresh
        instuctions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instuctions, 'tStartRefresh')  # time at next scr refresh
        instuctions.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions_2"-------
for thisComponent in Instructions_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instuctions.started', instuctions.tStartRefresh)
thisExp.addData('instuctions.stopped', instuctions.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trialsquare_pres"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
trialsquare_presComponents = [image_2, polygon]
for thisComponent in trialsquare_presComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialsquare_presClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trialsquare_pres"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trialsquare_presClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialsquare_presClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_2* updates
    if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_2.frameNStart = frameN  # exact frame index
        image_2.tStart = t  # local t and not account for scr refresh
        image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
        image_2.setAutoDraw(True)
    if image_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_2.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            image_2.tStop = t  # not accounting for scr refresh
            image_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_2, 'tStopRefresh')  # time at next scr refresh
            image_2.setAutoDraw(False)
    
    # *polygon* updates
    if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon.frameNStart = frameN  # exact frame index
        polygon.tStart = t  # local t and not account for scr refresh
        polygon.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
        polygon.setAutoDraw(True)
    if polygon.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            polygon.tStop = t  # not accounting for scr refresh
            polygon.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
            polygon.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialsquare_presComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trialsquare_pres"-------
for thisComponent in trialsquare_presComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_2.started', image_2.tStartRefresh)
thisExp.addData('image_2.stopped', image_2.tStopRefresh)
thisExp.addData('polygon.started', polygon.tStartRefresh)
thisExp.addData('polygon.stopped', polygon.tStopRefresh)

# ------Prepare to start Routine "trialsymmetry_pres"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
trialsymmetry_presComponents = [image, key_resp_5, text_4]
for thisComponent in trialsymmetry_presComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialsymmetry_presClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trialsymmetry_pres"-------
while continueRoutine:
    # get current time
    t = trialsymmetry_presClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialsymmetry_presClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['left', 'right'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    if text_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_4.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_4.tStop = t  # not accounting for scr refresh
            text_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
            text_4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialsymmetry_presComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trialsymmetry_pres"-------
for thisComponent in trialsymmetry_presComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
# the Routine "trialsymmetry_pres" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions_4"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
Instructions_4Components = [text_3, key_resp_4]
for thisComponent in Instructions_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instructions_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions_4"-------
while continueRoutine:
    # get current time
    t = Instructions_4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instructions_4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions_4"-------
for thisComponent in Instructions_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "recalltrial"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
gotValidClick = False  # until a click is received
# keep track of which components have finished
recalltrialComponents = [trialselect, mouse, text_5]
for thisComponent in recalltrialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
recalltrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "recalltrial"-------
while continueRoutine:
    # get current time
    t = recalltrialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=recalltrialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *trialselect* updates
    if trialselect.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        trialselect.frameNStart = frameN  # exact frame index
        trialselect.tStart = t  # local t and not account for scr refresh
        trialselect.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trialselect, 'tStartRefresh')  # time at next scr refresh
        trialselect.setAutoDraw(True)
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # abort routine on response
                continueRoutine = False
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in recalltrialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "recalltrial"-------
for thisComponent in recalltrialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('trialselect.started', trialselect.tStartRefresh)
thisExp.addData('trialselect.stopped', trialselect.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse.getPos()
buttons = mouse.getPressed()
thisExp.addData('mouse.x', x)
thisExp.addData('mouse.y', y)
thisExp.addData('mouse.leftButton', buttons[0])
thisExp.addData('mouse.midButton', buttons[1])
thisExp.addData('mouse.rightButton', buttons[2])
thisExp.addData('mouse.started', mouse.tStart)
thisExp.addData('mouse.stopped', mouse.tStop)
thisExp.nextEntry()
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
# the Routine "recalltrial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions_3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
Instructions_3Components = [key_resp_3, text_2]
for thisComponent in Instructions_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instructions_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions_3"-------
while continueRoutine:
    # get current time
    t = Instructions_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instructions_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions_3"-------
for thisComponent in Instructions_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# the Routine "Instructions_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
memory_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('choose_cond.xlsx'),
    seed=None, name='memory_trials')
thisExp.addLoop(memory_trials)  # add the loop to the experiment
thisMemory_trial = memory_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMemory_trial.rgb)
if thisMemory_trial != None:
    for paramName in thisMemory_trial:
        exec('{} = thisMemory_trial[paramName]'.format(paramName))

for thisMemory_trial in memory_trials:
    currentLoop = memory_trials
    # abbreviate parameter names if possible (e.g. rgb = thisMemory_trial.rgb)
    if thisMemory_trial != None:
        for paramName in thisMemory_trial:
            exec('{} = thisMemory_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Reset_sequence"-------
    continueRoutine = True
    # update component parameters for each repeat
    correct_sequence = []
    # keep track of which components have finished
    Reset_sequenceComponents = []
    for thisComponent in Reset_sequenceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Reset_sequenceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Reset_sequence"-------
    while continueRoutine:
        # get current time
        t = Reset_sequenceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Reset_sequenceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Reset_sequenceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Reset_sequence"-------
    for thisComponent in Reset_sequenceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Reset_sequence" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    sym_trials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(condition_file),
        seed=None, name='sym_trials')
    thisExp.addLoop(sym_trials)  # add the loop to the experiment
    thisSym_trial = sym_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSym_trial.rgb)
    if thisSym_trial != None:
        for paramName in thisSym_trial:
            exec('{} = thisSym_trial[paramName]'.format(paramName))
    
    for thisSym_trial in sym_trials:
        currentLoop = sym_trials
        # abbreviate parameter names if possible (e.g. rgb = thisSym_trial.rgb)
        if thisSym_trial != None:
            for paramName in thisSym_trial:
                exec('{} = thisSym_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Square_pres"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        square.setPos([-0.075, 0.075])
        correct_sequence.append(square_corr)
        # keep track of which components have finished
        Square_presComponents = [fixation_1, grid, square]
        for thisComponent in Square_presComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Square_presClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Square_pres"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Square_presClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Square_presClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_1* updates
            if fixation_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_1.frameNStart = frameN  # exact frame index
                fixation_1.tStart = t  # local t and not account for scr refresh
                fixation_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_1, 'tStartRefresh')  # time at next scr refresh
                fixation_1.setAutoDraw(True)
            if fixation_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_1.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_1.tStop = t  # not accounting for scr refresh
                    fixation_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation_1, 'tStopRefresh')  # time at next scr refresh
                    fixation_1.setAutoDraw(False)
            
            # *grid* updates
            if grid.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                grid.frameNStart = frameN  # exact frame index
                grid.tStart = t  # local t and not account for scr refresh
                grid.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(grid, 'tStartRefresh')  # time at next scr refresh
                grid.setAutoDraw(True)
            if grid.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > grid.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    grid.tStop = t  # not accounting for scr refresh
                    grid.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(grid, 'tStopRefresh')  # time at next scr refresh
                    grid.setAutoDraw(False)
            
            # *square* updates
            if square.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square.frameNStart = frameN  # exact frame index
                square.tStart = t  # local t and not account for scr refresh
                square.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square, 'tStartRefresh')  # time at next scr refresh
                square.setAutoDraw(True)
            if square.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > square.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    square.tStop = t  # not accounting for scr refresh
                    square.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(square, 'tStopRefresh')  # time at next scr refresh
                    square.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Square_presComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Square_pres"-------
        for thisComponent in Square_presComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # ------Prepare to start Routine "Sym_trials"-------
        continueRoutine = True
        # update component parameters for each repeat
        symmetry_grid.setImage(picture)
        sym_resp.keys = []
        sym_resp.rt = []
        _sym_resp_allKeys = []
        # keep track of which components have finished
        Sym_trialsComponents = [symmetry_grid, sym_resp, text]
        for thisComponent in Sym_trialsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Sym_trialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Sym_trials"-------
        while continueRoutine:
            # get current time
            t = Sym_trialsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Sym_trialsClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *symmetry_grid* updates
            if symmetry_grid.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                symmetry_grid.frameNStart = frameN  # exact frame index
                symmetry_grid.tStart = t  # local t and not account for scr refresh
                symmetry_grid.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(symmetry_grid, 'tStartRefresh')  # time at next scr refresh
                symmetry_grid.setAutoDraw(True)
            
            # *sym_resp* updates
            waitOnFlip = False
            if sym_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                sym_resp.frameNStart = frameN  # exact frame index
                sym_resp.tStart = t  # local t and not account for scr refresh
                sym_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sym_resp, 'tStartRefresh')  # time at next scr refresh
                sym_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(sym_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(sym_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if sym_resp.status == STARTED and not waitOnFlip:
                theseKeys = sym_resp.getKeys(keyList=['left', 'right'], waitRelease=False)
                _sym_resp_allKeys.extend(theseKeys)
                if len(_sym_resp_allKeys):
                    sym_resp.keys = _sym_resp_allKeys[-1].name  # just the last key pressed
                    sym_resp.rt = _sym_resp_allKeys[-1].rt
                    # was this correct?
                    if (sym_resp.keys == str(sym_corr)) or (sym_resp.keys == sym_corr):
                        sym_resp.corr = 1
                    else:
                        sym_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Sym_trialsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Sym_trials"-------
        for thisComponent in Sym_trialsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if sym_resp.keys in ['', [], None]:  # No response was made
            sym_resp.keys = None
            # was no response the correct answer?!
            if str(sym_corr).lower() == 'none':
               sym_resp.corr = 1;  # correct non-response
            else:
               sym_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for sym_trials (TrialHandler)
        sym_trials.addData('sym_resp.keys',sym_resp.keys)
        sym_trials.addData('sym_resp.corr', sym_resp.corr)
        if sym_resp.keys != None:  # we had a response
            sym_trials.addData('sym_resp.rt', sym_resp.rt)
        sym_trials.addData('sym_resp.started', sym_resp.tStartRefresh)
        sym_trials.addData('sym_resp.stopped', sym_resp.tStopRefresh)
        # the Routine "Sym_trials" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'sym_trials'
    
    
    # set up handler to look after randomisation of conditions etc
    recall = data.TrialHandler(nReps=5, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='recall')
    thisExp.addLoop(recall)  # add the loop to the experiment
    thisRecall = recall.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRecall.rgb)
    if thisRecall != None:
        for paramName in thisRecall:
            exec('{} = thisRecall[paramName]'.format(paramName))
    
    for thisRecall in recall:
        currentLoop = recall
        # abbreviate parameter names if possible (e.g. rgb = thisRecall.rgb)
        if thisRecall != None:
            for paramName in thisRecall:
                exec('{} = thisRecall[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Square_recall_practice"-------
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the square_resp
        square_resp.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        Square_recall_practiceComponents = [recall_text, instructions_2, fixation_2, grid_2, square_resp, square_1, square_2, square_3, square_4, square_5, square_6, square_7, square_8, square_9, square_10, square_11, square_12, square_13, square_14, square_15, square_16]
        for thisComponent in Square_recall_practiceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Square_recall_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Square_recall_practice"-------
        while continueRoutine:
            # get current time
            t = Square_recall_practiceClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Square_recall_practiceClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *recall_text* updates
            if recall_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                recall_text.frameNStart = frameN  # exact frame index
                recall_text.tStart = t  # local t and not account for scr refresh
                recall_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(recall_text, 'tStartRefresh')  # time at next scr refresh
                recall_text.setAutoDraw(True)
            
            # *instructions_2* updates
            if instructions_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                instructions_2.frameNStart = frameN  # exact frame index
                instructions_2.tStart = t  # local t and not account for scr refresh
                instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instructions_2, 'tStartRefresh')  # time at next scr refresh
                instructions_2.setAutoDraw(True)
            
            # *fixation_2* updates
            if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_2.frameNStart = frameN  # exact frame index
                fixation_2.tStart = t  # local t and not account for scr refresh
                fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
                fixation_2.setAutoDraw(True)
            if fixation_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_2.tStop = t  # not accounting for scr refresh
                    fixation_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
                    fixation_2.setAutoDraw(False)
            
            # *grid_2* updates
            if grid_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                grid_2.frameNStart = frameN  # exact frame index
                grid_2.tStart = t  # local t and not account for scr refresh
                grid_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(grid_2, 'tStartRefresh')  # time at next scr refresh
                grid_2.setAutoDraw(True)
            # *square_resp* updates
            if square_resp.status == NOT_STARTED and t >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square_resp.frameNStart = frameN  # exact frame index
                square_resp.tStart = t  # local t and not account for scr refresh
                square_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_resp, 'tStartRefresh')  # time at next scr refresh
                square_resp.status = STARTED
                square_resp.mouseClock.reset()
                prevButtonState = square_resp.getPressed()  # if button is down already this ISN'T a new click
            if square_resp.status == STARTED:  # only update if started and not finished!
                buttons = square_resp.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [square_1, square_2, square_3, square_4, square_5, square_6, square_7, square_8, square_9, square_10, square_11, square_12, square_13, square_14, square_15, square_16]:
                            if obj.contains(square_resp):
                                gotValidClick = True
                                square_resp.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *square_1* updates
            if square_1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square_1.frameNStart = frameN  # exact frame index
                square_1.tStart = t  # local t and not account for scr refresh
                square_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_1, 'tStartRefresh')  # time at next scr refresh
                square_1.setAutoDraw(True)
            
            # *square_2* updates
            if square_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square_2.frameNStart = frameN  # exact frame index
                square_2.tStart = t  # local t and not account for scr refresh
                square_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_2, 'tStartRefresh')  # time at next scr refresh
                square_2.setAutoDraw(True)
            
            # *square_3* updates
            if square_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square_3.frameNStart = frameN  # exact frame index
                square_3.tStart = t  # local t and not account for scr refresh
                square_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_3, 'tStartRefresh')  # time at next scr refresh
                square_3.setAutoDraw(True)
            
            # *square_4* updates
            if square_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square_4.frameNStart = frameN  # exact frame index
                square_4.tStart = t  # local t and not account for scr refresh
                square_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_4, 'tStartRefresh')  # time at next scr refresh
                square_4.setAutoDraw(True)
            
            # *square_5* updates
            if square_5.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square_5.frameNStart = frameN  # exact frame index
                square_5.tStart = t  # local t and not account for scr refresh
                square_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_5, 'tStartRefresh')  # time at next scr refresh
                square_5.setAutoDraw(True)
            
            # *square_6* updates
            if square_6.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square_6.frameNStart = frameN  # exact frame index
                square_6.tStart = t  # local t and not account for scr refresh
                square_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_6, 'tStartRefresh')  # time at next scr refresh
                square_6.setAutoDraw(True)
            
            # *square_7* updates
            if square_7.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square_7.frameNStart = frameN  # exact frame index
                square_7.tStart = t  # local t and not account for scr refresh
                square_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_7, 'tStartRefresh')  # time at next scr refresh
                square_7.setAutoDraw(True)
            
            # *square_8* updates
            if square_8.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square_8.frameNStart = frameN  # exact frame index
                square_8.tStart = t  # local t and not account for scr refresh
                square_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_8, 'tStartRefresh')  # time at next scr refresh
                square_8.setAutoDraw(True)
            
            # *square_9* updates
            if square_9.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square_9.frameNStart = frameN  # exact frame index
                square_9.tStart = t  # local t and not account for scr refresh
                square_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_9, 'tStartRefresh')  # time at next scr refresh
                square_9.setAutoDraw(True)
            
            # *square_10* updates
            if square_10.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square_10.frameNStart = frameN  # exact frame index
                square_10.tStart = t  # local t and not account for scr refresh
                square_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_10, 'tStartRefresh')  # time at next scr refresh
                square_10.setAutoDraw(True)
            
            # *square_11* updates
            if square_11.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square_11.frameNStart = frameN  # exact frame index
                square_11.tStart = t  # local t and not account for scr refresh
                square_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_11, 'tStartRefresh')  # time at next scr refresh
                square_11.setAutoDraw(True)
            
            # *square_12* updates
            if square_12.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square_12.frameNStart = frameN  # exact frame index
                square_12.tStart = t  # local t and not account for scr refresh
                square_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_12, 'tStartRefresh')  # time at next scr refresh
                square_12.setAutoDraw(True)
            
            # *square_13* updates
            if square_13.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square_13.frameNStart = frameN  # exact frame index
                square_13.tStart = t  # local t and not account for scr refresh
                square_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_13, 'tStartRefresh')  # time at next scr refresh
                square_13.setAutoDraw(True)
            
            # *square_14* updates
            if square_14.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square_14.frameNStart = frameN  # exact frame index
                square_14.tStart = t  # local t and not account for scr refresh
                square_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_14, 'tStartRefresh')  # time at next scr refresh
                square_14.setAutoDraw(True)
            
            # *square_15* updates
            if square_15.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square_15.frameNStart = frameN  # exact frame index
                square_15.tStart = t  # local t and not account for scr refresh
                square_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_15, 'tStartRefresh')  # time at next scr refresh
                square_15.setAutoDraw(True)
            
            # *square_16* updates
            if square_16.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square_16.frameNStart = frameN  # exact frame index
                square_16.tStart = t  # local t and not account for scr refresh
                square_16.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_16, 'tStartRefresh')  # time at next scr refresh
                square_16.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Square_recall_practiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Square_recall_practice"-------
        for thisComponent in Square_recall_practiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        recall.addData('instructions_2.started', instructions_2.tStartRefresh)
        recall.addData('instructions_2.stopped', instructions_2.tStopRefresh)
        # store data for recall (TrialHandler)
        x, y = square_resp.getPos()
        buttons = square_resp.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [square_1, square_2, square_3, square_4, square_5, square_6, square_7, square_8, square_9, square_10, square_11, square_12, square_13, square_14, square_15, square_16]:
                if obj.contains(square_resp):
                    gotValidClick = True
                    square_resp.clicked_name.append(obj.name)
        recall.addData('square_resp.x', x)
        recall.addData('square_resp.y', y)
        recall.addData('square_resp.leftButton', buttons[0])
        recall.addData('square_resp.midButton', buttons[1])
        recall.addData('square_resp.rightButton', buttons[2])
        if len(square_resp.clicked_name):
            recall.addData('square_resp.clicked_name', square_resp.clicked_name[0])
        recall.addData('square_resp.started', square_resp.tStart)
        recall.addData('square_resp.stopped', square_resp.tStop)
        square_corr = correct_sequence[recall.thisN]
        square_resp.clicked_name = square_resp.clicked_name[0]
        if square_resp.clicked_name == square_corr:
            corr = 1
        else:
            corr = 0
        thisExp.addData('square_correct', corr)
        # the Routine "Square_recall_practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 5 repeats of 'recall'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'memory_trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
