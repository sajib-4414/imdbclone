FROM node:alpine

WORKDIR /app

COPY package*.json ./
RUN npm install -g nodemon
RUN npm install

COPY . .
EXPOSE 3002
CMD ["npm", "start"]
