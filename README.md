# html2pdf-server

This is a server application that converts HTML to PDF using [weasyprint](https://weasyprint.org/).

## Usage

Simply run the created Docker container using

```bash
docker run -p 8082:8082 --rm -it improrama/html2pdf-server:latest
```

and send a POST request to `http://localhost:8082/render` (as defined in the OpenAPI 3 specification located in `openapi.yaml`) with the HTML content in the request body.

## Integration

If you want to integrate this server into your application, simply generate an OpenAPI client using the OpenAPI 3 specification located in `openapi.yaml`. Hence, you can use the server in different programming languages.

**This repository will not provide any clients for different programming languages.**
