import { apiSlice } from "../services/apiSlice";

interface User {
  name: string;
  email: string;
}

const authApiSlice = apiSlice.injectEndpoints({
  endpoints: (builder) => ({
    retrieveUser: builder.query<User, void>({
      query: () => "/users/me/",
    }),
    login: builder.mutation({
      query: (form_data) => ({
        url: "/login",
        method: "POST",
        body: form_data,
      }),
    }),
    register: builder.mutation({
      query: ({ name, email, password }) => ({
        url: "/user/",
        method: "POST",
        body: { name, email, password },
      }),
    }),
    verify: builder.mutation({
      query: () => ({
        url: "/jwt/verify/",
        method: "POST",
      }),
    }),
    logout: builder.mutation({
      query: () => ({
        url: "/logout/",
        method: "POST",
      }),
    }),
  }),
});

export const {
  useRetrieveUserQuery,
  useLoginMutation,
  useRegisterMutation,
  useVerifyMutation,
  useLogoutMutation,
} = authApiSlice;
