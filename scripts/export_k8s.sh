#!/bin/sh
set -x
mkdir /workspace || true
mkdir /workspace/.kube || true
echo -n "${_KUBE_CONFIG}"  | base64 -d > /workspace/.kube/config
echo -n "${_CLIENT_TOKEN}" | base64 -d > /workspace/.kube/token
chmod 644 /workspace/.kube/config

cat /workspace/.kube/config
helm upgrade parser parser --install --debug
