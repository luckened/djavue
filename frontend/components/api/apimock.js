var logged_user = null;

function mockasync(data) {
  return new Promise((resolve, reject) => {
    setTimeout(() => resolve({ data: data }), 600);
  });
}

const api = {
  login(username, password) {
    if (password) {
      logged_user = {
        username: username,
        first_name: "Mark",
        last_name: "Zuckerberg",
        email: "zuck@facebook.com",
        notifications_enabled: true,
        permissions: {
          ADMIN: username == "admin",
          STAFF: username == "admin"
        }
      };
    }
    return mockasync(logged_user);
  },
  logout() {
    logged_user = null;
    return mockasync({});
  },
  whoami() {
    return mockasync(
      logged_user
        ? {
            authenticated: true,
            user: logged_user
          }
        : { authenticated: false }
    );
  },
  add_todo(newtask) {
    return mockasync({ description: newtask, done: false });
  },
  list_todos() {
    return mockasync({
      todos: [
        { description: "Do the laundry", done: true },
        { description: "Walk the dog", done: false }
      ]
    });
  },
  list_tweets(username) {
    return mockasync({
      tweets: [
        {
          author_name: "Isaac Newton",
          author_username: username || "isaacnewton",
          author_avatar: "http://placekitten.com/200/300",
          created_at: "2021-09-14T20:19:07.551Z",
          content: "Ser ou nao ser eis a questao"
        },
        {
          author_name: "Victor Antonio",
          author_username: username || "vict12",
          author_avatar: "http://placekitten.com/300/300",
          created_at: "2021-07-14T20:18:07.551Z",
          content: "Bom dia"
        },
        {
          author_name: "asdasd",
          author_username: username || "asasdasd",
          author_avatar: "http://placekitten.com/122/122",
          created_at: "2020-09-14T20:18:07.551Z",
          content: "Escrevi sai correndo"
        }
      ]
    });
  }
};

export default api;
