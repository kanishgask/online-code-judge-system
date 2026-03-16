class EvaluationService:

    def evaluate(self, output, expected):

        if output == expected:
            return "PASS"

        return "FAIL"
