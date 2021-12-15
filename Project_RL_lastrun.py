#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Wed Dec  1 15:22:07 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'Project_RL'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
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
    originPath='/Users/riinalehtonen/UNI/NEURO/Psychophysics/Project/Project_RL_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

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

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instruction"
InstructionClock = core.Clock()
Instruction_image = visual.ImageStim(
    win=win,
    name='Instruction_image', units='pix', 
    image='Instruction_image.png', mask=None,
    ori=0.0, pos=(0, 0), size=[1214, 612],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Begin_task = keyboard.Keyboard()

# Initialize components for Routine "Part_1"
Part_1Clock = core.Clock()
Warning_signal_1 = visual.ShapeStim(
    win=win, name='Warning_signal_1', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
The_word_1 = visual.TextStim(win=win, name='The_word_1',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Response_1 = keyboard.Keyboard()

# Initialize components for Routine "Part_2"
Part_2Clock = core.Clock()
Warning_signal_2 = visual.ShapeStim(
    win=win, name='Warning_signal_2', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
The_word_2 = visual.TextStim(win=win, name='The_word_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Response_2 = keyboard.Keyboard()

# Initialize components for Routine "The_end"
The_endClock = core.Clock()
The_end_text = visual.TextStim(win=win, name='The_end_text',
    text='Thank you for participating! Press space bar to end the trial.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
End_task = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instruction"-------
continueRoutine = True
# update component parameters for each repeat
Begin_task.keys = []
Begin_task.rt = []
_Begin_task_allKeys = []
# keep track of which components have finished
InstructionComponents = [Instruction_image, Begin_task]
for thisComponent in InstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instruction"-------
while continueRoutine:
    # get current time
    t = InstructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instruction_image* updates
    if Instruction_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instruction_image.frameNStart = frameN  # exact frame index
        Instruction_image.tStart = t  # local t and not account for scr refresh
        Instruction_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruction_image, 'tStartRefresh')  # time at next scr refresh
        Instruction_image.setAutoDraw(True)
    
    # *Begin_task* updates
    waitOnFlip = False
    if Begin_task.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Begin_task.frameNStart = frameN  # exact frame index
        Begin_task.tStart = t  # local t and not account for scr refresh
        Begin_task.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Begin_task, 'tStartRefresh')  # time at next scr refresh
        Begin_task.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Begin_task.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Begin_task.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Begin_task.status == STARTED and not waitOnFlip:
        theseKeys = Begin_task.getKeys(keyList=['space'], waitRelease=False)
        _Begin_task_allKeys.extend(theseKeys)
        if len(_Begin_task_allKeys):
            Begin_task.keys = _Begin_task_allKeys[-1].name  # just the last key pressed
            Begin_task.rt = _Begin_task_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction"-------
for thisComponent in InstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instruction_image.started', Instruction_image.tStartRefresh)
thisExp.addData('Instruction_image.stopped', Instruction_image.tStopRefresh)
# check responses
if Begin_task.keys in ['', [], None]:  # No response was made
    Begin_task.keys = None
thisExp.addData('Begin_task.keys',Begin_task.keys)
if Begin_task.keys != None:  # we had a response
    thisExp.addData('Begin_task.rt', Begin_task.rt)
thisExp.addData('Begin_task.started', Begin_task.tStartRefresh)
thisExp.addData('Begin_task.stopped', Begin_task.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Conditions_1 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions_file.xlsx'),
    seed=None, name='Conditions_1')
thisExp.addLoop(Conditions_1)  # add the loop to the experiment
thisCondition_1 = Conditions_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCondition_1.rgb)
if thisCondition_1 != None:
    for paramName in thisCondition_1:
        exec('{} = thisCondition_1[paramName]'.format(paramName))

for thisCondition_1 in Conditions_1:
    currentLoop = Conditions_1
    # abbreviate parameter names if possible (e.g. rgb = thisCondition_1.rgb)
    if thisCondition_1 != None:
        for paramName in thisCondition_1:
            exec('{} = thisCondition_1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Part_1"-------
    continueRoutine = True
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    The_word_1.setText(stimulusWord)
    Response_1.keys = []
    Response_1.rt = []
    _Response_1_allKeys = []
    # keep track of which components have finished
    Part_1Components = [Warning_signal_1, The_word_1, Response_1]
    for thisComponent in Part_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Part_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Part_1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Part_1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Part_1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Warning_signal_1* updates
        if Warning_signal_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Warning_signal_1.frameNStart = frameN  # exact frame index
            Warning_signal_1.tStart = t  # local t and not account for scr refresh
            Warning_signal_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Warning_signal_1, 'tStartRefresh')  # time at next scr refresh
            Warning_signal_1.setAutoDraw(True)
        if Warning_signal_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Warning_signal_1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Warning_signal_1.tStop = t  # not accounting for scr refresh
                Warning_signal_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Warning_signal_1, 'tStopRefresh')  # time at next scr refresh
                Warning_signal_1.setAutoDraw(False)
        
        # *The_word_1* updates
        if The_word_1.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            The_word_1.frameNStart = frameN  # exact frame index
            The_word_1.tStart = t  # local t and not account for scr refresh
            The_word_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(The_word_1, 'tStartRefresh')  # time at next scr refresh
            The_word_1.setAutoDraw(True)
        if The_word_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > The_word_1.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                The_word_1.tStop = t  # not accounting for scr refresh
                The_word_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(The_word_1, 'tStopRefresh')  # time at next scr refresh
                The_word_1.setAutoDraw(False)
        
        # *Response_1* updates
        waitOnFlip = False
        if Response_1.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Response_1.frameNStart = frameN  # exact frame index
            Response_1.tStart = t  # local t and not account for scr refresh
            Response_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_1, 'tStartRefresh')  # time at next scr refresh
            Response_1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Response_1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Response_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Response_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_1.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                Response_1.tStop = t  # not accounting for scr refresh
                Response_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Response_1, 'tStopRefresh')  # time at next scr refresh
                Response_1.status = FINISHED
        if Response_1.status == STARTED and not waitOnFlip:
            theseKeys = Response_1.getKeys(keyList=['left', 'right'], waitRelease=False)
            _Response_1_allKeys.extend(theseKeys)
            if len(_Response_1_allKeys):
                Response_1.keys = _Response_1_allKeys[-1].name  # just the last key pressed
                Response_1.rt = _Response_1_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Part_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Part_1"-------
    for thisComponent in Part_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Conditions_1.addData('Warning_signal_1.started', Warning_signal_1.tStartRefresh)
    Conditions_1.addData('Warning_signal_1.stopped', Warning_signal_1.tStopRefresh)
    Conditions_1.addData('The_word_1.started', The_word_1.tStartRefresh)
    Conditions_1.addData('The_word_1.stopped', The_word_1.tStopRefresh)
    # check responses
    if Response_1.keys in ['', [], None]:  # No response was made
        Response_1.keys = None
    Conditions_1.addData('Response_1.keys',Response_1.keys)
    if Response_1.keys != None:  # we had a response
        Conditions_1.addData('Response_1.rt', Response_1.rt)
    Conditions_1.addData('Response_1.started', Response_1.tStartRefresh)
    Conditions_1.addData('Response_1.stopped', Response_1.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Conditions_1'


# set up handler to look after randomisation of conditions etc
Conditions_2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions2_file.xlsx'),
    seed=None, name='Conditions_2')
thisExp.addLoop(Conditions_2)  # add the loop to the experiment
thisCondition_2 = Conditions_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCondition_2.rgb)
if thisCondition_2 != None:
    for paramName in thisCondition_2:
        exec('{} = thisCondition_2[paramName]'.format(paramName))

for thisCondition_2 in Conditions_2:
    currentLoop = Conditions_2
    # abbreviate parameter names if possible (e.g. rgb = thisCondition_2.rgb)
    if thisCondition_2 != None:
        for paramName in thisCondition_2:
            exec('{} = thisCondition_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Part_2"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    The_word_2.setText(stimulusWord_2)
    Response_2.keys = []
    Response_2.rt = []
    _Response_2_allKeys = []
    # keep track of which components have finished
    Part_2Components = [Warning_signal_2, The_word_2, Response_2]
    for thisComponent in Part_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Part_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Part_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Part_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Part_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Warning_signal_2* updates
        if Warning_signal_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Warning_signal_2.frameNStart = frameN  # exact frame index
            Warning_signal_2.tStart = t  # local t and not account for scr refresh
            Warning_signal_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Warning_signal_2, 'tStartRefresh')  # time at next scr refresh
            Warning_signal_2.setAutoDraw(True)
        if Warning_signal_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Warning_signal_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Warning_signal_2.tStop = t  # not accounting for scr refresh
                Warning_signal_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Warning_signal_2, 'tStopRefresh')  # time at next scr refresh
                Warning_signal_2.setAutoDraw(False)
        
        # *The_word_2* updates
        if The_word_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            The_word_2.frameNStart = frameN  # exact frame index
            The_word_2.tStart = t  # local t and not account for scr refresh
            The_word_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(The_word_2, 'tStartRefresh')  # time at next scr refresh
            The_word_2.setAutoDraw(True)
        if The_word_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > The_word_2.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                The_word_2.tStop = t  # not accounting for scr refresh
                The_word_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(The_word_2, 'tStopRefresh')  # time at next scr refresh
                The_word_2.setAutoDraw(False)
        
        # *Response_2* updates
        waitOnFlip = False
        if Response_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Response_2.frameNStart = frameN  # exact frame index
            Response_2.tStart = t  # local t and not account for scr refresh
            Response_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response_2, 'tStartRefresh')  # time at next scr refresh
            Response_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Response_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Response_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Response_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response_2.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                Response_2.tStop = t  # not accounting for scr refresh
                Response_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Response_2, 'tStopRefresh')  # time at next scr refresh
                Response_2.status = FINISHED
        if Response_2.status == STARTED and not waitOnFlip:
            theseKeys = Response_2.getKeys(keyList=['left', 'right'], waitRelease=False)
            _Response_2_allKeys.extend(theseKeys)
            if len(_Response_2_allKeys):
                Response_2.keys = _Response_2_allKeys[-1].name  # just the last key pressed
                Response_2.rt = _Response_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Part_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Part_2"-------
    for thisComponent in Part_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Conditions_2.addData('Warning_signal_2.started', Warning_signal_2.tStartRefresh)
    Conditions_2.addData('Warning_signal_2.stopped', Warning_signal_2.tStopRefresh)
    Conditions_2.addData('The_word_2.started', The_word_2.tStartRefresh)
    Conditions_2.addData('The_word_2.stopped', The_word_2.tStopRefresh)
    # check responses
    if Response_2.keys in ['', [], None]:  # No response was made
        Response_2.keys = None
    Conditions_2.addData('Response_2.keys',Response_2.keys)
    if Response_2.keys != None:  # we had a response
        Conditions_2.addData('Response_2.rt', Response_2.rt)
    Conditions_2.addData('Response_2.started', Response_2.tStartRefresh)
    Conditions_2.addData('Response_2.stopped', Response_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Conditions_2'


# ------Prepare to start Routine "The_end"-------
continueRoutine = True
# update component parameters for each repeat
End_task.keys = []
End_task.rt = []
_End_task_allKeys = []
# keep track of which components have finished
The_endComponents = [The_end_text, End_task]
for thisComponent in The_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
The_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "The_end"-------
while continueRoutine:
    # get current time
    t = The_endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=The_endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *The_end_text* updates
    if The_end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        The_end_text.frameNStart = frameN  # exact frame index
        The_end_text.tStart = t  # local t and not account for scr refresh
        The_end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(The_end_text, 'tStartRefresh')  # time at next scr refresh
        The_end_text.setAutoDraw(True)
    
    # *End_task* updates
    waitOnFlip = False
    if End_task.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        End_task.frameNStart = frameN  # exact frame index
        End_task.tStart = t  # local t and not account for scr refresh
        End_task.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(End_task, 'tStartRefresh')  # time at next scr refresh
        End_task.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(End_task.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(End_task.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if End_task.status == STARTED and not waitOnFlip:
        theseKeys = End_task.getKeys(keyList=['space'], waitRelease=False)
        _End_task_allKeys.extend(theseKeys)
        if len(_End_task_allKeys):
            End_task.keys = _End_task_allKeys[-1].name  # just the last key pressed
            End_task.rt = _End_task_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in The_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "The_end"-------
for thisComponent in The_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('The_end_text.started', The_end_text.tStartRefresh)
thisExp.addData('The_end_text.stopped', The_end_text.tStopRefresh)
# check responses
if End_task.keys in ['', [], None]:  # No response was made
    End_task.keys = None
thisExp.addData('End_task.keys',End_task.keys)
if End_task.keys != None:  # we had a response
    thisExp.addData('End_task.rt', End_task.rt)
thisExp.addData('End_task.started', End_task.tStartRefresh)
thisExp.addData('End_task.stopped', End_task.tStopRefresh)
thisExp.nextEntry()
# the Routine "The_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
