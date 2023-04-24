## **NGINX-FLASK-DOCKER**

>NOTE: Nginx loadbalancer

Configure a nginx server as **loadbalancer** using a two _flask app_ running in the _**same** port_ or running each one from _**different** ports_.

**Different ports**

- In **differents_ports** folder run:

  ``` cd differents_ports```    
    ``` docker-compose up -d ```

- Test: ```curl localhost:8080```

**Same port**

- In **same_port** folder run:

    ``` cd same_port```    
    ``` docker-compose up -d ```
- Test: ```curl localhost:8080```
