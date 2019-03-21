# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 07:44:23 2019

@author: nils.droste@cec.lu.se
"""

# https://developer.twitter.com/en/docs/tweets/search/api-reference/premium-search

import os
from searchtweets import ResultStream, gen_rule_payload, load_credentials, collect_results

path="C:\\Users\\Nils\\Box\\projects\\Glyphosate\\Scraping\\BECCglyph"
os.chdir(path)

premium_search_args = load_credentials(filename="./twitter_keys.yaml",
                                       yaml_key="search_tweets_fullarchive_sandbox",
                                       env_overwrite=False)

rule = gen_rule_payload("glyphosate", # -is:retweet
                        results_per_call=100,
                        from_date="2019-03-01", 
                        to_date="2019-03-21 09:00")

tweets = collect_results(rule,
                         max_results=10,
                         result_stream_args=premium_search_args) # change this if you need to

rs = ResultStream(rule_payload=rule,
                  max_results=500,
                  max_pages=5,
                  **premium_search_args)

tweets = list(rs.stream())