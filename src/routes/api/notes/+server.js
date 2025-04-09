import { loadNotes } from '$lib/notes';
import { json } from '@sveltejs/kit';

export async function GET() {
  const notes = await loadNotes();
  return json(notes);
}