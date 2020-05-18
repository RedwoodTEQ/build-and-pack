::SET PACK_OUTPUT_DIR=E:\rp\local-nuget-packages
SET SOLUTION_DIR=E:\rp\outdoor-asset-tracking\app-front-end\dotnet-worker
SET PACK_OUTPUT_DIR=E:\rp\outdoor-asset-tracking\app-front-end\dotnet-worker\Publish

SET PROJECT_NAME=GeoSensePlus.Server
dotnet pack %SOLUTION_DIR%\%PROJECT_NAME%\%PROJECT_NAME%.csproj -c Release -o %PACK_OUTPUT_DIR%
::dotnet tool update -g %PROJECT_NAME% --add-source %PACK_OUTPUT_DIR%

SET PROJECT_NAME=GeoSensePlus.Cli
dotnet pack %SOLUTION_DIR%\%PROJECT_NAME%\%PROJECT_NAME%.csproj -c Release -o %PACK_OUTPUT_DIR%