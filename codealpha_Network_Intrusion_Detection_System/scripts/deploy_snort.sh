#!/bin/bash
# Script to start Snort in NIDS mode on the VMware interface

INTERFACE="eth0" # Change this to match your VMnet8 interface
RULE_PATH="./local.rules"

echo "Starting Snort NIDS on interface $INTERFACE..."
sudo snort -A console -q -u snort -g snort -c $RULE_PATH -i $INTERFACE