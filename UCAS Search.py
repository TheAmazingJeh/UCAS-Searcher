import json, sys
from requests import post as rPost
class UCAS_handler:
    def __init__(self):
        self.uniInput = ""
        self.uniName = ""
        self.subjectInput = ""
        self.subjectName = ""

    def search_ucas(self, searchTerm):
        """
        Searches UCAS for the input.

        Will return a dictionary with the keys `courseTitles`, `locations`, `providers` and `subjects`
        """

        url = "https://services.ucas.com/search/api/v2/autocomplete"
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"

        data = json.dumps({"searchTerm": searchTerm})
        return dict(rPost(url, headers=headers, data=data).json())
def main():
    # Create UCAS_handler object
    handler = UCAS_handler()
if __name__ == "__main__":
    main()