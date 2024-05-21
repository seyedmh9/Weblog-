
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
    DeleteButton,
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
export const categoryList = () => (
    <List>
        <ListToolbar />
        <Datagrid rowClick="edit">
            <TextField disabled source="id" />
            <TextField source="name"/>
            <TextField source="Description"/>
            <EmailField source="created_at"/>
            <ShowButton label='show'/>
            <DeleteButton label='delete'/>
        </Datagrid>
    </List>
);