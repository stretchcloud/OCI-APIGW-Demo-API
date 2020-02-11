#!/bin/bash
oci api-gateway gateway create --display-name "ListInstanceAPIGW" --compartment-id <compartment-id> --endpoint-type "PUBLIC" --subnet-id <subnet-ocid> --wait-for-state ACTIVE
