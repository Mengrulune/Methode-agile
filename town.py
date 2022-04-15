from pythonProject.country import Country
from dataclasses import dataclass

@dataclass
class Town():
    name : str = 'Paris'
    gdp_per_habitat : int = 38
    nb_habitats : int = 2_000_000
    country : Country = Country()

    def set_country(self, country):
        if self.country != country :
            self.country.towns.remove(self)
            self.country = country

    def gdp_town(self):
        return self.gdp_per_habitat * self.nb_habitats

    def contribution_in_gdp_country(self):
        return self.gdp_town() / self.country.gdp_country





