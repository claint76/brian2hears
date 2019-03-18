from brian2 import *
from brian2hears import *

def test_basic_filterbanks():
    #sound = whitenoise(100*ms)
    sound = tone(100*Hz, 100*ms)
    # res = FunctionFilterbank(sound, lambda x: abs(x)).process()
    res = Gammatone(sound, erbspace(50*Hz, 200*Hz, 4)).process()
    plot(sound.times/ms, res)
    show()

def test_filterbankgroup():
    sound1 = tone(1 * kHz, .1 * second)
    sound2 = whitenoise(.1 * second)
    sound = sound1 + sound2
    sound = sound.ramp()
    cf = erbspace(20 * Hz, 20 * kHz, 3000)
    cochlea = Gammatone(sound, cf)
    # Half-wave rectification and compression [x]^(1/3)
    ihc = FunctionFilterbank(cochlea, lambda x: 3 * clip(x, 0, Inf) ** (1.0 / 3.0))
    # Leaky integrate-and-fire model with noise and refractoriness
    eqs = '''
    dv/dt = (I-v)/(1*ms)+0.2*xi*(2/(1*ms))**.5 : 1 (unless refractory)
    I : 1
    '''
    anf = FilterbankGroup(ihc, 'I', eqs, reset='v=0', threshold='v>1', refractory=5*ms)
    M = SpikeMonitor(anf)
    run(sound.duration)
    plot(M.t/ms, M.i, ',k')
    show()


if __name__=='__main__':
    test_basic_filterbanks()
    #test_filterbankgroup()