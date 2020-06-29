:: for a clean build, it is recommended to use --pull flag as well

SET GSV_VERSION=v1.2.0.4-working3
SET GSTTN_VERSION=v1.1.0-working3

SET DOTNET_WORKER_PATH=E:\rp\outdoor-asset-tracking\app-front-end\dotnet-worker
SET NODE_WORKER_PATH=E:\rp\outdoor-asset-tracking\app-front-end\node-worker

::docker build --no-cache -t redwoodteq/geosenseplusserver:latest -t redwoodteq/geosenseplusserver:%GSV_VERSION% -f ../dotnet-worker/GeoSensePlus.Server/Dockerfile ../dotnet-worker
docker build --no-cache -t redwoodteq/geosenseplusserver:latest -t redwoodteq/geosenseplusserver:%GSV_VERSION% -f %DOTNET_WORKER_PATH%\GeoSensePlus.Server\Dockerfile %DOTNET_WORKER_PATH%

::docker build --no-cache -t redwoodteq/gsttn:latest -t redwoodteq/gsttn:%GSTTN_VERSION% -f ../node-worker/Dockerfile ../node-worker
docker build --no-cache -t redwoodteq/gsttn:latest -t redwoodteq/gsttn:%GSTTN_VERSION% -f %NODE_WORKER_PATH%\Dockerfile %NODE_WORKER_PATH%