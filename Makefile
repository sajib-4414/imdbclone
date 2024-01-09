# Makefile
# .PHONY: up This PHONY ensures that even if there is a file named up in your directory,
# running make up will execute the specified command (docker compose up) instead of trying 
# to treat up as a file target.
.PHONY: up
up:
	docker compose up
down:
	docker compose down
restart-movie:
	docker compose restart movie-service
configure_vm_path:
    # Change server_name in nginx-config.conf
	sed -i 's/server_name .*/server_name shamsul-dev1.rits.uregina.ca;/' nginx-config.conf

    # Change REACT_API_HOST in react_client/.env
	sed -i 's/REACT_API_HOST=.*/REACT_API_HOST=http:\/\/shamsul-dev1.rits.uregina.ca:8005/' react_client/.env

    # Change publicPath in react_client/webpack.config.js
	sed -i "s#publicPath: '.*'#publicPath: 'http://shamsul-dev1.rits.uregina.ca:8005/'#" react_client/webpack.config.js
    # Change REACT_API_HOST in react_staff/.env
	sed -i 's/REACT_API_HOST=.*/REACT_API_HOST=http:\/\/shamsul-dev1.rits.uregina.ca:8005/' react_staff/.env

    # Change publicPath in react_staff/webpack.config.js
	sed -i "s#publicPath: '.*'#publicPath: 'http://shamsul-dev1.rits.uregina.ca:8005/'#" react_staff/webpack.config.js
configure_localhost_path:
    # Change server_name in nginx-config.conf
	sed -i 's/server_name .*/server_name localhost;/' nginx-config.conf

    # Change REACT_API_HOST in react_client/.env
	sed -i 's/REACT_API_HOST=.*/REACT_API_HOST=http:\/\/localhost:8005/' react_client/.env

    # Change publicPath in react_client/webpack.config.js
	sed -i "s#publicPath: '.*'#publicPath: 'http://localhost:8005/'#" react_client/webpack.config.js
     # Change REACT_API_HOST in react_staff/.env
	sed -i 's/REACT_API_HOST=.*/REACT_API_HOST=http:\/\/localhost:8005/' react_staff/.env

    # Change publicPath in react_staff/webpack.config.js
	sed -i "s#publicPath: '.*'#publicPath: 'http://localhost:8005/'#" react_staff/webpack.config.js
