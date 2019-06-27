from sanic_graphql import GraphQLView
from sanic import Sanic
from schema import schema

app = Sanic(__name__)
app.debug = True

app.add_route(GraphQLView.as_view(schema=schema, graphiql=True), '/graphql')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
