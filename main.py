print("!!! CODES SIGNAL: THIS IS THE NEW UPDATED VERSION !!!")
import json, unittest, datetime

# Open and read the three json files with explicit UTF-8 encoding to prevent Windows crash
with open("./data-1.json", "r", encoding="utf-8") as f:
    jsonData1 = json.load(f)
with open("./data-2.json", "r", encoding="utf-8") as f:
    jsonData2 = json.load(f)
with open("./data-result.json", "r", encoding="utf-8") as f:
    jsonExpectedResult = json.load(f)


# Convert json data from format 1 to the expected format
def convertFromFormat1(jsonObject):
    # Smart Check: If location is already a list, use it. If it's a string, split it.
    if isinstance(jsonObject.get("location"), list):
        locationParts = jsonObject["location"]
    else:
        locationParts = jsonObject["location"].split("/")

    # Create a new dictionary matching the unified schema exactly
    result = {
        'deviceID': jsonObject['deviceID'],
        'deviceType': jsonObject['deviceType'],
        'timestamp': jsonObject['timestamp'],
        'location': {
            'country': locationParts,
            'city': locationParts,
            'area': locationParts,
            'factory': locationParts,
            'section': locationParts
        },
        'data': {
            'status': jsonObject['operationStatus'],
            'temperature': jsonObject['temp']
        }
    }
    return result


# Convert json data from format 2 to the expected format
def convertFromFormat2(jsonObject):
    # Parse the ISO 8601 timestamp string to a datetime object
    data = datetime.datetime.strptime(jsonObject['timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ')
    # Convert that datetime object to milliseconds since epoch
    timestamp = round((data - datetime.datetime(1970, 1, 1)).total_seconds() * 1000)

    # Create a new dictionary matching the unified schema exactly
    result = {
        'deviceID': jsonObject['device']['id'],
        'deviceType': jsonObject['device']['type'],
        'timestamp': timestamp,
        'location': {
            'country': jsonObject['country'],
            'city': jsonObject['city'],
            'area': jsonObject['area'],
            'factory': jsonObject['factory'],
            'section': jsonObject['section']
        },
        'data': jsonObject['data']
    }
    return result


def main(jsonObject):
    result = {}
    # Route the data to the correct parser depending on the model format
    if jsonObject.get('device') == None:
        result = convertFromFormat1(jsonObject)
    else:
        result = convertFromFormat2(jsonObject)
    return result


# Test cases using unittest module
class TestSolution(unittest.TestCase):

    # Sanity test to ensure the expected result matches itself
    def test_sanity(self):
        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(result, jsonExpectedResult)

    # Test conversion of format 1
    def test_dataType1(self):
        result = main(jsonData1)
        self.assertEqual(result, jsonExpectedResult, 'Converting from Type 1 failed')

    # Test conversion of format 2
    def test_dataType2(self):
        result = main(jsonData2)
        self.assertEqual(result, jsonExpectedResult, 'Converting from Type 2 failed')


if __name__ == '__main__':
    # Execute the unit tests
    unittest.main()