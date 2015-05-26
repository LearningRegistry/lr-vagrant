#!/bin/bash

PUBLISH_BIN=./bin/publish.py
NODE_NAME=lr51a
NUM_ENV=1

#publish a normal envelope
${PUBLISH_BIN} --mode publish \
   --node ${NODE_NAME} --sign local --num ${NUM_ENV} \
   --outidfile "tmp/0_idfile.json" \
   --msg "This is a normal original"


# publish a replacement
${PUBLISH_BIN} --mode replace \
   --node ${NODE_NAME} --sign local --num ${NUM_ENV} \
   --idfile "tmp/0_idfile.json" \
   --outidfile "tmp/01_idfile.json" \
   --msg "This is a normal replacment"


#publish a normal envelope
${PUBLISH_BIN} --mode publish \
   --node ${NODE_NAME} --sign local --num ${NUM_ENV} \
   --outidfile "tmp/1_idfile.json" \
   --msg "This is a whitelist original"


# publish a replacement
${PUBLISH_BIN} --mode replace \
   --node ${NODE_NAME} --sign whitelist --num ${NUM_ENV} \
   --idfile "tmp/1_idfile.json" \
   --outidfile "tmp/11_idfile.json" \
   --msg "This is a replacment by whitelist"



#publish a proxy envelope
${PUBLISH_BIN} --mode publish \
   --node ${NODE_NAME} --sign proxy --num ${NUM_ENV} \
   --outidfile "tmp/2_idfile.json" \
   --msg "This is the proxy original"


# publish a replacement
${PUBLISH_BIN} --mode replace \
   --node ${NODE_NAME} --sign whitelist --num ${NUM_ENV} \
   --idfile "tmp/2_idfile.json" \
   --outidfile "tmp/21_idfile.json" \
   --msg "This is a replacment for proxy by whitelist"



#publish a local signed envelope
${PUBLISH_BIN} --mode publish \
   --node ${NODE_NAME} --sign local --num ${NUM_ENV} \
   --outidfile "tmp/3_idfile.json" \
   --msg "This is a rogue original"


# publish a replacement using untrusted key
${PUBLISH_BIN} --mode replace \
   --node ${NODE_NAME} --sign rogue --num ${NUM_ENV} \
   --idfile "tmp/3_idfile.json" \
   --outidfile "tmp/31_idfile.json" \
   --msg "This is a replacment by rouge"

