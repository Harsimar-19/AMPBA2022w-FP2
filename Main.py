class EnergyForecastModel():
    def __init__(self, model):
        self.model = model


def main():
    ForecastModel = md.FetchModel()
    sud.PublishHeading()
    sud.PublishSideBars(ForecastModel)
    

if __name__ == '__main__':
    import StreamlitUIDetails as sud
    import ModelDetails as md
    main()