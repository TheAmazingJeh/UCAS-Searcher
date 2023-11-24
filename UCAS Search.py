import json, sys
from urllib.parse import urlencode
from webbrowser import open as open_browser
from requests.structures import CaseInsensitiveDict
from time import sleep
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

    def open_uni_page(self, NAME,SUBJECTS):    # Opens the UCAS page for the university.
        """
        Opens the UCAS page for the university.
        
        Requires the exact name of the university and subject to search for. (Use UCAS search to find these)
        """

        # Create the parameters for the URL
        params = {
            # Set the provider name to NAME
            "providers":NAME,
            # Set the subject name to SUBJECTS
            "subjects": SUBJECTS,

            # These parameters are required for the URL to work, assuming you want to search for undergraduate courses starting in 2023
            "studyYear": "2023",
            "destination": "Undergraduate",
            "postcodeDistanceSystem": "imperial",
            "pageNumber": "1",
            "sort": "MostRelevant",
            "clearingPreference": "NextYear"
        }
        open_browser(f"https://digital.ucas.com/coursedisplay/results/courses?{urlencode(params)}")

    def select_from_list(self, optionList):
        """
        Allows the user to select an option from a list of options using numbers.

        Returns the selected option.
        """
        # If there are no options, return False
        if optionList == []:
            print("No Match")
            return False
        
        # If there is only one option, return that option
        if len(optionList) == 1:
            print(f"Selected {optionList[0]}")
            return optionList[0]
        
        # If there are multiple options, ask the user to select one
        i=1
        for item in optionList: print(f"{i:2} - {item}"); i+=1
        course = input(f"Please select (1-{len(optionList)}): ")

        # If the user didn't select a valid option, return False
        if not course.isdigit() or int(course) > len(optionList) or int(course) < 1:
            print("Invalid Selection")
            return False
        
        # Return the selected option
        return optionList[int(course)-1]

def main():
    # Create UCAS_handler object
    handler = UCAS_handler()
if __name__ == "__main__":
    main()