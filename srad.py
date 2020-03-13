import consul  # https://python-consul.readthedocs.io/en/v0.4.4/

consul = consul.Consul(host="3.17.67.170", port=8500)

agent = consul.agent

service = agent.service

# first fast api app
service.register("fourth", service_id="fourth",
                 address='127.0.0.1', port=8080)




# second fast api app
service.register("fifth", service_id="fifth",
                 address='127.0.0.1', port=8081)


service_list = agent.services()

#print(service_list)

third_service = service_list['fourth']


print(third_service['Address'], ":", third_service['Port'])

user = reqeusts.get('adr : port ? userId=10')

print(user)

# service.deregister(service_id='first')


# info = service.info(name='second')

# print(info)
