#!/bin/sh
# echo "In the run script... Replacing Variables"
sed -i 's+"\__API_URL__\"+"'${API_URL}'"+g' /usr/share/nginx/html/config.js
exec "$@"
echo "Variables have been re-named/replaced, starting NGINX and serviing the app"
nginx -g 'daemon off;'