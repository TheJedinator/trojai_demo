FROM node:latest as build
WORKDIR /app
RUN rm -rf /app/node_modules
COPY package.json package.json
COPY package-lock.json package-lock.json
RUN npm install --no-cache-dir
COPY . /app
RUN npm run build

FROM nginx:alpine
# copy the build folder from react to the root of nginx (www)
COPY --from=build /app/dist /usr/share/nginx/html
# --------- only for those using react router ----------
# if you are using react router 
# you need to overwrite the default nginx configurations
# remove default nginx configuration file
RUN rm /etc/nginx/conf.d/default.conf
# replace with custom one
COPY nginx.conf /etc/nginx/conf.d
COPY ./run.sh /

EXPOSE 80
# start nginx 
RUN chmod +x run.sh
WORKDIR /
CMD ["/run.sh"]