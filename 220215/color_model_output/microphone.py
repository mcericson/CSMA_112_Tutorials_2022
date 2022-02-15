default_max =  0.5
sensitivity = 2.0

def initialize(sketch, AudioIn, Amplitude):
    global ampl
    mic = AudioIn(sketch,0)
    mic.start()
    ampl = Amplitude(sketch)
    ampl.input(mic)



def get_level():
    input_level = ampl.analyze()
    new_max = default_max*sensitivity 
    adjusted_level = map(input_level,0,default_max,0,new_max)
    
    return adjusted_level
