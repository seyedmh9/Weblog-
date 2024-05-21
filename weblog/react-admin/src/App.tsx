import {
  Admin,
  Resource,
  ListGuesser,
  EditGuesser,
  ShowGuesser,
} from "react-admin";
import { dataProvider } from "./dataProvider";
import { authProvider } from "./authProvider";
import { usersList } from "./resource db/Users";
import { usersCreate } from "./resource db/Users_create";
import { commentCreate } from "./resource db/Comments_create";
import { commentList } from "./resource db/Comments";
import { commentEdit } from "./resource db/Comment_edit";
import { PostsList } from "./resource db/Posts";
import { PostsCreate } from "./resource db/Posts_create";
import { PostsEdit } from "./resource db/Posts_edit";
import { categoryList } from "./resource db/Categories";
import { categoryCreate } from "./resource db/Categories_create";


export const App = () => (
  <Admin dataProvider={dataProvider} authProvider={authProvider}>
    <Resource
      name="Users"
      list={usersList}
      edit={EditGuesser}
      show={ShowGuesser}
      create={usersCreate}
    />
    <Resource
      name="Posts"
      list={PostsList}
      edit={PostsEdit}
      show={ShowGuesser}
      create={PostsCreate}
    />
    <Resource
      name="Categories"
      list={categoryList}
      edit={EditGuesser}
      show={ShowGuesser}
      create={categoryCreate}
    />
    <Resource
      name="comments"
      list={commentList}
      edit={commentEdit}
      show={ShowGuesser}
      create={commentCreate}
    />
  </Admin>
);
