import * as React from 'react';
import { Create, SimpleForm, TextInput, DateInput, required,ReferenceInput,ImageField } from 'react-admin';

export const commentCreate = () => (
    <Create>
        <SimpleForm>
            <ReferenceInput source="user_id" reference='Users'/>
            <ReferenceInput source="post_id" reference='Posts'/>
            <TextInput source="Description" label="Description" validate={[required()]}/>
        </SimpleForm>
    </Create>
);