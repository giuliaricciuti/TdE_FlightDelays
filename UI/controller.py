import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self, e):
        cMinTxt= self._view._txtInCMin.value
        if cMinTxt == "":
            #inserisci!!!
            return
        try:
            cMin = int(cMinTxt)
        except ValueError:
            #self._view.txt_result.controls.append()
            return

        if cMin<=0:
            #stampa inserisci valore positivo
            return

        self._model.buildGraph()
        nNodes, nEdges = self._model.getGraphDetails()
        #stampa su txt_result

    def handleConnessi(self, e):
        pass

    def handleCerca(self, e):
        pass

