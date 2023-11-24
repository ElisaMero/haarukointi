class Cite:  # pylint: disable=too-few-public-methods
    """Luokka, joka kuvaa viitettä.

    Attributes:
        id (str): Viitteen tunnus.
        type (str): Viitteen tyyppi.
        authors: (list[str]): Viitteen tekijät.
        fields (dict): Viitteen kentät.
    """

    def __init__(self, id: str, type: str, authors: list[str], fields: dict = {}) -> None:
        """Luokan konstruktori

        Args:
            id (str): Viitteen tunnus.
            type (str): Viitteen tyyppi.
            authors: (list[str]): Viitteen tekijät.
            fields (dict): Viitteen kentät.
        """

        self.id: str = id
        self.type: str = type
        self.authors: list[str] = authors
        self.fields: dict = fields

    def __str__(self) -> str:
        """Palauttaa luokan merkkijonona

        Returns:
            str: Luokka merkkijonona.
        """

        return f"{self.id} - {self.type} - {self.fields}"
