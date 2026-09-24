import os

from dotenv import dotenv_values
from supabase import create_client


env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
config = dotenv_values(env_path)
supabase_url = config.get('SUPABASE_URL')
supabase_key = config.get('SUPABASE_KEY')

if not supabase_url or not supabase_key:
    raise RuntimeError('Set SUPABASE_URL and SUPABASE_KEY in the project-root .env file')
if not supabase_url.startswith('https://'):
    raise RuntimeError('SUPABASE_URL must be the HTTPS project URL from Supabase, not a Postgres URI')
if supabase_key.startswith('sb_publishable_'):
    raise RuntimeError('SUPABASE_KEY is a publishable key; use a server-side secret key from Supabase Settings > API Keys for RLS-protected tables')

supabase = create_client(supabase_url, supabase_key)