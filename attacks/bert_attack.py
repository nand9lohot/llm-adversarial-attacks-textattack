from textattack.attack_recipes import BERTAttackLi2020


class BertAttack:

    name = "bert_attack"

    description = "Masked language model adversarial substitution"

    mitre_atlas = "AML.T0042"

    nist_rmf = "MEASURE"

    @staticmethod
    def build(model_wrapper):
        return BERTAttackLi2020.build(model_wrapper)