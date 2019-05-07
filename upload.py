# -*- coding: utf-8 -*-

import sys
import requests
import os


token = os.getenv("YUQUE_TOKEN")
s = requests.Session()
s.headers = {"X-Auth-Token": token, "User-Agent": "python-uploader"}

DETAIL_URL = "https://{domain}/api/v2/repos/{namespace}/docs/{slug}"


def get_url_body():
    filename = sys.argv[1]
    with open(filename, "r") as f:
        lines = f.readlines()

    url, body = lines[0], lines[1:]
    return url, body


def upload_to_yuque(domain, namespace, doc_id, lines, slug, is_public):
    update_url = DETAIL_URL.format(domain=domain, namespace=namespace, slug=doc_id)
    title = [line for line in lines if line.strip()][0]
    body = "".join(lines)
    resp = s.put(
        update_url,
        data={
            "title": title.strip("#"),
            "slug": slug,
            "public": is_public,
            "body": body,
        },
    )
    return resp


def parse_url(url):
    parts = url.split("/")
    domain, namespace, slug = parts[-4], "{}/{}".format(parts[-3], parts[-2]), parts[-1]
    return domain, namespace, slug


def main():
    url, body = get_url_body()
    domain, namespace, slug = parse_url(url[:-1])
    doc_url = DETAIL_URL.format(domain=domain, namespace=namespace, slug=slug)
    resp = s.get(doc_url)
    data = resp.json()["data"]
    doc_id = data["id"]
    is_public = data["public"]

    result = upload_to_yuque(domain, namespace, doc_id, body, slug, is_public)
    if result.status_code == 200:
        print("Success updated!")
        print("URL: {}".format(url))
    else:
        print("Error!")
        print(result.text)
