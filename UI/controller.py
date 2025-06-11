import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self, e):
        self._view.txt_result.controls.clear()
        cMin = self._view._txtInCMin.value
        if cMin is None or cMin == "":
            self._view.create_alert("Inserire il numero minimo di compagnie")
            return
        try:
            int(cMin)
        except ValueError:
            self._view.create_alert("La distanza minima deve essere un intero!")
            return

        self._model.buildGraph(int(cMin))
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato!\n"
                                                      f"con {self._model.getNum()[0]} vertici "
                                                      f"e {self._model.getNum()[1]} archi"))
        self.fillDDAeroporti()
        self._view.update_page()

    def fillDDAeroporti(self):
        for n in self._model.getNodes():
            self._view._ddAeroportoP.options.append(ft.dropdown.Option(
                text = n.IATA_CODE,
                data = n, on_click = self.readDDPartenza
            ))

        for n in self._model.getNodes():
            self._view._ddAeroportoD.options.append(ft.dropdown.Option(
                text = n.IATA_CODE,
                data = n, on_click = self.readDDDestinazione
            ))
        self._view.update_page()

    def readDDPartenza(self, e):
        self._aeroportoP = e.control.data

    def readDDDestinazione(self, e):
        self._aeroportoD = e.control.data

    def handleConnessi(self, e):
        vicini = self._model.handleConnessi(self._aeroportoP)
        for v in vicini:
            self._view.txt_result.controls.append(ft.Text(f"{v[0].AIRPORT} - {v[1]}"))

        self._view.update_page()

    def handlePercorso(self, e):
        pass

    def handleCerca(self, e):
        pass
