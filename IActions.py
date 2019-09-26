import abc


class IActions(abc.ABC):
    """An interface that describes what actions a game participant can perform"""
    @abc.abstractmethod
    def deals_damage(self, min_range, max_range):
        """Damage method"""
        pass

    @abc.abstractmethod
    def use_first_aid_kit(self, min_low_range, max_low_range):
        """Health Recovery Method"""
        pass
