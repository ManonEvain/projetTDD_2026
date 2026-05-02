import csv
import os


class CSVExporter:

    def export_animals(self, file_path: str, animals):
        if not animals:
            print("Il n'y a aucun animaux dans la ferme")
            return

        directory = os.path.dirname(file_path)

        if directory:
            os.makedirs(directory, exist_ok=True)

        with open(file_path, mode="w", newline="", encoding="utf-8") as f:

            writer = csv.writer(f)

            # headers simples
            writer.writerow(["name", "age", "type"])

            for animal in animals:

                animal_type = animal.__class__.__name__.lower()

                writer.writerow([
                    animal.name,
                    animal.age,
                    animal_type
                ])
    
    def export_combats(self, file_path: str, combats):
        if not combats:
            print("Il n'y a aucun combat dans la ferme")
            return

        directory = os.path.dirname(file_path)

        if directory:
            os.makedirs(directory, exist_ok=True)

        with open(file_path, mode="w", newline="", encoding="utf-8") as f:

            writer = csv.writer(f)

            # headers simples
            writer.writerow(["adversaire1", "adversaire2", "score1", "score2"])

            for combat in combats:

                writer.writerow([
                    str(combat.adversaire1.name),
                    str(combat.adversaire2.name),
                    combat.score1,
                    combat.score2
                ])