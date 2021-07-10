from flask import Flask, jsonify, request
from dnadb import DNAdb
from dna_mutant import DNACheck, DNAException

server = Flask(__name__)

@server.route('/mutant', methods=['POST'])
def mutant():
    dna = request.json
    try:
        DNACheck.isValid(dna)
        mutant = DNACheck.isMutant(dna)
        DNAdb.post_mutant_db(str(dna["dna"]),1 if mutant else 0)
        return jsonify({"mutant" : mutant}), (200 if mutant else 403)
    except DNAException as dna_ex:
        return jsonify({"error" : str(dna_ex)}), 400
    except Exception as ex:
        return jsonify({"error" : "Error interno en el servidor"}), 500


@server.route('/stats', methods=['GET'])
def stats():
    try:
        humans, mutants = DNAdb.get_stats_db()
        ratio = mutants / humans if humans != 0 else 0
        return jsonify({"count_human_dna": humans, "count_mutant_dna" : mutants, "ratio": ratio}), 200
    except Exception as ex:
        return jsonify({"error" : "Error interno en el servidor"}), 500
