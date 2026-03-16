from textattack.attack_recipes import DeepWordBugGao2018


class DeepWordBugAttack:

    name = "deepwordbug"

    description = "Character-level adversarial perturbation"

    mitre_atlas = "AML.T0043"

    nist_rmf = "MEASURE"

    @staticmethod
    def build(model_wrapper):
        return DeepWordBugGao2018.build(model_wrapper)