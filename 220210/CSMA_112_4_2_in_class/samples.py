
samples = []
buffer_size = 8

def add_sample(val):
    samples.append(val)
    if len(samples) == buffer_size:
        samples.pop(0)
        
def get_smoothed():
    return sum(samples) / len(samples)
