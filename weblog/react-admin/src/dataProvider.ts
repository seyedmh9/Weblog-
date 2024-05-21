import simpleRestProvider from "ra-data-simple-rest";
import axios from 'axios';
import { stringify } from 'query-string';
import { DataProvider } from 'react-admin';
export const dataProvider = simpleRestProvider(
  import.meta.env.VITE_SIMPLE_REST_URL
);

const apiUrl = 'http://localhost:8000';

const httpClient = axios.create({
  baseURL: apiUrl,
});

update: (resource, params) => {
  if (resource === 'Users' && params.data.profile_picture) {
    const formData = new FormData();
    Object.keys(params.data).forEach(key => {
      if (key === 'profile_picture' && params.data[key].rawFile) {
        formData.append(key, params.data[key].rawFile);
      } else {
        formData.append(key, params.data[key]);
      }
    });
    return httpClient.put(`/${resource}/${params.id}`, formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    }).then(response => ({ data: response.data }));
  } else if (resource === 'profile_picture' && params.data.image) { // اضافه کردن برای ادیت عکس پست
    const formData = new FormData();
    Object.keys(params.data).forEach(key => {
      if (key === 'profile_picture' && params.data[key].rawFile) {
        formData.append(key, params.data[key].rawFile);
      } else {
        formData.append(key, params.data[key]);
      }
    });
    return httpClient.put(`/${resource}/${params.id}`, formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    }).then(response => ({ data: response.data }));
  } else {
    return httpClient.put(`/${resource}/${params.id}`, params.data).then(response => ({ data: response.data }));
  }
}

create: (resource, params) => {
  if ((resource === 'Users' && params.data.profile_picture) || (resource === 'Posts' && params.data.image)) {
      const formData = new FormData();
      Object.keys(params.data).forEach(key => {
          if ((key === 'profile_picture' || key === 'image') && params.data[key].rawFile) {
              formData.append(key, params.data[key].rawFile);
          } else {
              formData.append(key, params.data[key]);
          }
      });
      return httpClient.post(`/${resource}`, formData, {
          headers: { 'Content-Type': 'multipart/form-data' },
      }).then(response => ({ data: response.data }));
  } else {
      return httpClient.post(`/${resource}`, params.data).then(response => ({ data: response.data }));
  }
}
