# visionary_storytelling

Using AI Vision models for
- analysis
- multi-modal RAG (future scope)

## Jupyter Notebooks

- Teaching AI Vision models to cry "Werewolf"
    - [Ollama LLaVA Model](notebooks/ai_vision_image_classification_ollama.ipynb)
    - [OpenAI Vision Model](notebooks/ai_vision_image_classification_openai.ipynb)
    - [Google Gemini Vision Model](notebooks/ai_vision_image_classification_google.ipynb)
    - Behavior is relatively consistent, but given the quality of the werewolf image the rate of false negatives is higher 

### Core Prompt

- intended for general image classification to enable routing to specialized agents for detailed analysis

```
**Objective:** Analyze the image to categorize it and provide a standardized JSON output that includes a comprehensive summary of the initial analysis, ensuring consistency and conciseness for downstream processing.

**Process:**

1. **Visual Inspection:**
   - Summarize the primary visual content, noting prominent features such as objects, scenes, figures, or text.
2. **Contextual Clues:**
   - Note any context-specific elements indicating the image's purpose or origin.
3. **Image Type Identification:**
   - Classify the image into one of the predefined categories: `Artwork`, `Real-life Photograph`, `Business-related`, `Medical`, `Other`.
4. **Intended Audience:**
   - Speculate on the intended audience based on content and style.
5. **Initial Interpretation:**
   - Provide a brief interpretation of the image's conveyed or represented content.
6. **Special Attention Elements:**
   - Highlight elements requiring special attention in detailed analysis.
7. **Recommendation for Specialized Analysis:**
   - Indicate if the image is recommended for further analysis by a specialized tool.

**Output Structure:**

```json
{
  "imageType": "Category",
  "visualInspectionSummary": "Summary of the primary visual content.",
  "contextualClues": "Noted context-specific elements.",
  "intendedAudience": "Speculated audience.",
  "initialInterpretation": "Brief interpretation of the image content.",
  "specialAttentionElements": "Elements needing special attention.",
  "recommendedForDetailedAnalysis": true/false,
  "additionalDetails": {
    "potentialConcerns": "Any potential concerns for detailed analysis.",
    "comparativeAnalysis": "Comparative notes if applicable."
  }
}
```

### First Generation Prompt

- not as effective for general image classification, but still works best for identifying the werewolf in the pack

```
*Begin your image analysis by following these steps:*

Initial Impression: Describe your first reaction to the image and the overall mood or emotion it conveys.
Contextual Background: If known, provide any relevant historical, cultural, or artistic context of the image.
Detailed Walkthrough: Use art analysis techniques for a detailed examination of the image, focusing on composition, symbolism, and artistic choices.
Unrealistic and Fantastical Elements: Focus on features that are unrealistic or symbolic, especially in depictions of humans, creatures, or environments. Discuss how they differ from real-life counterparts and their potential meanings.

*Conclude your analysis with:*

- Overall Interpretation: Summarize your comprehensive understanding of the image, integrating the various elements you have analyzed.
```