import React from "react";
import { UserContextProvider } from "./contexts/UserContext";
import Layout from "./components/Layout";
import AppRoutes from "./pages/Routes";

const App: React.FC = () => {
  return <>
    <UserContextProvider>
      <AppRoutes />
    </UserContextProvider>
  </>;
};

export default App;
