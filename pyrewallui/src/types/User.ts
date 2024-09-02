import { z } from 'zod';

export const UserSchema = z.object({

});

type User = z.infer<typeof UserSchema>;

export default User;