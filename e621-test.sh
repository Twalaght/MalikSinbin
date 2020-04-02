#!/bin/bash
curl --location --request GET 'https://e621.net/posts.json' \
--header 'User-Agent: TestBot' \
--header 'Authorization: Basic <B64 USERNAME AND API KEY>'
