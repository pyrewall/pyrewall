import { makeApi, Zodios } from "@zodios/core";
import { z } from "zod";

import { useUserContext } from "./contexts/UserContext";

export type AuthenticatedUser = {
  token: Token;
  user: User;
};
export type Token = {
  access_token: string;
  expires_at: string;
  expires_in: number;
};
export type User = {
  created_by_id: string;
  created_by_user: (User | null) | Array<User | null>;
  created_date: string;
  email: (string | null) | Array<string | null>;
  enabled: boolean;
  expires: (string | null) | Array<string | null>;
  full_name: (string | null) | Array<string | null>;
  id: string;
  modified_by_id: string;
  modified_by_user: (User | null) | Array<User | null>;
  modified_date: string;
  unix_id: number;
  username: string;
};
export type UserList = Array<User>;

const LoginRequest = z
  .object({ password: z.string(), username: z.string() })
  .passthrough();
const Token: z.ZodType<Token> = z
  .object({
    access_token: z.string(),
    expires_at: z.string().datetime({ offset: true }),
    expires_in: z.number().int(),
  })
  .passthrough();
const User: z.ZodType<User> = z.lazy(() =>
  z
    .object({
      created_by_id: z.string().uuid(),
      created_by_user: z.union([User, z.null()]),
      created_date: z.string().datetime({ offset: true }),
      email: z.union([z.string(), z.null()]),
      enabled: z.boolean(),
      expires: z.union([z.string(), z.null()]),
      full_name: z.union([z.string(), z.null()]),
      id: z.string().uuid(),
      modified_by_id: z.string().uuid(),
      modified_by_user: z.union([User, z.null()]),
      modified_date: z.string().datetime({ offset: true }),
      unix_id: z.number().int(),
      username: z.string(),
    })
    .passthrough()
);
const AuthenticatedUser: z.ZodType<AuthenticatedUser> = z
  .object({ token: Token, user: User })
  .passthrough();
const ValidationErrorModel = z
  .object({
    ctx: z
      .union([z.object({}).partial().passthrough(), z.null()])
      .describe(
        "an optional object which contains values required to render the error message."
      ),
    loc: z
      .union([z.array(z.string()), z.null()])
      .describe("the error's location as a list. "),
    msg: z
      .union([z.string(), z.null()])
      .describe("a computer-readable identifier of the error type."),
    type_: z
      .union([z.string(), z.null()])
      .describe("a human readable explanation of the error."),
  })
  .partial()
  .passthrough();
const UserList: z.ZodType<UserList> = z.array(User);
const CreateUser = z.object({}).partial().passthrough();

export const schemas = {
  LoginRequest,
  Token,
  User,
  AuthenticatedUser,
  ValidationErrorModel,
  UserList,
  CreateUser,
};

export const AuthenticationEndpoints = makeApi([
  {
    method: "post",
    path: "/api/v1/auth/login",
    alias: "auth_login",
    requestFormat: "json",
    parameters: [
      {
        name: "body",
        type: "Body",
        schema: LoginRequest,
      },
    ],
    response: AuthenticatedUser,
    errors: [
      {
        status: 422,
        description: `Unprocessable Entity`,
        schema: z.array(ValidationErrorModel),
      },
    ],
  },
]);

export const useAuthenticationApi = () => {
  const userContext = useUserContext();
  return new Zodios(import.meta.env.VITE_API_URL, AuthenticationEndpoints, {
    axiosConfig: {
      headers: {
        Authorization: `Bearer ${userContext.user.token.access_token}`,
      },
    },
  });
};

export const UserEndpoints = makeApi([
  {
    method: "get",
    path: "/api/v1/users",
    alias: "get_users_list",
    requestFormat: "json",
    response: z.array(User),
  },
  {
    method: "post",
    path: "/api/v1/users",
    alias: "create_user",
    requestFormat: "json",
    parameters: [
      {
        name: "body",
        type: "Body",
        schema: z.object({}).partial().passthrough(),
      },
    ],
    response: User,
    errors: [
      {
        status: 422,
        description: `Unprocessable Entity`,
        schema: z.array(ValidationErrorModel),
      },
    ],
  },
]);

export const useUserApi = () => {
  const userContext = useUserContext();
  return new Zodios(import.meta.env.VITE_API_URL, UserEndpoints, {
    axiosConfig: {
      headers: {
        Authorization: `Bearer ${userContext.user.token.access_token}`,
      },
    },
  });
};
