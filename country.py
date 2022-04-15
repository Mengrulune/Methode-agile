from dataclasses import dataclass, field

@dataclass
class Country():
    name: str = 'France'
    gdp: int = 2_000_000_000
    surface : int = 543000
    towns: list = field(default_factory=list)

    def gdp_country(self):
        total_gdp = 0
        for town in self.towns:
            total_gdp += town.gdp_town()
        return total_gdp

    def add_towns(self, towns):
        for town in towns:
            town.country = self
            self.towns.append(town)

    def count_towns_over_word_average_gdp(self, word_average_gdp):
        count = 0
        for town in self.towns:
            if town.gdp_per_habitat > word_average_gdp:
                count += 1
        return count
    def set_population(self, population):
        self.population = population

    def calculate_density(self):
        return self.population / self.surface

