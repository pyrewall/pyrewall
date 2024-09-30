import React, { useState } from "react";
import { Modal, ModalBody, ModalFooter, ModalHeader } from "../../../components/Modal";
import { useNavigate } from "react-router-dom";
import { useUserApi } from "../../../api";
import { useMutation } from "@tanstack/react-query";

import '../../../libs/string.extensions';
import Label from "../../../components/Label";
import Input from "../../../components/Input";

const SystemCreateUserPage: React.FC = () => {
    const userApi = useUserApi();
    const navigate = useNavigate();

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
    const [enabled, setEnabled] = useState(true);
    const [fullName, setFullName] = useState('');
    const [expires, setExpires] = useState(false);
    const [expiresDate, setExpiresDate] = useState(new Date())
    const [userId, setUserId] = useState(-1);

    const saveUserMutation = useMutation({
        mutationFn: async () => {
            const data = {
                username,
                password,
                enabled,
                email: email.trimOrNull(),

            };

            const newUser = await userApi.create_user(data);
        }
    })

    const close = () => {
        navigate('..')
    }

    return <>
        <Modal show={true} closeModal={close}>
            <ModalHeader>Create User</ModalHeader>
            <ModalBody>
                <div>
                    <Label htmlFor="username">Username</Label>
                    <Input id="username" value={username} onChange={(e) => setUsername(e.target.value)} />
                </div>
            </ModalBody>
            <ModalFooter></ModalFooter>
        </Modal>
    </>
};  

export default SystemCreateUserPage;