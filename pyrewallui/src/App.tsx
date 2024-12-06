import React from "react";
import { UserContextProvider } from "./contexts/UserContext";
import AppRoutes from "./pages/Routes";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

const queryClient = new QueryClient();

const App: React.FC = () => {
  return <>
    <QueryClientProvider client={queryClient}>
      <UserContextProvider>
        <AppRoutes />
      </UserContextProvider>
    </QueryClientProvider>
  </>;
};

export default App;
