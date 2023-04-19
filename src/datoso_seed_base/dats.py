from datoso.repositories.dat import ClrMameProDatFile, XMLDatFile

class BaseDat(XMLDatFile):
    seed: str = 'nointro'

    def initial_parse(self) -> list:
        """ Parse the dat file. """
        # pylint: disable=R0801
        self.preffix = ''
        self.company = ''
        self.system = ''
        self.suffix = ''
        self.date = ''

        return [self.preffix, self.company, self.system, self.suffix, self.get_date()]


    def get_date(self) -> str:
        """ Get the date from the dat file. """
        return self.date