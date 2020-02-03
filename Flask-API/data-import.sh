#!/bin/sh

(echo .mode csv instances; echo .import instances.csv instances; echo .quit) | sqlite3 instances.db
