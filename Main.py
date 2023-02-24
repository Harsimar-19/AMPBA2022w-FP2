class EnergyForecastModel():
    def __init__(self, model, features, rmse, r2square):
        self.model = model
        self.features = features
        self.rmse = rmse
        self.r2square = r2square


def main():
    #mlModel = pmd.FetchModel()
    sud.PublishHeading()
    sud.PublishSideBars(mlModel)

if __name__ == '__main__':
    #import PickledModelDetails as pmd
    import StreamlitUIDetails as sud
    main()
