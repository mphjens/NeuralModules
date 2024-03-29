class NeuralModule:
    def __init__(self):
        self.initialized = False
        self.outputlabels = []

    def initializeModule(self):
        self.model = self.createModel()
        self.model.load_weights(self.weight_path)
        print ("I: Loaded NeuralModule: " + self.mod_name)


    def createModel(self):
        raise NotImplementedError("E: You should implement CreateModel() in your NeuralModule")

    def inTransform(self, input):
        raise NotImplementedError("E: You should implement inTransform() in your NeuralModule")

    def outTransform(self, rawoutput):
        raise NotImplementedError("E: You should implement outTransform() in your NeuralModule")

    def predict(self, input):
        try:
            predictions = self.outTransform(self.model.predict(self.inTransform(input), verbose=0))
            if(len(self.outputlabels) != len(predictions[0])):
                print "INFO: Number of output labels does not correspond with the number of predicted values. Output labels not used."
                return predictions.tolist()

            retVal = []
            for pred in predictions:
                plist = pred.tolist()
                cRow = {}
                for idx, cVal in enumerate(plist):
                    cRow[self.outputlabels[str(idx)]] = cVal

                retVal.append(cRow)

            return retVal
        except:
           return None

    def predict_string(self, input):
        return str(self.predict(input))

    def predictsingle_string(self, input):
        retVal = str(self.predict([input]))
        return retVal