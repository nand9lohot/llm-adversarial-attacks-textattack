import os
import subprocess

from textattack.datasets import Dataset
from textattack import Attacker, AttackArgs

from app.attack_adapter import AttackAdapter

from attacks.textfooler_attack import TextFoolerAttack
from attacks.bert_attack import BertAttack
from attacks.deepwordbug_attack import DeepWordBugAttack


class AttackEngine:

    def __init__(self):

        # Ensure reports directory exists
        os.makedirs("reports", exist_ok=True)

        self.model_wrapper = AttackAdapter()

        self.examples = [
            ("This movie is fantastic and inspiring", 1),
            ("The plot was dull and poorly written", 0),
            ("I loved the cinematography and acting", 1),
            ("The film was painfully boring", 0),
        ]

        self.attacks = [
            TextFoolerAttack,
            BertAttack,
            DeepWordBugAttack,
        ]

    def dataset(self):
        return Dataset(self.examples)

    def run(self):

        dataset = self.dataset()

        for attack_class in self.attacks:

            print(f"\nRunning attack: {attack_class.name}")

            attack = attack_class.build(self.model_wrapper)

            args = AttackArgs(
                num_examples=len(self.examples),
                log_to_csv=f"reports/{attack_class.name}_results.csv",
                disable_stdout=False,
            )

            attacker = Attacker(attack, dataset, args)

            try:
                attacker.attack_dataset()
            except Exception as e:
                print(f"Attack {attack_class.name} failed: {e}")

        self.generate_report()

    def generate_report(self):

        report_script = "scripts/generate_html_report.py"

        if not os.path.exists(report_script):
            print("Report generator not found, skipping report generation.")
            return

        print("\nGenerating HTML report...")

        try:
            subprocess.run(
                ["python", report_script],
                check=True
            )
        except subprocess.CalledProcessError as e:
            print(f"Report generation failed: {e}")


def main():

    engine = AttackEngine()
    engine.run()


if __name__ == "__main__":
    main()