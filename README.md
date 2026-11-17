# RheumaSCE — iPhone Study App

A free, private-progress, offline-capable Progressive Web App (PWA) created from your uploaded **Rheumatology_SCE_Question_Bank_Corrected (1).pdf**.

## Contents

- `index.html`: the app screen
- `style.css`: comfortable warm, white and dark themes
- `app.js`: question navigation, answer reveals, search, bookmarks, progress and settings
- `questions.json`: **451** extracted questions, original five options, keyed answer and explanation
- `manifest.webmanifest`, `sw.js`, `icon-*.png`: iPhone Home Screen / offline support
- `build_data.py`: optional regeneration utility (requires the PDF and PyMuPDF; not needed to run or deploy)

## Deploy using GitHub Pages (free)

1. Sign in at https://github.com in Safari, select **+** > **New repository**. Name it `rheumasce-iphone` and choose **Public** (required for GitHub Pages on free personal accounts).
2. Extract the supplied ZIP in the **Files** app. In the repository select **Add file** > **Upload files**. Upload **all files inside** `RheumaSCE_iPhone_GitHub`, rather than uploading the ZIP itself. `index.html`, `questions.json`, `app.js`, `style.css` and `sw.js` **must be in the repository root** (not nested in a subfolder). Commit the changes. The `build_data.py` file is optional.
3. Open **Settings > Pages**, choose **Deploy from a branch**, select `main`, folder `/(root)`, then **Save**.
4. Your URL will usually be `https://YOUR-USERNAME.github.io/rheumasce-iphone/`. Replace `YOUR-USERNAME` with your GitHub username. Open this URL in Safari on your iPhone.
5. In **Safari**, tap **Share** > **Add to Home Screen** > **Add**. Open the new RheumaSCE icon. The app runs without an Apple Developer membership or App Store account.
6. After opening the installed app online for the first time and allowing the content to load, it can work offline. If a new version is uploaded, open it while online to refresh the cached files. Some content may take another reload to update.

**Important:** On iPhone, GitHub's mobile web interface may hide upload controls. Use **Request Desktop Website** in Safari or upload from a computer if needed. The free GitHub Pages URL is public; do not upload private or copyrighted material that you are not permitted to redistribute. If public hosting is inappropriate, self-host behind authentication instead.

## Features

- Adjustable reading size (15–26px), warm paper, bright light, and dark themes
- Focus mode to maximize reading space
- Full-text search of question, options and explanation
- All, unanswered, review mistakes, and saved filters
- Random questions and sequential navigation
- Immediate feedback with explanations
- Local progress and bookmarks, optional JSON export
- All content cached for offline use after initial online installation

## Caveats

The questions, answer choices, answer keys, and explanations are **reproduced** from the supplied PDF and not independently fact-checked against current guidelines. Original wording was joined across PDF line breaks and some typographic hyphen spacing was normalized. This app is intended for revision, not for direct clinical decision-making.

Data is stored in `localStorage` on the device/browser; it does **not** automatically sync, and clearing website data may erase progress. Use **Reading comfort > Export progress** to keep a backup. Export is currently backup-only; it does not support importing progress back into the app.

When deploying a changed version of `questions.json`, change `CACHE` in `sw.js` (for example `rheumasce-offline-v2`) to ensure the offline cache is refreshed reliably.
