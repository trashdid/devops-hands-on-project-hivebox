from litestar import Controller, get

from versioning.service import get_current_version


class VersioningController(Controller):
    path = '/version'
    tags = ['Version']

    @get('/')
    async def get_current_version(self) -> str:
        return get_current_version()