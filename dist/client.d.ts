declare class ImageRecogniiton {
    private baseUrl;
    constructor(baseUrl?: string);
    recognize(image: File | Blob, question: string): Promise<ImageRecogniitonResponse>;
}
export default ImageRecogniiton;
interface ImageRecogniitonResponse {
    question: string;
    answer?: string;
    error?: string;
}
//# sourceMappingURL=client.d.ts.map