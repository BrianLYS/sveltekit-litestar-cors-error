#!/bin/bash

# sleep 5 seconds to wait for the database to start
sleep 3

# Run migrations
piccolo migrations forwards session_auth && piccolo migrations forwards user