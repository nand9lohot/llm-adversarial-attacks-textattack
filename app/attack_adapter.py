import torch

from textattack.models.wrappers import ModelWrapper

from app.model_service import model_service


class AttackAdapter(ModelWrapper):

    def __init__(self):

        # TextAttack expects a model attribute
        self.model = model_service.model

    def __call__(self, text_inputs):

        outputs = []

        for text in text_inputs:

            result = model_service.predict(text)

            negative_prob = result["probabilities"]["negative"]
            positive_prob = result["probabilities"]["positive"]

            outputs.append([negative_prob, positive_prob])

        return torch.tensor(outputs)