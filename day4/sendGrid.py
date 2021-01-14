# Simple Hello World program using the sendgris API
# Sends an email with "Hello, World!"

import http.client

conn = http.client.HTTPSConnection("api.sendgrid.com")

# template_id removed for security
# emails removed for privacy
payload = "{\"personalizations\":[{\"to\":[{\"email\":\"alex.doe@example.com\",\"name\":\"Alex Doe\"}],\"dynamic_template_data\":{\"verb\":\"\",\"adjective\":\"\",\"noun\":\"\",\"currentDayofWeek\":\"\"},\"subject\":\"Hello, World!\"}],\"from\":{\"email\":\"noreply@smth.com\",\"name\":\"Some One\"},\"reply_to\":{\"email\":\"noreply@smth.com\",\"name\":\"Someone\"},\"template_id\":\"<<template_id>>\"}"

headers = {
    # Key removed for security
    'authorization': "Bearer <<api_key>>",
    'content-type': "application/json"
    }

conn.request("POST", "/v3/mail/send", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
