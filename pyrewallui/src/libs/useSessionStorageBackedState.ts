import React, { useEffect, useState } from 'react';

import { sessionObjectStorage } from './ObjectStorage';

const useSessionStorageBackedState = <T>(storageKey: string, initialState: T): [T, (state: React.SetStateAction<T>) => void] => {
  const [internalState, setState] = useState<T>(sessionObjectStorage.tryGet<T>(storageKey) ?? initialState);

  useEffect(() => {
    sessionObjectStorage.set(storageKey, internalState);
  }, [internalState]);

  return [internalState, setState];
};

export default useSessionStorageBackedState;