import argparse
import logging
import sys
from google.cloud import secretmanager

from bot import RandoBot


def main():
    parser = argparse.ArgumentParser(
        description='RandoBot for Paper Mario 64 Randomizer',
    )
    parser.add_argument('--verbose', '-v', action='store_true', help='verbose output')
    args = parser.parse_args()

    logger = logging.getLogger()
    handler = logging.StreamHandler(sys.stdout)

    if args.verbose:
        logger.setLevel(logging.DEBUG)
        handler.setLevel(logging.DEBUG)

    handler.setFormatter(logging.Formatter(
        '[%(asctime)s] %(name)s (%(levelname)s) :: %(message)s'
    ))
    logger.addHandler(handler)

    # Get token with google secret manager
    secret_manager = secretmanager.SecretManagerServiceClient()
    client_id = secret_manager.access_secret_version(request={"name": "projects/4264716284/secrets/racetime-client-id/versions/1"}).payload.data.decode("UTF-8")
    client_secret = secret_manager.access_secret_version(request={"name": "projects/4264716284/secrets/racetime-client-secret/versions/1"}).payload.data.decode("UTF-8")
    api_key = secret_manager.access_secret_version(request={"name": "projects/4264716284/secrets/api-key/versions/1"}).payload.data.decode("UTF-8")

    inst = RandoBot(        
        api_key=api_key,
        category_slug="pm64r",
        client_id=client_id,
        client_secret=client_secret,
        logger=logger,
    )
    inst.run()


if __name__ == '__main__':
    main()