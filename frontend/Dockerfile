FROM node:14.18-alpine3.15
WORKDIR /app
COPY yarn.lock /app/yarn.lock
COPY package.json /app/package.json
COPY src /app/src
COPY public /app/public
RUN yarn install
CMD ['yarn', 'start']
