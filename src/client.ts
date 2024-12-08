class ImageRecogniiton {
  private baseUrl: string;

  constructor(baseUrl: string = 'http://localhost:5000') {
    this.baseUrl = baseUrl;
  }

  async recognize(image: File | Blob, question: string): Promise<ImageRecogniitonResponse> {
    const formData = new FormData();
    formData.append('image', image);
    formData.append('question', question);

    try {
      const response = await fetch(this.baseUrl, {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const result: ImageRecogniitonResponse = await response.json();
      return result;
    } catch (error) {
      return { question, error: 'Error checking image' };
    }
  }
}

export default ImageRecogniiton;

interface ImageRecogniitonResponse {
  question: string;
  answer?: string;
  error?: string;
}
