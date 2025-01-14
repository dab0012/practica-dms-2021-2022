from sqlalchemy import Table, MetaData, Column, String
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer  # type: ignore
from dms2122backend.data.db.results.resultbase import ResultBase


class Answer(ResultBase):
    """ Class Answer
    """

    def __init__(self, questionId: int, answer:str, valoration:float, username:str):
        """ Constructor method.

        Initializes a user record.

        Args:
            - questionId (int): The question answered ID.
            - answer (str): A string with the answer.
            - valoration (str): A string with the valoration.
        """
        self.id: int = questionId
        self.answer: str =  answer
        self.valoration :float =  valoration
        self.username :str =  username


    @staticmethod
    def _table_definition(metadata: MetaData) -> Table:
        """ Gets the table definition.

        Args:
            - metadata (MetaData): The database schema metadata
                        (used to gather the entities' definitions and mapping)

        Returns:
            - Table: A `Table` object with the table definition.
        """
        return Table(
            'answers',
            metadata,
                Column('id', Integer, ForeignKey('questions.id') , primary_key=True) ,
                Column('answer', String(64), nullable=False),
                Column('valoration', Integer, nullable=False),
                Column('username', String(64), primary_key=True) 
        )

