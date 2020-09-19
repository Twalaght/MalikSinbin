#!/usr/bin/python3

import sys
import requests
from bs4 import BeautifulSoup
from pathlib import Path

# Generate a dictionary of file names and their URL
def download_dict_gen(links):
	# Dictionary of the form {name : url}, and list of unique names
	file_dict = {}
	unique_names = []

	# Process every link in our input
	for url in links:
		# Separate file name from full url
		name = url.rsplit("/")[-1]

		# While we do not have a unique name, increase the iterator until we do
		n = 1
		while name in unique_names:
			title = name.split(".")
			ext = title[-1]
			title = title[:-1]
			title.append(f"({n})")
			temp = "".join(title) + "." + ext
			if temp not in unique_names:
				name = temp
			n += 1

		# Add to the list of unique names, and build its dictionary entry
		unique_names.append(name)
		file_dict[f"{name}"] = url

	# Return our complete file dictionary
	return file_dict

# TODO - Archaic way of downloading, but seems be all that works for now
def save_files(file_dict, name):
	n = 1
	for file_name, url in file_dict.items():
		img_path = Path.cwd() / "Downloads" / name / file_name

		print(f"[{n}/{len(file_dict)}] Downloading {file_name}...")

		if not img_path.exists():
			in_file = requests.get(url, stream=True)
			if in_file.ok:
				with open(img_path, "wb") as f:
					for chunk in in_file.iter_content(chunk_size=8192):
						f.write(chunk)

		n += 1

# Collect all downloadable content links
def get_links(soup, filter_type=None, filter_list=None):
	# Find all "a" tags in the webpage soup
	links = soup.find_all("a")
	temp_links = []

	# Sanitise every "a" tag that has been collected
	for link in links:
		href = link.get("href")
		if href is None:
			continue

		# TODO - May remove if we ditch the filters
		if (filter_type == "bl"):
			if href.split('.')[-1] in filter_list:
				continue
		elif (filter_type == "wh"):
			if href.split('.')[-1] not in filter_list:
				continue

		# Fix any links that require a prefix
		if "patreon_inline" in href:
				temp_links.append("https://data.yiff.party" + href)
		elif "patreon_data" in href:
				temp_links.append(href)

	# Return the list of collected links
	return temp_links


def download_manager(name, links):
	# Ensure there is a folder to save files
	Path(Path.cwd() / "Downloads").mkdir(parents=True, exist_ok=True)

	# Generate a dictionary of file names and their URL
	file_dict = download_dict_gen(links)


	# Check if a folder for this creator exists already
	if Path(f"Downloads/{name}").exists():
		print(f"[ Existing files for {name} found, updating them... ]")
	else:
		Path(f"Downloads/{name}").mkdir()

	save_files(file_dict, name)


def project_links_scraper(creator_code):
	# TODO
	blacklist_extensions = ["rar", "zip"]
	whitelist_extensions = ["png", "jpg", "gif", "mp4"]
	filter_type='bl'
	filter_list=blacklist_extensions
	# TODO

	# Set some required variables then iterate over each of the creators content pages
	page = 1
	links = []
	url = "https://yiff.party/patreon/" + creator_code + "?p="
	while True:
		# Parse the given page into searchable soup
		soup = BeautifulSoup(requests.get(url + str(page)).content, "html.parser")

		# On the initial page, set the name, total pages, and display status messages
		if page == 1:
			creator_name = soup.find_all("span", {"class": "yp-info-name"})[0].text
			page_element = soup.find_all("p", {"class": "paginate-count"})[0].text
			total_pages = int(page_element.split("/")[1])
			print(f"[ Starting {creator} : {creator_name} ]")

		# Display a status message and collect all downloadable content links
		print(f"- Processing page {page} of {total_pages}")
		links += get_links(soup, filter_type=filter_type, filter_list=filter_list)

		# TODO - Make this an input variable
		# Exit when each page has been parsed, otherwise increment to the next page
		if page == total_pages: break
		else: page += 1

	# Display a status messages, sanitize the links, and download them
	print(f"[ Found {len(links)} links for {creator_name} ]")
	download_manager(creator_name, links)
	print(f"[ Finished {creator_name} ]")

# Iterate over each given argument
for creator in sys.argv[1:]: project_links_scraper(creator)
print("[ All creators finished ]")
