import { z } from 'zod';

export const UserSchema = z.object({
    id: z.string().uuid(),
    unix_id: z.number().int().positive(),
    username: z.string(),
    enabled: z.boolean(),
    full_name: z.string().nullable(),
    email: z.string().email().nullable(),
    expires: z.coerce.date().nullable(),
    created_date: z.coerce.date(),
    created_by_id: z.string().uuid(),
    modified_date: z.coerce.date(),
    modified_by_id: z.string().uuid()
});

type User = z.infer<typeof UserSchema>;

export default User;