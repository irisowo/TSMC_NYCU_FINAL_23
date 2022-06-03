FROM node:14.18-alpine3.15
COPY yarn.lock /app/yarn.lock
COPY package.json /app/package.json
COPY src /app/src
COPY public /app/public
WORKDIR /app
RUN yarn install
CMD ["yarn", "start"]