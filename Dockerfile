FROM node:lts-alpine3.19
WORKDIR /usr/app
RUN npm install @slidev/cli @slidev/theme-default