class PannelloFotovoltaico:
    def __init__(self, codice: str, modello: str, potenza_kw: float) -> None:
        self.codice = codice
        self.modello = modello
        
        try:
            self.potenza_kw = potenza_kw
        except potenza_kw < 0.0:
            AttributeError("Il valore della potenza non può essere negativo")
    
    def __str__(self) -> str:
        return f"Codice: {self.codice}. Modello: {self.modello}. Potenza(in kw): {self.potenza_kw}"
    