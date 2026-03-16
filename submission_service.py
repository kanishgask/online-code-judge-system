class SubmissionService:

    def __init__(self):
        self.submissions = []
        self.submission_id = 0

    def submit_code(self, user_id, problem_id, code):

        self.submission_id += 1

        submission = {
            "submission_id": self.submission_id,
            "user_id": user_id,
            "problem_id": problem_id,
            "code": code,
            "status": "SUBMITTED"
        }

        self.submissions.append(submission)

        return submission

    def get_submissions(self):

        return self.submissions
