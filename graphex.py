from flask import Flask, request
import graphene
import json


app = Flask(__name__)

class Query(graphene.ObjectType):
    hello = graphene.String(argument=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, argument):
        import pdb; pdb.set_trace()
        return f'Hello {argument}'

schema = graphene.Schema(query=Query)
# result = schema.execute('{ hello }')
# print(result.data['hello'])

@app.route("/graphql", methods=['POST'])
def graphql():
    data = json.loads(request.data)
    return json.dumps(schema.execute(data['query'][0]).data)