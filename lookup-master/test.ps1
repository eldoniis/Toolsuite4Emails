# Define la URL de la API
$url = "http://127.0.0.1:5000/whois-dns"

# Crea el cuerpo de la solicitud en formato JSON
$body = @{
    domain = "google.com"
} | ConvertTo-Json -Depth 1

# Realiza la solicitud POST
$response = Invoke-WebRequest -Uri $url -Method POST -Body $body -ContentType "application/json"

# Muestra el contenido de la respuesta
$response.Content