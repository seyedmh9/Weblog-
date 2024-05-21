import * as React from 'react';
import { Create, SimpleForm, TextInput, DateInput, required, ImageField , ImageInput } from 'react-admin';

export const usersCreate = () => (
    <Create>
        <SimpleForm>
            <TextInput source="username" validate={[required()]} />
            <TextInput source="password" label="Password" validate={[required()]}/>
            <TextInput source="email" multiline={true} label="Email" validate={[required()]}/>
            <ImageInput source="profile_picture" label="profile_picture" accept="image/*">
                <ImageField source="src" title="title" />
            </ImageInput>
        </SimpleForm>
    </Create>
);