from flask import Flask, request, send_file, abort
from weasyprint import HTML
import io
import argparse

app = Flask(__name__)

@app.route('/render', methods=['POST'])
def render_pdf():
    try:
        html_content = request.data.decode('utf-8')
        file_name = request.args.get('filename', 'output.pdf')

        pdf_file = io.BytesIO()
        HTML(string=html_content).write_pdf(pdf_file)
        pdf_file.seek(0)
        return send_file(pdf_file, mimetype='application/pdf', as_attachment=True, download_name=file_name)
    except Exception as e:
        abort(400, description=f'Error generating PDF: {str(e)}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the HTML to PDF Flask server.')
    parser.add_argument('--host', type=str, default='0.0.0.0', help='Host to run the server on')
    parser.add_argument('--port', type=int, default=8082, help='Port to run the server on')
    parser.add_argument('--debug', action='store_true', help='Run the server in debug mode')
    args = parser.parse_args()
    
    app.run(host=args.host, port=args.port, debug=args.debug)
