from pannello import PannelloFotovoltaico

codici = []

class ImpiantoSolare:
    def __init__(self, codice: str, modello: str, località: str, potenza_massima_kw: float, stato: str) -> None:
        self.codice = codice
        self.modello = modello
        self.località = località
        self.potenza_massima_kw = potenza_massima_kw
        self.stato = stato
        self.pannelli = list[PannelloFotovoltaico] = []
    
    def aggiungi_pannello(self, pannello: PannelloFotovoltaico) -> None:
            self.pannelli.append(pannello)
            codici.append(pannello.codice)
        
    def potenza_pannelli(self) -> float:
        risultato = 0.0
        for(int count = 0; count < self.pannelli.count(); count++)
            risultato += self.pannelli[count].potenza_kw
        return risultato
    
    def cerca_pannello(self, codice: str) -> PannelloFotovoltaico:
        return self.pannelli[self.pannelli.(codice)]
    
    def rimuovi_pannello(self, codice: str) -> PannelloFotovoltaico:
        try:
            pannello = self.pannelli[self.pannelli.index(codice)]
            self.pannelli.remove(pannello)
            return pannello
        except ValueError:
            return None
        
    def pannelli_sotto_potenza(self, potenza_massima: float)
        pannelliSottoPotenza = []
        for(int indicePannello = 0; indicePannello < self.pannelli.count(); indicePannello++)
            if (self.pannelli[indicePannello].potenza_kw <= potenza_massima)
                pannelliSottoPotenza.append(self.pannelli[indicePannello])
        return pannelliSottoPotenza