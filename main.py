import stravalib
import requests

from stravalib.client import Client

def execute():
	access_token = "83ebeabdec09f6670863766f792ead24d61fe3f9"
	bounds = "-6.5754340,39.5643222,-7.0693569,39.0156433e"

	segments = get_explore_segments(access_token, bounds )

	if "Problem" not in segments:
		write(segments)
	else:
		print segments

def get_client_activities(access_token, limit):

	client = Client(access_token=ACCESS_TOKEN)

	activities = client.get_activities(limit=limit)
	return activities

def get_explore_segments(access_token, bounds):
	url = "https://www.strava.com/api/v3/segments/explore"
	url = url + '?bounds='+ str(bounds) + '&access_token=' + \
	str(access_token)
	response = requests.get(url)

	if response.status_code is 200:
		return response.content
	else:
		return "Problem in retrieveing data "+ \
		str(response.status_code)

def write(segments):

    with open("data/result", "a") as res_file:
    	res_file.write(segments)

if __name__ == "__main__":
    execute()

