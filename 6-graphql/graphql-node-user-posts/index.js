const express = require('express');
const { graphqlHTTP } = require('express-graphql');
const { GraphQLObjectType, GraphQLSchema, GraphQLString, GraphQLID, GraphQLList } = require('graphql');

// Hardcoded data for users and posts
let users = [
  { id: '1', name: 'Alice' },
  { id: '2', name: 'Bob' },
];

let posts = [
  { id: '1', userId: '1', content: 'This is Alice\'s first post' },
  { id: '2', userId: '2', content: 'Bob is here!' },
];

// UserType: Defines the shape of the user data
const UserType = new GraphQLObjectType({
  name: 'User',
  fields: {
    id: { type: GraphQLID },
    name: { type: GraphQLString },
  },
});

// PostType: Defines the shape of the post data
const PostType = new GraphQLObjectType({
  name: 'Post',
  fields: {
    id: { type: GraphQLID },
    userId: { type: GraphQLID },
    content: { type: GraphQLString },
  },
});

// RootQuery: Defines how you can fetch data (Users and Posts)
const RootQuery = new GraphQLObjectType({
  name: 'RootQueryType',
  fields: {
    users: {
      type: new GraphQLList(UserType),
      resolve() {
        return users;
      },
    },
    posts: {
      type: new GraphQLList(PostType),
      resolve() {
        return posts;
      },
    },
    user: {
      type: UserType,
      args: { id: { type: GraphQLID } },
      resolve(parent, args) {
        const user = users.find(user => user.id === args.id);
        if (!user) {
          throw new Error(`User with ID ${args.id} not found`);
        }
        return user;
      },
    },
    post: {
      type: PostType,
      args: { id: { type: GraphQLID } },
      resolve(parent, args) {
        const post = posts.find(post => post.id === args.id);
        if (!post) {
          throw new Error(`Post with ID ${args.id} not found`);
        }
        return post;
      },
    },
  },
});

// Mutation: Defines how you can modify data (Adding/Updating Users and Posts)
const Mutation = new GraphQLObjectType({
  name: 'Mutation',
  fields: {
    addUser: {
      type: UserType,
      args: {
        name: { type: GraphQLString },
      },
      resolve(parent, args) {
        if (!args.name) {
          throw new Error('Name is required to add a user');
        }

        const newUser = { id: String(users.length + 1), name: args.name };
        users.push(newUser);
        return newUser;
      },
    },
    updateUser: {
      type: UserType,
      args: {
        id: { type: GraphQLID },
        name: { type: GraphQLString },
      },
      resolve(parent, args) {
        if (!args.name) {
          throw new Error('Name is required to update user');
        }

        const user = users.find(user => user.id === args.id);
        if (!user) {
          throw new Error(`User with ID ${args.id} not found`);
        }

        user.name = args.name;
        return user;
      },
    },
    addPost: {
      type: PostType,
      args: {
        userId: { type: GraphQLID },
        content: { type: GraphQLString },
      },
      resolve(parent, args) {
        if (!args.content) {
          throw new Error('Content is required for the post');
        }

        const user = users.find(user => user.id === args.userId);
        if (!user) {
          throw new Error(`User with ID ${args.userId} not found`);
        }

        const newPost = { id: String(posts.length + 1), userId: args.userId, content: args.content };
        posts.push(newPost);
        return newPost;
      },
    },
  },
});

// Schema: Defines how to interact with the API (Query and Mutation)
const schema = new GraphQLSchema({
  query: RootQuery,
  mutation: Mutation,
});

// Initialize the Express app
const app = express();

// Set up the /graphql endpoint for GraphQL queries and mutations
app.use(
  '/graphql',
  graphqlHTTP({
    schema: schema,
    graphiql: true, // Enable the GraphiQL UI for testing
    customFormatErrorFn(err) {
      // Format error message for better understanding
      return {
        message: err.message,
        locations: err.locations,
        stack: err.stack ? err.stack.split('\n') : [],
        path: err.path,
      };
    },
  })
);

// Start the server
const PORT = process.env.PORT || 4000;
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}/graphql`);
});
