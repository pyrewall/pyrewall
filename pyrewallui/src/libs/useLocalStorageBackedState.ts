import React, { useEffect, useState } from 'react';

import { localObjectStorage } from './ObjectStorage';

const useLocalStorageBackedState = <T>(storageKey: string, initialState: T): [T, (state: React.SetStateAction<T>) => void] => {
  const [internalState, setState] = useState<T>(localObjectStorage.tryGet<T>(storageKey) ?? initialState);

  useEffect(() => {
    localObjectStorage.set(storageKey, internalState);
  }, [internalState]);

  return [internalState, setState];
};

export default useLocalStorageBackedState;