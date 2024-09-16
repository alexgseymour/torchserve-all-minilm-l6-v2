#!/bin/bash

# --ncs means the snapshot feature is disabled.

echo "server is starting..."
torchserve --foreground --model-store model_store --models embedder=$ENCODER_MODEL_NAME.mar,cross_encoder=$CROSSENCODER_MODEL_NAME.mar --ncs