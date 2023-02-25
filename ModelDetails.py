import pickle

def FetchModel():
    b = ''
    with open('./FinalPickleFile.pickle', 'rb') as handle:
        b = pickle.load(handle)
    return b