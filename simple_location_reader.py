#!/usr/bin/env python3

import argparse
import logging

from common_constants import LOGGING_ARGS
from location_client import LocationClient

if __name__ == "__main__":
    # Setup CLI
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--grpc", required=True, help="gRPC location server hostname")
    args = vars(parser.parse_args())

    # Setup logging
    logging.basicConfig(**LOGGING_ARGS)

    locations = LocationClient(args["grpc"]).start()

    try:
        while True:
            print("Got location: {0}".format(locations.get_xy()))
    except KeyboardInterrupt:
        pass
    finally:
        locations.stop()

    print("Exiting...")
