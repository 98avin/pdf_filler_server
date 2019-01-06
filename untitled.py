import http.client

conn = http.client.HTTPConnection("localhost")

payload = "{ \n\t\"First Name\": \"Navruz\" ,\n\t\"Last Name\": \"Baum\",\n\t\"Vote-by-Mail\":\"true\"\n}"

headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "14488ae1-92c2-4888-84a4-73495d791cfb"
    }

for _ in range(500):
	conn.request("POST", "generate", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))