#!/bin/bash
git add *.py
git add *.md
git commit -m "$(date "+%Y-%m-%d %H:%M")"
git push
