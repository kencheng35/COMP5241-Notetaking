# NoteTaker - Personal Note Management Application

A modern, responsive web application for managing personal notes with a beautiful user interface and full CRUD functionality.

## 🌟 Features

- **Create Notes**: Add new notes with titles and rich content
- **Edit Notes**: Update existing notes with real-time editing
- **Delete Notes**: Remove notes you no longer need
- **Search Notes**: Find notes quickly by searching titles and content
- **Translate Notes**: Preview a translation and apply it to the current note
- **Auto-save**: Notes are automatically saved as you type
- **Responsive Design**: Works perfectly on desktop and mobile devices
- **Modern UI**: Beautiful gradient design with smooth animations
- **Real-time Updates**: Instant feedback and updates

## 🚀 Live Demo

The application is deployed and accessible at: **https://3dhkilc88dkk.manus.space**

## 🛠 Technology Stack

### Frontend
- **HTML5**: Semantic markup structure
- **CSS3**: Modern styling with gradients, animations, and responsive design
- **JavaScript (ES6+)**: Interactive functionality and API communication

### Backend
- **Python Flask**: Web framework for API endpoints
- **Supabase Python client**: Server-side access to the Supabase Data API
- **OpenRouter**: On-demand note translation via Nemotron 3 Ultra

### Database
- **Supabase Postgres**: Hosted database for data persistence

## 📁 Project Structure

```
notetaking-app/
├── src/
│   ├── routes/
│   │   ├── user.py          # User API routes (template)
│   │   └── note.py          # Note API endpoints
│   ├── static/
│   │   ├── index.html       # Frontend application
│   │   └── favicon.ico      # Application icon
│   ├── supabase_client.py   # Server-side Supabase API client
│   └── main.py              # Flask application entry point
├── venv/                    # Python virtual environment
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🔧 Local Development Setup

### Prerequisites
- Python 3.11+
- pip (Python package manager)
- A Supabase project URL and a server-side secret/service-role API key

### Installation Steps

1. **Clone or download the project**
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**
   ```bash
   source venv/bin/activate
   ```

   Remark: On Windows, use `venv\Scripts\activate`

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Supabase API**
   In your Supabase dashboard, copy the **Project URL** and a server-side **secret key** (`sb_secret_...`, or legacy `service_role` key) from **Settings → API Keys**. Do not use a Postgres connection string. A `sb_publishable_...` or anon key can list zero notes but cannot create notes with the RLS configuration below.

   Edit the `.env` file in the project root (beside `requirements.txt`):
   ```dotenv
   SUPABASE_URL=https://PROJECT_REF.supabase.co
   SUPABASE_KEY=YOUR_SERVER_SIDE_SECRET_KEY
   ```

   Replace the placeholders with your own values. The old `DATABASE_URL` setting is no longer used. The `.env` file is ignored by Git; never commit or share the key, or put it in frontend JavaScript. No shell environment variable is needed.

   Before starting the app, run the table-creation SQL below in the Supabase **SQL Editor**. The Data API cannot create tables automatically.

5. **Run the application**
   ```bash
   python src/main.py
   ```

6. **Access the application**
   - Open your browser and go to `http://localhost:5001`

   Existing SQLite data is not migrated automatically.

### Translation Setup

Add an OpenRouter API key to the same project-root `.env` file:

```dotenv
OPENROUTER_API_KEY=YOUR_OPENROUTER_API_KEY
```

The key stays on the Flask server. Restart Flask after adding it. Translation is optional; notes still work without it. Clicking **Translate** sends the current note content to OpenRouter using `nvidia/nemotron-3-ultra-550b-a55b:free` and shows a preview. **Use translation** replaces the editor content and saves it; **Discard** leaves the note unchanged. Never commit or expose the API key in browser code. The free model may be rate limited or temporarily unavailable.

## 📡 API Endpoints

### Notes API
- `GET /api/notes` - Get all notes
- `POST /api/notes` - Create a new note
- `GET /api/notes/<id>` - Get a specific note
- `PUT /api/notes/<id>` - Update a note
- `DELETE /api/notes/<id>` - Delete a note
- `GET /api/notes/search?q=<query>` - Search notes
- `POST /api/translate` - Translate text with `{ "text": "...", "language": "fr" }` (returns `{ "translation": "..." }`)

### Request/Response Format
```json
{
  "id": 1,
  "title": "My Note Title",
  "content": "Note content here...",
  "created_at": "2025-09-03T11:26:38.123456",
  "updated_at": "2025-09-03T11:27:30.654321"
}
```

## 🎨 User Interface Features

### Sidebar
- **Search Box**: Real-time search through note titles and content
- **New Note Button**: Create new notes instantly
- **Notes List**: Scrollable list of all notes with previews
- **Note Previews**: Show title, content preview, and last modified date

### Editor Panel
- **Title Input**: Edit note titles
- **Content Textarea**: Rich text editing area
- **Save Button**: Manual save option (auto-save also available)
- **Delete Button**: Remove notes with confirmation
- **Real-time Updates**: Changes reflected immediately

### Design Elements
- **Gradient Background**: Beautiful purple gradient backdrop
- **Glass Morphism**: Semi-transparent panels with backdrop blur
- **Smooth Animations**: Hover effects and transitions
- **Responsive Layout**: Adapts to different screen sizes
- **Modern Typography**: Clean, readable font stack

## 🔒 Database Schema

### Tables (run once in Supabase SQL Editor)
```sql
CREATE TABLE IF NOT EXISTS public.note (
   id bigint GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
   title varchar(200) NOT NULL,
   content text NOT NULL,
   created_at timestamptz NOT NULL DEFAULT now(),
   updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS public."user" (
   id bigint GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
   username varchar(80) NOT NULL UNIQUE,
   email varchar(120) NOT NULL UNIQUE
);

ALTER TABLE public.note ENABLE ROW LEVEL SECURITY;
ALTER TABLE public."user" ENABLE ROW LEVEL SECURITY;
```

The server-side secret/service-role key bypasses RLS. The Flask routes have no user authentication and can read or change all rows; keep this app local until you add authentication and authorization before deploying it publicly.

## 🚀 Deployment

The application is configured for easy deployment with:
- Frontend and API served from the same origin
- Local-only binding to `127.0.0.1` for development
- Persistent Supabase Postgres database

## 🔧 Configuration

### Local Configuration
- `.env`: Set `SUPABASE_URL` and `SUPABASE_KEY` (required)

### Database Configuration
- Database: Supabase Postgres through the Data API (no direct database socket)
- Tables must be created once in the Supabase SQL Editor

## 📱 Browser Compatibility

- Chrome/Chromium (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers (iOS Safari, Chrome Mobile)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

For issues or questions:
1. Check the browser console for error messages
2. Verify the Flask server is running
3. Ensure all dependencies are installed
4. Check network connectivity for the deployed version

## 🎯 Future Enhancements

Potential improvements for future versions:
- User authentication and multi-user support
- Note categories and tags
- Rich text formatting (bold, italic, lists)
- File attachments
- Export functionality (PDF, Markdown)
- Dark/light theme toggle
- Offline support with service workers
- Note sharing capabilities

---

**Built with ❤️ using Flask, Supabase Postgres, and modern web technologies**

