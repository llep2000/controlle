#........................................................................
#..                    Academia Cisco Fermin Toro                      ..
#..                       Derechos reservados                          ..
#..                        Developer Llep A.                           ..
#..                            Ver. 0.0.1                              ..
#..                                                                    ..
#........................................................................

import json
import requests
api_url = "http://localhost:58000/api/v1/ticket"

headers = {
    "content-type": "application/json"
}

body_json = {
    "username": "llep",
    "password": "llep"  
}

resp = requests.post(api_url, json.dumps(body_json), headers=headers, verify=False)

print("Estatus de conexion: ", resp.status_code)
response_json = resp.json()

serviceTicket = response_json["response"]["serviceTicket"]
print("Numero de session de conexion: ", serviceTicket) 


"###########################################################################################"


api_url = "http://localhost:58000/api/v1/network-device"

headers={"X-Auth-Token": serviceTicket}

resp = requests.get(api_url, headers=headers, verify=False)

if (resp.ok):

    print("Estado de la repuesta :", resp.status_code)

    response_json = resp.json()
    networkDevices = response_json["response"]

    for networkDevice in networkDevices:
        print("############################################")
        print("Dispositivo :", networkDevice["hostname"])
        print("Plataforma :",networkDevice["platformId"])
        print("Version IOS :",networkDevice["softwareVersion"])
        print("Direccion :",networkDevice["managementIpAddress"])
        print("Nombres de equipos conectados :",networkDevice["connectedNetworkDeviceName"])
        print("Ips de equipos conectados :",networkDevice["connectedNetworkDeviceIpAddress"])
        
    

"###########################################################################################"


api_url = "http://localhost:58000/api/v1/host"

if (resp.ok):
    resp = requests.get(api_url, headers=headers, verify=False)


    print("Estado de la repuesta :", resp.status_code)

    response_json = resp.json()
    hosts = response_json["response"]

    for host in hosts:
        print("############################################")
        print("Nombre :",host["hostName"])
        print("IP :",host["hostIp"])
        print("Tipo de dispositivo :",host["hostType"])
        print("Direccion mac :",host["hostMac"])
        print("Interface conectada :", host["connectedInterfaceName"])
        print("Dispositivo al que se conecta :", host["connectedNetworkDeviceName"])
        print("Saludo ICMP :",host["pingStatus"])

"###########################################################################################"


api_url = "http://localhost:58000/api/v1/physical-topology"

if (resp.ok):
    resp = requests.get(api_url, headers=headers, verify=False)

    response_json = resp.json()
    print(response_json)
