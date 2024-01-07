# ---------this dockerfile, compiles and runs everything, and does not need node_modules to be present
# with the code, but is not supporting hotloading
# # Fetching the latest node image on alpine linux
# FROM node:alpine AS development

# # Declaring env
# ENV NODE_ENV development

# # Creating the /app2 directory
# RUN mkdir /app2

# # Setting up the work directory
# # Dont use /app directory for react, something is wrong i dont know
# WORKDIR /app2

# # Installing dependencies
# # Dont use /app directory for react, something is wrong i dont know
# COPY ./package.json /app2
# RUN npm install

# # Copying all the files in our project
# COPY . .

# # Starting our application
# CMD npm start

# ---------this is supporting hotloading, but needs node_modules to be present
FROM node:alpine

WORKDIR /app
COPY package.json .
RUN npm install
COPY . .

CMD ["npm", "start"] 
# you can only have one CMD command