interface String {
    trimOrNull(): string|null;
}

String.prototype.trimOrNull = function (): string | null {
    const responseString = this.trim();
    if (responseString.length === 0) {
        return null;
    }
    return responseString;
}