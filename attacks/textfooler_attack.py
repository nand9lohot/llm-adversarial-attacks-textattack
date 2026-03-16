from textattack.attack_recipes import TextFoolerJin2019


class TextFoolerAttack:

    name = "textfooler"

    description = "Word substitution attack using semantic similarity"

    mitre_atlas = "AML.T0040"

    nist_rmf = "MEASURE"

    @staticmethod
    def build(model_wrapper):
        return TextFoolerJin2019.build(model_wrapper)