const { makeExecutableSchema } = require('@graphql-tools/schema');
const fs = require('fs');
const path = require('path');

let users = [
  { id: '1', name: 'Alice' },
  { id: '2', name: 'Bob' },
];

let posts = [
  { id: '1', userId: '1', content: "This is Alice's first post" },
  { id: '2', userId: '2', content: 'Bob is here!' },
];

// Load schema from the SDL file
const typeDefs = fs.readFileSync(path.join(__dirname, 'schema.graphql'), 'utf8');

const resolvers = {
  Query: {
    users: () => users,
    posts: () => posts,
    user: (_, { id }) => {
      const user = users.find(user => user.id === id);
      if (!user) throw new Error(`User with ID ${id} not found`);
      return user;
    },
    post: (_, { id }) => {
      const post = posts.find(post => post.id === id);
      if (!post) throw new Error(`Post with ID ${id} not found`);
      return post;
    },
  },
  Mutation: {
    addUser: (_, { name }) => {
      if (!name) throw new Error('Name is required to add a user');
      const newUser = { id: String(users.length + 1), name };
      users.push(newUser);
      return newUser;
    },
    updateUser: (_, { id, name }) => {
      if (!name) throw new Error('Name is required to update user');
      const user = users.find(user => user.id === id);
      if (!user) throw new Error(`User with ID ${id} not found`);
      user.name = name;
      return user;
    },
    addPost: (_, { userId, content }) => {
      if (!content) throw new Error('Content is required for the post');
      const user = users.find(user => user.id === userId);
      if (!user) throw new Error(`User with ID ${userId} not found`);
      const newPost = { id: String(posts.length + 1), userId, content };
      posts.push(newPost);
      return newPost;
    },
  },
};

module.exports = makeExecutableSchema({ typeDefs, resolvers });
