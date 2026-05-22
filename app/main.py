import os

from litestar import Litestar
from litestar.openapi.config import OpenAPIConfig
from litestar.openapi.plugins import ScalarRenderPlugin
import uvicorn

from versioning import VersioningController

routes = [VersioningController]

app = Litestar(route_handlers=routes,
               openapi_config=OpenAPIConfig(
                   title="Hivebox API",
                   description="API to learn about DevOps",
                   version=str(os.getenv("APP_VERSION")),
                   render_plugins=[ScalarRenderPlugin()]
               ))

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)