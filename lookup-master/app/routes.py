from flask import render_template, request, jsonify
from .functionalities.whoisdns import perform_dns_query, perform_whois

def setup_routes(app):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/whois-dns", methods=["POST"])
    def whoisdns():
        query_results = {}
        user_request = request.get_json()
        query_results["dns"] = perform_dns_query(user_request["domain"])
        query_results["whois"] = perform_whois(user_request["domain"])
        return jsonify({"domain": user_request["domain"], "query_results": query_results})

