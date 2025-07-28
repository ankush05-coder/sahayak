# Sahayak: AI-Powered Teaching Assistant for Multi-Grade Classrooms

## Overview
Sahayak is an AI-powered teaching assistant designed to empower teachers in under-resourced, multi-grade classrooms in India. It leverages Google AI technologies (Gemini API, Vertex AI Speech-to-Text) and Firebase Studio to deliver hyper-local content, differentiated materials, instant knowledge responses, visual aids, and innovative features like audio assessments and lesson planners. The solution is built using free tools to ensure accessibility and scalability.

## Tech Stack
- **Frontend**: HTML, JavaScript, Tailwind CSS (via CDN for simplicity).
- **Backend**: Firebase Functions (free tier) for serverless API calls.
- **AI Services**:
  - **Gemini API** (free tier via Google AI Studio) for text generation, multimodal content, and explanations.
  - **Vertex AI Speech-to-Text** (free tier for limited usage) for audio-based reading assessments.
- **Storage**: Firebase Firestore (free tier) for storing teacher profiles, generated content, and lesson plans.
- **Deployment**: Firebase Studio for no-code/low-code configuration and hosting.
- **Additional Tools**: Google Translate API (free tier) for multilingual support, Canvas API for generating simple visual aids.

## Approach to Solve Each Objective

### 1. Generate Hyper-Local Content
**Goal**: Allow teachers to request culturally relevant content in local languages (e.g., Marathi story about farmers and soil types).

- **Solution**:
  <!-- - Use the **Gemini API** (accessible via Google AI Studio's free tier) to generate text-based content like stories or explanations.
  - Teachers input requests via a simple web interface (e.g., "Create a story in Marathi about farmers to explain soil types").
  - Gemini generates the story, leveraging its ability to produce contextually relevant and culturally sensitive content.
  - **Google Translate API** (free tier) ensures the output is translated into the requested local language if Gemini's response is in English. -->
  <!-- - Store generated content in **Firebase Firestore** for reuse, allowing teachers to access past materials. -->

<!-- - **Implementation**:
  - Frontend: A form where teachers select the language and enter a prompt.
  - Backend: Firebase Function calls the Gemini API with the prompt and language, stores the response in Firestore, and returns it to the frontend.
  - Example Prompt: "Generate a 200-word story in Marathi about a farmer learning about soil types (loamy, sandy, clay) for 5th-grade students." -->

### 2. Create Differentiated Materials
**Goal**: Enable teachers to upload a textbook page photo, and generate worksheets tailored to different grade levels using a multimodal Gemini model.

- **Solution**:
  <!-- - Use **Gemini API's multimodal capabilities** (free tier in Google AI Studio) to process an uploaded image of a textbook page and extract text/content. -->
  <!-- - Generate multiple worksheet versions (e.g., for grades 3, 5, and 7) based on the extracted content, adjusting complexity using Gemini's text generation. -->
  - Store worksheets in **Firebase Firestore** as JSON objects (with fields for grade level, content, and questions).
  - Allow teachers to download worksheets as PDFs using a client-side library like jsPDF.

- **Implementation**:
  - Frontend: A file upload input for the textbook page image and a dropdown to select target grade levels.
  - Backend: Firebase Function processes the image via Gemini API, extracts text, and generates differentiated worksheets (e.g., simpler questions for lower grades, complex ones for higher grades).
  - Example: For a science textbook page on the water cycle, generate a grade 3 worksheet with basic fill-in-the-blanks, a grade 5 worksheet with short-answer questions, and a grade 7 worksheet with analytical questions.

### 3. Act as an Instant Knowledge Base
**Goal**: Provide simple, accurate explanations for student questions in the local language with analogies (e.g., "Why is the sky blue?").

- **Solution**:
  - Use **Gemini API** to generate concise, student-friendly explanations with analogies tailored to the cultural context.
  - Teachers input questions via the web interface, specifying the language and grade level.
  - Gemini crafts responses (e.g., "The sky is blue because sunlight scatters tiny air particles, like how water looks blue when you stir it with a spoon").
  - **Google Translate API** ensures accurate translation into languages like Hindi, Marathi, or Tamil.
  - Store FAQs in **Firebase Firestore** for quick retrieval in future sessions.

- **Implementation**:
  - Frontend: A text input for questions and a language selector.
  - Backend: Firebase Function queries Gemini API with the question and grade level, translates the response if needed, and stores it in Firestore.
  - Example Response: For "Why is the sky blue?" in Hindi for grade 4, Gemini might explain scattering using an analogy of sunlight filtering through a dusty village window.

### 4. Design Visual Aids
**Goal**: Generate simple line drawings or charts (e.g., water cycle diagram) for blackboard replication.

- **Solution**:
  - Use the **HTML5 Canvas API** to programmatically generate simple line drawings or charts based on teacher descriptions.
  - Teachers input a description (e.g., "Draw a water cycle chart for grade 5").
  - **Gemini API** interprets the description and generates a JSON structure for the chart (e.g., coordinates for lines, labels for stages).
  - Canvas API renders the chart on the frontend, which teachers can save as an image or replicate on a blackboard.
  - Store chart data in **Firebase Firestore** for reuse.

- **Implementation**:
  - Frontend: A form for entering the chart description and a canvas element to display the output.
  - Backend: Firebase Function uses Gemini to convert the description into a JSON structure (e.g., `{ "type": "cycle", "stages": ["evaporation", "condensation", "precipitation"] }`).
  - Frontend renders the chart using Canvas API and allows image download.

### 5. Go Beyond: Innovative Features
**Audio-Based Reading Assessments**:
- Use **Vertex AI Speech-to-Text** (free tier for limited usage) to analyze student audio recordings for reading fluency and pronunciation.
- Teachers upload audio files of students reading a passage via the web interface.
- Vertex AI transcribes the audio, and Gemini evaluates accuracy by comparing it to the original text, providing feedback (e.g., "Student mispronounced 'precipitation'").
- Store results in **Firebase Firestore** for tracking progress.

**On-the-Fly Educational Game Generation**:
- Use **Gemini API** to generate simple game ideas (e.g., a quiz game on soil types) with questions and answers tailored to grade levels.
- Implement games as interactive HTML/JavaScript components (e.g., multiple-choice quizzes) using Firebase-hosted web pages.
- Store game templates in **Firebase Firestore**.

**AI-Powered Weekly Lesson Planners**:
- Teachers input a topic, grade levels, and duration (e.g., "One-week plan for water cycle, grades 3-5").
- **Gemini API** generates a structured lesson plan with objectives, activities, and assessments.
- Store plans in **Firebase Firestore** and allow export as PDF.

## Deployment with Firebase Studio
- **Firebase Studio**: Use Firebase Studio's no-code/low-code interface to configure the project:
  - Set up **Firebase Hosting** to serve the web app.
  - Configure **Firebase Functions** for API calls to Gemini and Vertex AI.
  - Use **Firestore** to manage teacher data, generated content, and lesson plans.
  - Enable **Firebase Authentication** (free tier) for teacher login using email or Google accounts.
- **Steps**:
  1. Initialize a Firebase project in Firebase Studio.
  2. Deploy the frontend (HTML, JavaScript, Tailwind CSS) to Firebase Hosting.
  3. Set up Firebase Functions for Gemini API and Vertex AI calls.
  4. Configure Firestore collections for content, worksheets, and lesson plans.
  5. Test the app locally using Firebase Emulator Suite (free) before deployment.








| Function                   | Tool                                                   |
| -------------------------- | ------------------------------------------------------ |
| LLM (core assistant)       | **Gemini Pro / Gemini 1.5**                            | complete
| Image generation / drawing | Gemini Vision or Gemini Image model                    | complete
| OCR                        | PaddleOCR or Tesseract                                 |
| Audio → Text               | **Whisper (open-source)**                              |
| Auth & DB                  | Supabase or PocketBase                                 |
| Hosting                    | Vercel / Render                                        |
| Frontend                   | Streamlit (for demo), Flutter / React (for mobile app) |
