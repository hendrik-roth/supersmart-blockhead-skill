"""Certificate Generator"""
import datetime


class CertificateGenerator:
    def __init__(self, answers, skill_path):
        self.answers = answers
        self.path = skill_path
        self.out_path = self.path + "/game/output"
        self.template = self.path + "/game/templates/certificate_generator.html"

    def generate_certificate(self):
        table = ""
        for q, a in self.answers.items():
            table += f"""
            <tr>
                <td>{q}</td>
                <td>{a}</td>
            </tr>
            """
        with open(self.template, "r") as template:
            data = template.readlines()
        html = [s.replace("#placeholder", table) for s in data]
        file = self.out_path + f"{datetime.datetime.now()}_results.html"
        with open(file, "w+") as outfile:
            outfile.write("".join(html))
        return file

