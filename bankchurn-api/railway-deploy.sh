#!/bin/bash

# Railway deployment script
echo "Starting Railway deployment..."

# Set the correct Railway token (this should be the long token from your local config)
RAILWAY_TOKEN="rw_Fe26.2**77e0504ad5405dac2446647190e165dfdaa869abf671ab9e4d351f396b595455*4Tlwl1P2R-9wQXfi60s9GQ*vxVbZUY2_a0KRbytmvhTiPQj2LB151jzXFojJHSIqvveg42YGfuY0en2Czd5F6W3ZN0U1FqJSwUBJi6Gz4LUdA*1760582722711*54f58c8c20066e95d48d3671b1e2fbeb7fb9e318942da644e3ba5ce29f7b4e51*Lc8KGamRV-BbQJVWR4Y2SMrbi2kOeEcNznSF7SleTKE"

# Set project and service IDs
RAILWAY_PROJECT_ID="f1151051-b81b-49d7-a5ab-99f86317cad1"
RAILWAY_SERVICE_ID="102676bd-5a32-41a2-ba57-2efd6bc753db"

echo "Setting Railway environment variables..."
export RAILWAY_TOKEN=$RAILWAY_TOKEN
export RAILWAY_PROJECT_ID=$RAILWAY_PROJECT_ID

echo "Creating Railway config file..."
mkdir -p ~/.railway
echo "{\"token\":\"$RAILWAY_TOKEN\"}" > ~/.railway/token.json

echo "Testing Railway connection..."
railway status

echo "Deploying to Railway..."
railway up --service=$RAILWAY_SERVICE_ID --detach

echo "Deployment completed!"
