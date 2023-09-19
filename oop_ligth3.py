class Cykel:
    def __init__(self, färg, typ) -> None:
        self._färg = färg
        self._typ = typ

    def get_färg(self):
        return self._färg
    
    def get_typ(self):
        return self._typ
    
    def set_färg(self, ny_färg):
        self._färg = ny_färg
    
class Bil:
    def __init__(self, färg, årsmodell, hästkrafter) -> None:
        self._färg = färg
        self._år = årsmodell
        self._hästkrafter = hästkrafter

    def get_färg(self):
        return self._färg
    
    def get_årsmodell(self):
        return self._år
    
    def get_hästkrafter(self):
        return self._hästkrafter

    def set_färg(self, ny_färg):
        self._färg = ny_färg

class Moped:
    def __init__(self, färg, typ, hästkrafter) -> None:
        self._färg = färg
        self._typ = typ
        self._hästkrafter = hästkrafter
        
    def get_färg(self):
        return self._färg
    
    def get_typ(self):
        return self._typ
    
    def get_hästkrafter(self):
        return self._hästkrafter
    
    def set_färg(self, ny_färg):
        self._färg = ny_färg    

class Traktor:
    def __init__(self, färg, årsmodell, hästkrafter) -> None:
        self._färg = färg
        self._år = årsmodell
        self._hästkrafter = hästkrafter

    def get_färg(self):
        return self._färg

    def get_årsmodell(self):
        return self._år

    def get_hästkrafter(self):
        return self._hästkrafter
    
    def set_färg(self, ny_färg):
        self._färg = ny_färg

