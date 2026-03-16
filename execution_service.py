class ExecutionService:

    def execute(self, code, test_input):

        try:
            local_vars = {}

            exec(code, {}, local_vars)

            if "solution" in local_vars:
                return local_vars["solution"](test_input)

            return "No solution function"

        except Exception as e:
            return str(e)
