import * as React from 'react';
import { Create, SimpleForm, TextInput, DateInput, ImageInput ,required,ReferenceInput,ImageField } from 'react-admin';

export const PostsCreate = () => (
    <Create>
        <SimpleForm>
            <ReferenceInput source="user_id" reference='Users'/>
            <TextInput source="title" label="title" validate={[required()]}/>
            <TextInput source="Description" multiline={true} label="Description" validate={[required()]}/>
            <ImageField source="image" title="image" />
            <ImageInput source="image" label="image" accept="image/*">
                <ImageField source="src" title="title" />
            </ImageInput>
            <TextInput source="tag" />
            <ReferenceInput source="category_id" reference='Categories'/>
            <TextInput source="status" multiline={true}/>
        </SimpleForm>
    </Create>
);