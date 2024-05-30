from datoso.repositories.dat_file import ClrMameProDatFile, XMLDatFile  # noqa: F401


class BaseDat(XMLDatFile):
    seed: str = 'Base'

    def initial_parse(self) -> list:
        """Parse the dat file."""
        # pylint: disable=R0801
        self.prefix = ''
        self.company = ''
        self.system = ''
        self.suffix = ''
        self.date = ''

        return [self.prefix, self.company, self.system, self.suffix, self.get_date()]


    def get_date(self) -> str:
        """Get the date from the dat file."""
        return self.date
