#!/bin/sh
ENV="${ENV:-Local}"
mkdir -p engine/output
ENV=$ENV python engine/src/container/manager.py run
