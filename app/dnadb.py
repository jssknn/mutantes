import redis

r = redis.StrictRedis(host='redis', port=6379, password='', decode_responses=True)

class DNAdb:

    def post_mutant_db(string, mutant):
        exist = r.get(string)
        if exist is None:
            r.set(string, mutant)
            r.incr("humans")
            if mutant: r.incr("mutants") 

    def get_stats_db():
        return int(r.get("humans") or 0), int(r.get("mutants") or 0)
