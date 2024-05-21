import {
    CreateButton,
    Datagrid,
    FilterButton,
    FilterForm,
    ListBase,
    List,
    Pagination,
    TextField,
    TextInput,
    SearchInput,
    EmailField,
    DateField,
    ShowButton,
    ReferenceField,
    ImageField,
    DeleteButton
} from 'react-admin';
import { Stack } from '@mui/material';

const CustomerFilters = [
    <SearchInput source="Name" resettable alwaysOn />,
    <TextInput label="email" source="Email" />
];
const ListToolbar = () => (
    <Stack direction="row" justifyContent="space-between">
        <FilterForm filters={CustomerFilters} />
        <div>
            <FilterButton filters={CustomerFilters} />
            <CreateButton />
        </div>
    </Stack>
)
export const PostsList = () => (
    <List>
        <ListToolbar />
        <Datagrid rowClick="edit">
            <TextField disabled source="id" />
            <ReferenceField source="user_id" reference='Users'/>
            <TextField source="title"/>
            <TextField source="Description"/>
            <ImageField source="image"/>
            <TextField source="tag" />
            <ReferenceField source="category_id" reference="Categories" />
            <TextField source="status" />
            <ShowButton label='show'/>
            <DeleteButton label='delete'/>
        </Datagrid>
    </List>
);