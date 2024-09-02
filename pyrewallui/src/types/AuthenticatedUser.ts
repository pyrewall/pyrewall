import { z } from 'zod';
import { UserSchema } from './User';

export const AuthenticatedUserSchema = z.object({
    user: UserSchema,
    token: z.object({
        access_token: z.string(),
        expires_in: z.number().int().positive()
    })
});

type AuthenticatedUser = z.infer<typeof AuthenticatedUserSchema>;

export default AuthenticatedUser;