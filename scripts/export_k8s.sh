#!/bin/sh
mkdir /workspace || true
mkdir /workspace/.kube
echo -n "${_KUBE_CONFIG}"  | base64 -d > /workspace/.kube/config
echo -n "${_CLIENT_TOKEN}" | base64 -d > /workspace/.kube/token
