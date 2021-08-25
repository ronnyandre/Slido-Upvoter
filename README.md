# Slido Upvoter

A simple Python script for automatically upvoting your Slido question.

## Why?

Why not?

## How it works

The script uses Selenium (which is required for it to run) and loops numerous times (that you set) and upvoting your question.

## Using the script

Edit `main.py` and set the following parameters:

`slido_id` This is **not** the Slido event code, but the unique ID from the URL *after* you enter the code on Slido.

`slido_qid` You need to find the unique ID for the question you have asked (use the browser inspector to find this). Each question `div` should have an attribute called `data-qid` that contains this ID.