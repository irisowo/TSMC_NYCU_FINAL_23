FROM node:14.18-alpine3.15 as builder
WORKDIR /app
COPY yarn.lock /app/yarn.lock
COPY package.json /app/package.json
COPY src /app/src
COPY public /app/public
RUN yarn install
CMD ['yarn', 'start']
RUN yarn build

FROM nginx
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/build /usr/share/nginx/html