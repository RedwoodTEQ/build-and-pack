SET SOLUTION_DIR=E:\rp\outdoor-asset-tracking\github\GeoSensePluse-Server

:: build docker image
:: ==================

SET GSV_VERSION=%1
docker build --no-cache -t redwoodteq/geosenseplusserver:latest -t redwoodteq/geosenseplusserver:%GSV_VERSION% -f %SOLUTION_DIR%\GeoSensePlus.Server\Dockerfile %SOLUTION_DIR%

:: pack to nuget package
:: =====================

SET PROJECT_NAME=GeoSensePlus.Server
SET PACK_OUTPUT_DIR=E:\rp\local-nuget-packages

dotnet pack %SOLUTION_DIR%\%PROJECT_NAME%\%PROJECT_NAME%.csproj -c Release -o %PACK_OUTPUT_DIR%
dotnet tool update -g %PROJECT_NAME% --add-source %PACK_OUTPUT_DIR%