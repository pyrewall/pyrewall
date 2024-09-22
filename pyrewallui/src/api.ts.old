import { z } from "zod";

export type Token = z.infer<typeof Token>;
export const Token = z.object({
  access_token: z.string(),
  expires_in: z.number(),
});

export type User = {
  created_by_id: string;
  created_by_user: User | null | Array<User | null>;
  created_date: string;
  email: string | null | Array<string | null>;
  enabled: boolean;
  expires: string | null | Array<string | null>;
  full_name: string | null | Array<string | null>;
  id: string;
  modified_by_id: string;
  modified_by_user: User | null | Array<User | null>;
  modified_date: string;
  unix_id: number;
  username: string;
};
export const User: z.ZodType<User> = z.lazy(() =>
  z.object({
    created_by_id: z.string(),
    created_by_user: z.union([User, z.null(), z.array(z.union([User, z.null()]))]),
    created_date: z.string(),
    email: z.union([z.string(), z.null(), z.array(z.union([z.string(), z.null()]))]),
    enabled: z.boolean(),
    expires: z.union([z.string(), z.null(), z.array(z.union([z.string(), z.null()]))]),
    full_name: z.union([z.string(), z.null(), z.array(z.union([z.string(), z.null()]))]),
    id: z.string(),
    modified_by_id: z.string(),
    modified_by_user: z.union([User, z.null(), z.array(z.union([User, z.null()]))]),
    modified_date: z.string(),
    unix_id: z.number(),
    username: z.string(),
  }),
);
export type AuthenticatedUser = z.infer<typeof AuthenticatedUser>;
export const AuthenticatedUser = z.object({
  token: Token,
  user: User,
});

export type LoginRequest = z.infer<typeof LoginRequest>;
export const LoginRequest = z.object({
  password: z.string(),
  username: z.string(),
});

export type ValidationErrorModel = z.infer<typeof ValidationErrorModel>;
export const ValidationErrorModel = z.object({
  ctx: z.union([z.unknown(), z.null(), z.array(z.union([z.unknown(), z.null()]))]).optional(),
  loc: z.union([z.array(z.string()), z.null(), z.array(z.union([z.array(z.string()), z.null()]))]).optional(),
  msg: z.union([z.string(), z.null(), z.array(z.union([z.string(), z.null()]))]).optional(),
  type_: z.union([z.string(), z.null(), z.array(z.union([z.string(), z.null()]))]).optional(),
});

export type post_Api_v1_auth_login_api_v1_auth_login_post = typeof post_Api_v1_auth_login_api_v1_auth_login_post;
export const post_Api_v1_auth_login_api_v1_auth_login_post = {
  method: z.literal("POST"),
  path: z.literal("/api/v1/auth/login"),
  requestFormat: z.literal("json"),
  parameters: z.object({
    body: LoginRequest,
  }),
  response: AuthenticatedUser,
};

// <EndpointByMethod>
export const EndpointByMethod = {
  post: {
    "/api/v1/auth/login": post_Api_v1_auth_login_api_v1_auth_login_post,
  },
};
export type EndpointByMethod = typeof EndpointByMethod;
// </EndpointByMethod>

// <EndpointByMethod.Shorthands>
export type PostEndpoints = EndpointByMethod["post"];
export type AllEndpoints = EndpointByMethod[keyof EndpointByMethod];
// </EndpointByMethod.Shorthands>

// <ApiClientTypes>
export type EndpointParameters = {
  body?: unknown;
  query?: Record<string, unknown>;
  header?: Record<string, unknown>;
  path?: Record<string, unknown>;
};

export type MutationMethod = "post" | "put" | "patch" | "delete";
export type Method = "get" | "head" | MutationMethod;

type RequestFormat = "json" | "form-data" | "form-url" | "binary" | "text";

export type DefaultEndpoint = {
  parameters?: EndpointParameters | undefined;
  response: unknown;
};

export type Endpoint<TConfig extends DefaultEndpoint = DefaultEndpoint> = {
  operationId: string;
  method: Method;
  path: string;
  requestFormat: RequestFormat;
  parameters?: TConfig["parameters"];
  meta: {
    alias: string;
    hasParameters: boolean;
    areParametersRequired: boolean;
  };
  response: TConfig["response"];
};

type Fetcher = (
  method: Method,
  url: string,
  parameters?: EndpointParameters | undefined,
) => Promise<Endpoint["response"]>;

type RequiredKeys<T> = {
  [P in keyof T]-?: undefined extends T[P] ? never : P;
}[keyof T];

type MaybeOptionalArg<T> = RequiredKeys<T> extends never ? [config?: T] : [config: T];

// </ApiClientTypes>

// <ApiClient>
export class ApiClient {
  baseUrl: string = "";

  constructor(public fetcher: Fetcher) {}

  setBaseUrl(baseUrl: string) {
    this.baseUrl = baseUrl;
    return this;
  }

  // <ApiClient.post>
  post<Path extends keyof PostEndpoints, TEndpoint extends PostEndpoints[Path]>(
    path: Path,
    ...params: MaybeOptionalArg<z.infer<TEndpoint["parameters"]>>
  ): Promise<z.infer<TEndpoint["response"]>> {
    return this.fetcher("post", this.baseUrl + path, params[0]) as Promise<z.infer<TEndpoint["response"]>>;
  }
  // </ApiClient.post>
}

export function createApiClient(fetcher: Fetcher, baseUrl?: string) {
  return new ApiClient(fetcher).setBaseUrl(baseUrl ?? "");
}

/**
 Example usage:
 const api = createApiClient((method, url, params) =>
   fetch(url, { method, body: JSON.stringify(params) }).then((res) => res.json()),
 );
 api.get("/users").then((users) => console.log(users));
 api.post("/users", { body: { name: "John" } }).then((user) => console.log(user));
 api.put("/users/:id", { path: { id: 1 }, body: { name: "John" } }).then((user) => console.log(user));
*/

// </ApiClient
