# pip install -r requirements.txt

try:
    import numpy as np                # this needs no expl
    import scipy.signal as sig        #
    import matplotlib.pyplot as plt
    import itertools                  # used to iterate over all combinations of parameters for a certain plot
    # alternative: plotly - also for jupyterLab

    import os.path                    # used to check if certain files exists

    ## WAV files
    import scipy.io.wavfile as wavf
    import IPython.display as ipd     # used to construct display elements. ipd.display == display (which is imported by default in Jupyter Lab)
    import warnings                   # used to ignore some warnings in WAV-file reading
    warnings.simplefilter(action='ignore', category=wavf.WavFileWarning)
except ModuleNotFoundError as exc:
    # raise new exception, but keep the old one around
    raise Exception("One of the modules we tried to import does not exist on your system, please examine the original error to install the right module and reload your kernel") from exc

#Code to read WAV file into an array
def getSpeechFragment(file_path):
    if os.path.isfile(file_path):
        _, wav = wavf.read(file_path)
#         maxi = abs(np.iinfo(wav.dtype).min)    #maximum analog value -- assume abs(ii16.min) > ii16.max
#         return wav/maxi               #absolute normalisation to [-1,1]
        maxi = np.max(abs(wav))
        return wav/maxi               #absolute normalisation to [-1,1]
    else:
        raise Exception("This isn't a valid audio file (doesn't exist)")
def setSpeechFragment(name, signal):
    """
    Make sure importstatements.audiofolder and importstatements.Fs are defined
    """
    try:
        audiofolder
        Fs
    except NameError:
        raise Exception("audiofolder or sampling frequency was not set")
    if os.path.isdir(audiofolder):
        #convert to audiofile
        file_path = audiofolder + name + ".wav"
        wavf.write(file_path, Fs, signal)
        print("Write to {} with sampling freq = {} Hz".format(file_path, Fs))
    else:
        raise Exception("The audiofolder doesn't exist")

## Random generator
rng = np.random.default_rng()

## HTML/CSS styling
def css_styling():
    css_file = "assets/styles/custom.css"
    if os.path.isfile(css_file):
        return ipd.display(ipd.HTML(open(css_file,'r').read()))
    else:
        raise ValueError("The custom CSS is not installed, which would limit the exercise experience...")

## Latex/MathJax styling
def latex_macros():
    latex_file = "assets/styles/presentation_macros.tex"
    if os.path.isfile(latex_file):
        return ipd.display(ipd.Latex(filename=latex_file))
    else:
        raise ValueError("The custom latex macros are not installed, which would limit the exercise experience...")

# execute them
def notebook_styling():
    css_styling()
    latex_macros()


# or simpleaudio
# https://realpython.com/playing-and-recording-sound-python/

## Plot parameters
#plt.ioff()                        # interactive mode off -- this means you need plt.show() to show the plots
#plt.rcParams['figure.figsize'] = [12, 8]
#plt.rcParams.update({'font.size': 22})
