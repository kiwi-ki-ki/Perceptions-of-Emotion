#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Wed Nov 30 16:23:58 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'KW_BodyFaceExp'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
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
    originPath='/Users/kierawingo/Desktop/FL - 22/4431 - Adv Cog Pro/Final Project Docs/KW_BodyFaceExp_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "intro" ---
intro_txt = visual.TextStim(win=win, name='intro_txt',
    text='This is a facial expression and body language perception task. You will be asked to complete two different tasks guessing the emotion shown.\n\nPress the spacebar to continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
intro_resp = keyboard.Keyboard()

# --- Initialize components for Routine "instruction_one" ---
insr_one_txt = visual.TextStim(win=win, name='insr_one_txt',
    text='The first task is a facial expression recognition task. Your job will be to guess which expression the clip is playing.\n\nThe answer choices will be happy, neutral, or angry for each trial. Please click the corresponding box to indicate your guess. \n\nPress the right arrow key to proceed to the practice trials. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
inst_one_resp = keyboard.Keyboard()

# --- Initialize components for Routine "face_trial" ---
face_images = visual.MovieStim(
    win, name='face_images',
    filename=None, movieLib='ffpyplayer',
    loop=False, volume=1.0,
    pos=(0, 0), size=[1.25,.75], units=None,
    ori=0.0, anchor='center',opacity=None, contrast=1.0,
)

# --- Initialize components for Routine "resp" ---
resp_angry = visual.TextStim(win=win, name='resp_angry',
    text='ANGRY',
    font='Arial',
    pos=[-.35, 0], height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
resp_happy = visual.TextStim(win=win, name='resp_happy',
    text='HAPPY',
    font='Arial',
    pos=[.35, 0], height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
resp_neutral = visual.TextStim(win=win, name='resp_neutral',
    text='NEUTRAL',
    font='Arial',
    pos=[0, 0], height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "begin_trial" ---
begin_txt = visual.TextStim(win=win, name='begin_txt',
    text='The real trials will now begin. \n\nPress the space bar to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
begin_resp = keyboard.Keyboard()

# --- Initialize components for Routine "face_trial" ---
face_images = visual.MovieStim(
    win, name='face_images',
    filename=None, movieLib='ffpyplayer',
    loop=False, volume=1.0,
    pos=(0, 0), size=[1.25,.75], units=None,
    ori=0.0, anchor='center',opacity=None, contrast=1.0,
)

# --- Initialize components for Routine "resp" ---
resp_angry = visual.TextStim(win=win, name='resp_angry',
    text='ANGRY',
    font='Arial',
    pos=[-.35, 0], height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
resp_happy = visual.TextStim(win=win, name='resp_happy',
    text='HAPPY',
    font='Arial',
    pos=[.35, 0], height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
resp_neutral = visual.TextStim(win=win, name='resp_neutral',
    text='NEUTRAL',
    font='Arial',
    pos=[0, 0], height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "instruction_two" ---
insr_two_txt = visual.TextStim(win=win, name='insr_two_txt',
    text='The second task is a body language recognition task. Your job will be to guess which expression the clip is displaying. \n\nThe answer choices will be happy, neutral, or angry for each trial. Please click the corresponding box to indicate your guess. \n\nPress the right arrow key to proceed to the practice trial. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
insr_two_resp = keyboard.Keyboard()

# --- Initialize components for Routine "body_trial" ---
body_images = visual.MovieStim(
    win, name='body_images',
    filename=None, movieLib='ffpyplayer',
    loop=False, volume=1.0,
    pos=(0, 0), size=[1.25,1], units=None,
    ori=0.0, anchor='center',opacity=None, contrast=1.0,
)

# --- Initialize components for Routine "resp" ---
resp_angry = visual.TextStim(win=win, name='resp_angry',
    text='ANGRY',
    font='Arial',
    pos=[-.35, 0], height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
resp_happy = visual.TextStim(win=win, name='resp_happy',
    text='HAPPY',
    font='Arial',
    pos=[.35, 0], height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
resp_neutral = visual.TextStim(win=win, name='resp_neutral',
    text='NEUTRAL',
    font='Arial',
    pos=[0, 0], height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "begin_trial" ---
begin_txt = visual.TextStim(win=win, name='begin_txt',
    text='The real trials will now begin. \n\nPress the space bar to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
begin_resp = keyboard.Keyboard()

# --- Initialize components for Routine "body_trial" ---
body_images = visual.MovieStim(
    win, name='body_images',
    filename=None, movieLib='ffpyplayer',
    loop=False, volume=1.0,
    pos=(0, 0), size=[1.25,1], units=None,
    ori=0.0, anchor='center',opacity=None, contrast=1.0,
)

# --- Initialize components for Routine "resp" ---
resp_angry = visual.TextStim(win=win, name='resp_angry',
    text='ANGRY',
    font='Arial',
    pos=[-.35, 0], height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
resp_happy = visual.TextStim(win=win, name='resp_happy',
    text='HAPPY',
    font='Arial',
    pos=[.35, 0], height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
resp_neutral = visual.TextStim(win=win, name='resp_neutral',
    text='NEUTRAL',
    font='Arial',
    pos=[0, 0], height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "end_exp" ---
end_exp_txt = visual.TextStim(win=win, name='end_exp_txt',
    text='Thank you for participating, this is the end of the experiment. \n \n\nThis window will close automatically. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "intro" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intro_resp.keys = []
intro_resp.rt = []
_intro_resp_allKeys = []
# keep track of which components have finished
introComponents = [intro_txt, intro_resp]
for thisComponent in introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "intro" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_txt* updates
    if intro_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_txt.frameNStart = frameN  # exact frame index
        intro_txt.tStart = t  # local t and not account for scr refresh
        intro_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intro_txt.started')
        intro_txt.setAutoDraw(True)
    
    # *intro_resp* updates
    waitOnFlip = False
    if intro_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_resp.frameNStart = frameN  # exact frame index
        intro_resp.tStart = t  # local t and not account for scr refresh
        intro_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intro_resp.started')
        intro_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intro_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intro_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intro_resp.status == STARTED and not waitOnFlip:
        theseKeys = intro_resp.getKeys(keyList=['space'], waitRelease=False)
        _intro_resp_allKeys.extend(theseKeys)
        if len(_intro_resp_allKeys):
            intro_resp.keys = _intro_resp_allKeys[-1].name  # just the last key pressed
            intro_resp.rt = _intro_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "intro" ---
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intro_resp.keys in ['', [], None]:  # No response was made
    intro_resp.keys = None
thisExp.addData('intro_resp.keys',intro_resp.keys)
if intro_resp.keys != None:  # we had a response
    thisExp.addData('intro_resp.rt', intro_resp.rt)
thisExp.nextEntry()
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instruction_one" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
inst_one_resp.keys = []
inst_one_resp.rt = []
_inst_one_resp_allKeys = []
# keep track of which components have finished
instruction_oneComponents = [insr_one_txt, inst_one_resp]
for thisComponent in instruction_oneComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instruction_one" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *insr_one_txt* updates
    if insr_one_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        insr_one_txt.frameNStart = frameN  # exact frame index
        insr_one_txt.tStart = t  # local t and not account for scr refresh
        insr_one_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(insr_one_txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'insr_one_txt.started')
        insr_one_txt.setAutoDraw(True)
    
    # *inst_one_resp* updates
    waitOnFlip = False
    if inst_one_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inst_one_resp.frameNStart = frameN  # exact frame index
        inst_one_resp.tStart = t  # local t and not account for scr refresh
        inst_one_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inst_one_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'inst_one_resp.started')
        inst_one_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(inst_one_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(inst_one_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if inst_one_resp.status == STARTED and not waitOnFlip:
        theseKeys = inst_one_resp.getKeys(keyList=['right'], waitRelease=False)
        _inst_one_resp_allKeys.extend(theseKeys)
        if len(_inst_one_resp_allKeys):
            inst_one_resp.keys = _inst_one_resp_allKeys[-1].name  # just the last key pressed
            inst_one_resp.rt = _inst_one_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_oneComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction_one" ---
for thisComponent in instruction_oneComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if inst_one_resp.keys in ['', [], None]:  # No response was made
    inst_one_resp.keys = None
thisExp.addData('inst_one_resp.keys',inst_one_resp.keys)
if inst_one_resp.keys != None:  # we had a response
    thisExp.addData('inst_one_resp.rt', inst_one_resp.rt)
thisExp.nextEntry()
# the Routine "instruction_one" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_face = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('practice_conditions.xlsx'),
    seed=None, name='practice_face')
thisExp.addLoop(practice_face)  # add the loop to the experiment
thisPractice_face = practice_face.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_face.rgb)
if thisPractice_face != None:
    for paramName in thisPractice_face:
        exec('{} = thisPractice_face[paramName]'.format(paramName))

for thisPractice_face in practice_face:
    currentLoop = practice_face
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_face.rgb)
    if thisPractice_face != None:
        for paramName in thisPractice_face:
            exec('{} = thisPractice_face[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "face_trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    face_images.setMovie(face_file)
    # keep track of which components have finished
    face_trialComponents = [face_images]
    for thisComponent in face_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "face_trial" ---
    while continueRoutine and routineTimer.getTime() < 1.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *face_images* updates
        if face_images.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            face_images.frameNStart = frameN  # exact frame index
            face_images.tStart = t  # local t and not account for scr refresh
            face_images.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(face_images, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'face_images.started')
            face_images.setAutoDraw(True)
            face_images.play()
        if face_images.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > face_images.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                face_images.tStop = t  # not accounting for scr refresh
                face_images.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'face_images.stopped')
                face_images.setAutoDraw(False)
                face_images.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in face_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "face_trial" ---
    for thisComponent in face_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    face_images.stop()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.500000)
    
    # --- Prepare to start Routine "resp" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    respComponents = [resp_angry, resp_happy, resp_neutral, mouse]
    for thisComponent in respComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "resp" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *resp_angry* updates
        if resp_angry.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp_angry.frameNStart = frameN  # exact frame index
            resp_angry.tStart = t  # local t and not account for scr refresh
            resp_angry.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_angry, 'tStartRefresh')  # time at next scr refresh
            resp_angry.setAutoDraw(True)
        
        # *resp_happy* updates
        if resp_happy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp_happy.frameNStart = frameN  # exact frame index
            resp_happy.tStart = t  # local t and not account for scr refresh
            resp_happy.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_happy, 'tStartRefresh')  # time at next scr refresh
            resp_happy.setAutoDraw(True)
        
        # *resp_neutral* updates
        if resp_neutral.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp_neutral.frameNStart = frameN  # exact frame index
            resp_neutral.tStart = t  # local t and not account for scr refresh
            resp_neutral.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_neutral, 'tStartRefresh')  # time at next scr refresh
            resp_neutral.setAutoDraw(True)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
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
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([resp_angry, resp_happy, resp_neutral])
                        clickableList = [resp_angry, resp_happy, resp_neutral]
                    except:
                        clickableList = [[resp_angry, resp_happy, resp_neutral]]
                    for obj in clickableList:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in respComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "resp" ---
    for thisComponent in respComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for practice_face (TrialHandler)
    practice_face.addData('mouse.x', mouse.x)
    practice_face.addData('mouse.y', mouse.y)
    practice_face.addData('mouse.leftButton', mouse.leftButton)
    practice_face.addData('mouse.midButton', mouse.midButton)
    practice_face.addData('mouse.rightButton', mouse.rightButton)
    practice_face.addData('mouse.time', mouse.time)
    practice_face.addData('mouse.clicked_name', mouse.clicked_name)
    # the Routine "resp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'practice_face'


# --- Prepare to start Routine "begin_trial" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
begin_resp.keys = []
begin_resp.rt = []
_begin_resp_allKeys = []
# keep track of which components have finished
begin_trialComponents = [begin_txt, begin_resp]
for thisComponent in begin_trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "begin_trial" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *begin_txt* updates
    if begin_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        begin_txt.frameNStart = frameN  # exact frame index
        begin_txt.tStart = t  # local t and not account for scr refresh
        begin_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin_txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'begin_txt.started')
        begin_txt.setAutoDraw(True)
    
    # *begin_resp* updates
    waitOnFlip = False
    if begin_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        begin_resp.frameNStart = frameN  # exact frame index
        begin_resp.tStart = t  # local t and not account for scr refresh
        begin_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'begin_resp.started')
        begin_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(begin_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(begin_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if begin_resp.status == STARTED and not waitOnFlip:
        theseKeys = begin_resp.getKeys(keyList=['space'], waitRelease=False)
        _begin_resp_allKeys.extend(theseKeys)
        if len(_begin_resp_allKeys):
            begin_resp.keys = _begin_resp_allKeys[-1].name  # just the last key pressed
            begin_resp.rt = _begin_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in begin_trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "begin_trial" ---
for thisComponent in begin_trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if begin_resp.keys in ['', [], None]:  # No response was made
    begin_resp.keys = None
thisExp.addData('begin_resp.keys',begin_resp.keys)
if begin_resp.keys != None:  # we had a response
    thisExp.addData('begin_resp.rt', begin_resp.rt)
thisExp.nextEntry()
# the Routine "begin_trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trial_one_loop = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('fpface.xlsx'),
    seed=None, name='trial_one_loop')
thisExp.addLoop(trial_one_loop)  # add the loop to the experiment
thisTrial_one_loop = trial_one_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_one_loop.rgb)
if thisTrial_one_loop != None:
    for paramName in thisTrial_one_loop:
        exec('{} = thisTrial_one_loop[paramName]'.format(paramName))

for thisTrial_one_loop in trial_one_loop:
    currentLoop = trial_one_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_one_loop.rgb)
    if thisTrial_one_loop != None:
        for paramName in thisTrial_one_loop:
            exec('{} = thisTrial_one_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "face_trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    face_images.setMovie(face_file)
    # keep track of which components have finished
    face_trialComponents = [face_images]
    for thisComponent in face_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "face_trial" ---
    while continueRoutine and routineTimer.getTime() < 1.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *face_images* updates
        if face_images.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            face_images.frameNStart = frameN  # exact frame index
            face_images.tStart = t  # local t and not account for scr refresh
            face_images.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(face_images, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'face_images.started')
            face_images.setAutoDraw(True)
            face_images.play()
        if face_images.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > face_images.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                face_images.tStop = t  # not accounting for scr refresh
                face_images.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'face_images.stopped')
                face_images.setAutoDraw(False)
                face_images.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in face_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "face_trial" ---
    for thisComponent in face_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    face_images.stop()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.500000)
    
    # --- Prepare to start Routine "resp" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    respComponents = [resp_angry, resp_happy, resp_neutral, mouse]
    for thisComponent in respComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "resp" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *resp_angry* updates
        if resp_angry.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp_angry.frameNStart = frameN  # exact frame index
            resp_angry.tStart = t  # local t and not account for scr refresh
            resp_angry.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_angry, 'tStartRefresh')  # time at next scr refresh
            resp_angry.setAutoDraw(True)
        
        # *resp_happy* updates
        if resp_happy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp_happy.frameNStart = frameN  # exact frame index
            resp_happy.tStart = t  # local t and not account for scr refresh
            resp_happy.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_happy, 'tStartRefresh')  # time at next scr refresh
            resp_happy.setAutoDraw(True)
        
        # *resp_neutral* updates
        if resp_neutral.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp_neutral.frameNStart = frameN  # exact frame index
            resp_neutral.tStart = t  # local t and not account for scr refresh
            resp_neutral.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_neutral, 'tStartRefresh')  # time at next scr refresh
            resp_neutral.setAutoDraw(True)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
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
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([resp_angry, resp_happy, resp_neutral])
                        clickableList = [resp_angry, resp_happy, resp_neutral]
                    except:
                        clickableList = [[resp_angry, resp_happy, resp_neutral]]
                    for obj in clickableList:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in respComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "resp" ---
    for thisComponent in respComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trial_one_loop (TrialHandler)
    trial_one_loop.addData('mouse.x', mouse.x)
    trial_one_loop.addData('mouse.y', mouse.y)
    trial_one_loop.addData('mouse.leftButton', mouse.leftButton)
    trial_one_loop.addData('mouse.midButton', mouse.midButton)
    trial_one_loop.addData('mouse.rightButton', mouse.rightButton)
    trial_one_loop.addData('mouse.time', mouse.time)
    trial_one_loop.addData('mouse.clicked_name', mouse.clicked_name)
    # the Routine "resp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'trial_one_loop'


# --- Prepare to start Routine "instruction_two" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
insr_two_resp.keys = []
insr_two_resp.rt = []
_insr_two_resp_allKeys = []
# keep track of which components have finished
instruction_twoComponents = [insr_two_txt, insr_two_resp]
for thisComponent in instruction_twoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instruction_two" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *insr_two_txt* updates
    if insr_two_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        insr_two_txt.frameNStart = frameN  # exact frame index
        insr_two_txt.tStart = t  # local t and not account for scr refresh
        insr_two_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(insr_two_txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'insr_two_txt.started')
        insr_two_txt.setAutoDraw(True)
    
    # *insr_two_resp* updates
    waitOnFlip = False
    if insr_two_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        insr_two_resp.frameNStart = frameN  # exact frame index
        insr_two_resp.tStart = t  # local t and not account for scr refresh
        insr_two_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(insr_two_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'insr_two_resp.started')
        insr_two_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(insr_two_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(insr_two_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if insr_two_resp.status == STARTED and not waitOnFlip:
        theseKeys = insr_two_resp.getKeys(keyList=['right'], waitRelease=False)
        _insr_two_resp_allKeys.extend(theseKeys)
        if len(_insr_two_resp_allKeys):
            insr_two_resp.keys = _insr_two_resp_allKeys[-1].name  # just the last key pressed
            insr_two_resp.rt = _insr_two_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_twoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction_two" ---
for thisComponent in instruction_twoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if insr_two_resp.keys in ['', [], None]:  # No response was made
    insr_two_resp.keys = None
thisExp.addData('insr_two_resp.keys',insr_two_resp.keys)
if insr_two_resp.keys != None:  # we had a response
    thisExp.addData('insr_two_resp.rt', insr_two_resp.rt)
thisExp.nextEntry()
# the Routine "instruction_two" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_loop_body = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('practice_conditions.xlsx'),
    seed=None, name='practice_loop_body')
thisExp.addLoop(practice_loop_body)  # add the loop to the experiment
thisPractice_loop_body = practice_loop_body.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_loop_body.rgb)
if thisPractice_loop_body != None:
    for paramName in thisPractice_loop_body:
        exec('{} = thisPractice_loop_body[paramName]'.format(paramName))

for thisPractice_loop_body in practice_loop_body:
    currentLoop = practice_loop_body
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_loop_body.rgb)
    if thisPractice_loop_body != None:
        for paramName in thisPractice_loop_body:
            exec('{} = thisPractice_loop_body[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "body_trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    body_images.setMovie(body_file)
    # keep track of which components have finished
    body_trialComponents = [body_images]
    for thisComponent in body_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "body_trial" ---
    while continueRoutine and routineTimer.getTime() < 1.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *body_images* updates
        if body_images.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            body_images.frameNStart = frameN  # exact frame index
            body_images.tStart = t  # local t and not account for scr refresh
            body_images.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(body_images, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'body_images.started')
            body_images.setAutoDraw(True)
            body_images.play()
        if body_images.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > body_images.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                body_images.tStop = t  # not accounting for scr refresh
                body_images.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'body_images.stopped')
                body_images.setAutoDraw(False)
                body_images.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in body_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "body_trial" ---
    for thisComponent in body_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    body_images.stop()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.500000)
    
    # --- Prepare to start Routine "resp" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    respComponents = [resp_angry, resp_happy, resp_neutral, mouse]
    for thisComponent in respComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "resp" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *resp_angry* updates
        if resp_angry.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp_angry.frameNStart = frameN  # exact frame index
            resp_angry.tStart = t  # local t and not account for scr refresh
            resp_angry.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_angry, 'tStartRefresh')  # time at next scr refresh
            resp_angry.setAutoDraw(True)
        
        # *resp_happy* updates
        if resp_happy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp_happy.frameNStart = frameN  # exact frame index
            resp_happy.tStart = t  # local t and not account for scr refresh
            resp_happy.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_happy, 'tStartRefresh')  # time at next scr refresh
            resp_happy.setAutoDraw(True)
        
        # *resp_neutral* updates
        if resp_neutral.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp_neutral.frameNStart = frameN  # exact frame index
            resp_neutral.tStart = t  # local t and not account for scr refresh
            resp_neutral.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_neutral, 'tStartRefresh')  # time at next scr refresh
            resp_neutral.setAutoDraw(True)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
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
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([resp_angry, resp_happy, resp_neutral])
                        clickableList = [resp_angry, resp_happy, resp_neutral]
                    except:
                        clickableList = [[resp_angry, resp_happy, resp_neutral]]
                    for obj in clickableList:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in respComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "resp" ---
    for thisComponent in respComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for practice_loop_body (TrialHandler)
    practice_loop_body.addData('mouse.x', mouse.x)
    practice_loop_body.addData('mouse.y', mouse.y)
    practice_loop_body.addData('mouse.leftButton', mouse.leftButton)
    practice_loop_body.addData('mouse.midButton', mouse.midButton)
    practice_loop_body.addData('mouse.rightButton', mouse.rightButton)
    practice_loop_body.addData('mouse.time', mouse.time)
    practice_loop_body.addData('mouse.clicked_name', mouse.clicked_name)
    # the Routine "resp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'practice_loop_body'


# --- Prepare to start Routine "begin_trial" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
begin_resp.keys = []
begin_resp.rt = []
_begin_resp_allKeys = []
# keep track of which components have finished
begin_trialComponents = [begin_txt, begin_resp]
for thisComponent in begin_trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "begin_trial" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *begin_txt* updates
    if begin_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        begin_txt.frameNStart = frameN  # exact frame index
        begin_txt.tStart = t  # local t and not account for scr refresh
        begin_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin_txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'begin_txt.started')
        begin_txt.setAutoDraw(True)
    
    # *begin_resp* updates
    waitOnFlip = False
    if begin_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        begin_resp.frameNStart = frameN  # exact frame index
        begin_resp.tStart = t  # local t and not account for scr refresh
        begin_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'begin_resp.started')
        begin_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(begin_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(begin_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if begin_resp.status == STARTED and not waitOnFlip:
        theseKeys = begin_resp.getKeys(keyList=['space'], waitRelease=False)
        _begin_resp_allKeys.extend(theseKeys)
        if len(_begin_resp_allKeys):
            begin_resp.keys = _begin_resp_allKeys[-1].name  # just the last key pressed
            begin_resp.rt = _begin_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in begin_trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "begin_trial" ---
for thisComponent in begin_trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if begin_resp.keys in ['', [], None]:  # No response was made
    begin_resp.keys = None
thisExp.addData('begin_resp.keys',begin_resp.keys)
if begin_resp.keys != None:  # we had a response
    thisExp.addData('begin_resp.rt', begin_resp.rt)
thisExp.nextEntry()
# the Routine "begin_trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trial_two_loop = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('fpbody.xlsx'),
    seed=None, name='trial_two_loop')
thisExp.addLoop(trial_two_loop)  # add the loop to the experiment
thisTrial_two_loop = trial_two_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_two_loop.rgb)
if thisTrial_two_loop != None:
    for paramName in thisTrial_two_loop:
        exec('{} = thisTrial_two_loop[paramName]'.format(paramName))

for thisTrial_two_loop in trial_two_loop:
    currentLoop = trial_two_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_two_loop.rgb)
    if thisTrial_two_loop != None:
        for paramName in thisTrial_two_loop:
            exec('{} = thisTrial_two_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "body_trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    body_images.setMovie(body_file)
    # keep track of which components have finished
    body_trialComponents = [body_images]
    for thisComponent in body_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "body_trial" ---
    while continueRoutine and routineTimer.getTime() < 1.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *body_images* updates
        if body_images.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            body_images.frameNStart = frameN  # exact frame index
            body_images.tStart = t  # local t and not account for scr refresh
            body_images.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(body_images, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'body_images.started')
            body_images.setAutoDraw(True)
            body_images.play()
        if body_images.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > body_images.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                body_images.tStop = t  # not accounting for scr refresh
                body_images.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'body_images.stopped')
                body_images.setAutoDraw(False)
                body_images.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in body_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "body_trial" ---
    for thisComponent in body_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    body_images.stop()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.500000)
    
    # --- Prepare to start Routine "resp" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    respComponents = [resp_angry, resp_happy, resp_neutral, mouse]
    for thisComponent in respComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "resp" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *resp_angry* updates
        if resp_angry.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp_angry.frameNStart = frameN  # exact frame index
            resp_angry.tStart = t  # local t and not account for scr refresh
            resp_angry.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_angry, 'tStartRefresh')  # time at next scr refresh
            resp_angry.setAutoDraw(True)
        
        # *resp_happy* updates
        if resp_happy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp_happy.frameNStart = frameN  # exact frame index
            resp_happy.tStart = t  # local t and not account for scr refresh
            resp_happy.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_happy, 'tStartRefresh')  # time at next scr refresh
            resp_happy.setAutoDraw(True)
        
        # *resp_neutral* updates
        if resp_neutral.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp_neutral.frameNStart = frameN  # exact frame index
            resp_neutral.tStart = t  # local t and not account for scr refresh
            resp_neutral.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_neutral, 'tStartRefresh')  # time at next scr refresh
            resp_neutral.setAutoDraw(True)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
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
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([resp_angry, resp_happy, resp_neutral])
                        clickableList = [resp_angry, resp_happy, resp_neutral]
                    except:
                        clickableList = [[resp_angry, resp_happy, resp_neutral]]
                    for obj in clickableList:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in respComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "resp" ---
    for thisComponent in respComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trial_two_loop (TrialHandler)
    trial_two_loop.addData('mouse.x', mouse.x)
    trial_two_loop.addData('mouse.y', mouse.y)
    trial_two_loop.addData('mouse.leftButton', mouse.leftButton)
    trial_two_loop.addData('mouse.midButton', mouse.midButton)
    trial_two_loop.addData('mouse.rightButton', mouse.rightButton)
    trial_two_loop.addData('mouse.time', mouse.time)
    trial_two_loop.addData('mouse.clicked_name', mouse.clicked_name)
    # the Routine "resp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'trial_two_loop'


# --- Prepare to start Routine "end_exp" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
end_expComponents = [end_exp_txt]
for thisComponent in end_expComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "end_exp" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_exp_txt* updates
    if end_exp_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_exp_txt.frameNStart = frameN  # exact frame index
        end_exp_txt.tStart = t  # local t and not account for scr refresh
        end_exp_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_exp_txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_exp_txt.started')
        end_exp_txt.setAutoDraw(True)
    if end_exp_txt.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_exp_txt.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            end_exp_txt.tStop = t  # not accounting for scr refresh
            end_exp_txt.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_exp_txt.stopped')
            end_exp_txt.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_expComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "end_exp" ---
for thisComponent in end_expComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
