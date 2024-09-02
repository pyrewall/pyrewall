import React from "react";
import { UserContextProvider } from "./contexts/UserContext";

const App: React.FC = () => {
  return <>
    <UserContextProvider>
      <></>
    </UserContextProvider>
  </>;
};

export default App;
