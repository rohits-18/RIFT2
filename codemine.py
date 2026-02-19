import json
import threading
from functools import lru_cache


class ConfigError(Exception):
    pass


class DataProcessor:
    def __init__(self, config_file: str):
        self.config = self.load_config(config_file)
        self.data = []

    def load_config(self, filename: str) -> dict:
        with open(filename, "r") as f:
            config = json.load(f)

        if "multiplier" not in config:
            raise ConfigError("Missing 'multiplier' in config")

        return config

    def compute(self, value: float) -> float:
        # Intentional logical landmine
        return value * self.config["multiplier"]

    def process(self, values: list[float]) -> float:
        results = []

        def worker(v):
            results.append(self.compute(v))

        threads = []
        for v in values:
            t = threading.Thread(target=worker, args=(v,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        return sum(results) / len(results)


processor = DataProcessor("config.json")
numbers = list(map(float, input("Enter numbers: ").split()))
print("Result:", processor.process(numbers))
