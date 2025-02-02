const express = require('express');
const { graphqlHTTP } = require('express-graphql');
const { GraphQLObjectType, GraphQLSchema, GraphQLString } = require('graphql');


//Let's break this down:
//    - RootQuery: This is like saying, "The first set of questions you can ask the server are called RootQuery."
//    - hello: This is one of the things you can ask for. In this case, you're asking for a greeting.
//    - args: You can ask the hello field to include a specific name (or not), and it will greet you by that name.
//    - resolve: This is how the server will respond to the question. If you ask for hello, it will give you a greeting like "Hello, Alice!" or "Hello, stranger!" if no name is provided.

const RootQuery = new GraphQLObjectType({
  name: 'RootQueryType',
  fields: {
    hello: {
      type: GraphQLString,
      args: { name: { type: GraphQLString } },
      resolve(parent, args) {
        return `Hello, ${args.name || 'stranger'}!`;
      },
    },
  },
});

// Mutation: Defines how you can modify data
const Mutation = new GraphQLObjectType({
  name: 'Mutation',
  fields: {
    setName: {
      type: GraphQLString, // The return type of the mutation
      args: {
        name: { type: GraphQLString }, // The argument for the mutation
      },
      resolve(parent, args) {
        // This mutation simply returns the name passed to it
        return `Hello, ${args.name}! You have set the name.`;
      },
    },
  },
});

// Here, we're saying that the GraphQL schema has a query section,
// and the only thing you can query (ask for) right now is the hello field from the RootQuery.
// This schema defines the "shape" of what data is available and how to ask for it.
const schema = new GraphQLSchema({
  query: RootQuery,
  mutation: Mutation
});

// Initialize the Express app
const app = express();

// Set up the /graphql endpoint for GraphQL queries
app.use(
  '/graphql',
  graphqlHTTP({
    schema: schema,
    graphiql: true, // Enable GraphiQL UI for testing
  })
);

// Start the server
const PORT = process.env.PORT || 4000;
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}/graphql`);
});
