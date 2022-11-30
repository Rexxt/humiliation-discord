from discord import Client
class UserPronouns:
    def __init__(self, bot: Client, id: int):
        """Helper class to make use of a saved user's pronouns.

        Args:
            bot (Client): The HUMILIATION instance to use.
            id (int): The id of the requested user.
        """
        self.bot = bot
        self.user_id = id
        
        self.user_data = self.bot.get_user_data(self.user_id, 'pronouns')
        self.use(0)

    def get_set_number(self):
        return len(self.user_data)
    
    def use(self, set_number: int):
        self.subjective = self.user_data[set_number]['subjective']
        self.objective = self.user_data[set_number]['objective']
        self.possessive_determiner = self.user_data[set_number]['posdet']
        self.possessive_pronoun = self.user_data[set_number]['posprn']
        self.reflexive = self.user_data[set_number]['reflexive']
        self.conjugation = self.user_data[set_number]['conjug']

class UndefPronouns(UserPronouns):
    def __init__(self, sets: list[dict]):
        """Helper class to make use of specified pronouns.

        Args:
            sets (list[dic]): The sets of pronouns to use.
        """
        self.user_data = sets
        self.use(0)