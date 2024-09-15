
// ? Should we optimize this for JS primitives
class ObjectStorage {
    private readonly storage: Storage;
  
    constructor(storage: Storage) {
      this.storage = storage;
    }
  
    clear(): void {
      this.storage.clear();
    }
  
    remove(key: string): void {
      this.storage.removeItem(key);
    }
  
    exists(key: string): boolean {
      return this.storage.getItem(key) !== null;
    }
  
    set<T>(key: string, value: T): void {
      this.storage.setItem(key, JSON.stringify(value));
    }
  
    tryGet<T>(key: string): T | null {
      const jsonValue = this.storage.getItem(key);
  
      if (jsonValue === null) return null;
  
      try {
        const value = JSON.parse(jsonValue) as T;
        return value;
      } catch {
        console.error('Failed to parse value for key: ', key);
        this.remove(key);
        return null;
      }
    }
  
    get<T>(key: string): T {
      const jsonValue = this.storage.getItem(key);
  
      if (jsonValue === null) throw Error(`Missing item for key "${key}"`);
  
      try {
        const value = JSON.parse(jsonValue) as T;
        return value;
      } catch {
        this.remove(key);
        throw Error(`Invalid value for key ${key}: ${jsonValue}`);
      }
    }
  }
  
  export const localObjectStorage = new ObjectStorage(localStorage);
  export const sessionObjectStorage = new ObjectStorage(sessionStorage);