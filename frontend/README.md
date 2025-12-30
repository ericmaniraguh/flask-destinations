# Destination Manager - Frontend (React)

This directory contains the user interface for the Destination Manager application, built with **React** and **Vite**.

## 📂 Project Structure

The project is organized as follows:

- **`src/main.jsx`**: The entry point of the React application.
- **`src/App.jsx`**: Handles the main routing setup using `react-router-dom`.
- **`src/components/`**: Contains the functional UI components.

## 🧩 Components

### 1. `DestinationList.jsx`

- **Purpose**: Fetches and displays the list of all travel destinations.
- **Key Features**:
  - Uses `useEffect` to fetch data from the API on mount.
  - Renders a grid of destination cards with images, ratings, and descriptions.
  - Provides "Edit" and "Delete" buttons for each item.
  - Handles deletion logic with user confirmation.

### 2. `DestinationForm.jsx`

- **Purpose**: A reusable form component for both **Creating** and **Updating** destinations.
- **Key Features**:
  - **Dynamic Mode**: Detects if it's in "Create" or "Edit" mode based on the URL parameter (`id`).
  - **State Management**: Manages form inputs (`destination`, `country`, `rating`, `image`).
  - **API Integration**: Sends `POST` requests to create new items and `PUT` requests to update existing ones.

### 3. `App.css`

- **Purpose**: Contains global styles and component-specific styling (Cards, Navbar, Forms).
- **Style**: Uses a clean, card-based layout with a responsive grid system.

## 🚀 Setup & Installation

1.  **Navigate to the frontend directory**:

    ```bash
    cd frontend
    ```

2.  **Install Dependencies**:

    ```bash
    npm install
    ```

3.  **Run the Development Server**:
    ```bash
    npm run dev
    ```
    The app will typically start at `http://localhost:5173`.

## 🧪 How to Test the UI

Ensure your Backend API is running on `http://localhost:5000` before testing.

1.  **View Destinations**:

    - Open the app in your browser.
    - You should see a grid of destination cards (or a "No destinations" message if empty).

2.  **Add a Destination**:

    - Click the **"+ Add New Destination"** button.
    - Fill in the form (Name, Country, Rating, Image URL).
    - Click **Create**. You should be redirected to the home page with the new item visible.

3.  **Edit a Destination**:

    - Click the **"Edit"** button on any card.
    - Change a value (e.g., update the Rating).
    - Click **Update**. The change should be reflected immediately on the list.

4.  **Delete a Destination**:
    - Click the **"Delete"** button on a card.
    - Confirm the browser alert popup.
    - The item should disappear from the list.
