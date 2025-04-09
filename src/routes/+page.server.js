import { loadNotes, saveNotes } from '$lib/notes';

export async function load() {
  const notes = await loadNotes();
  return { notes };
}

export const actions = {
  add: async ({ request }) => {
    const formData = await request.formData();
    console.log('Form Data (Add):', Object.fromEntries(formData)); // Debug log

    const notes = await loadNotes();
    const newNote = {
      id: Date.now(),
      title: formData.get('title') || '',
      page: formData.get('page') || '',
      book: formData.get('book') || '',
      tags: (formData.get('tags') || '').split(',').map(tag => tag.trim()).filter(Boolean),
      description: formData.get('description') || '',
      comments: formData.get('comments') || '',
      helpfulness: parseFloat(formData.get('helpfulness')) || 0, // Changed to parseFloat
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
    };
    notes.push(newNote);
    await saveNotes(notes);
    return { success: true };
  },

  edit: async ({ request }) => {
    const formData = await request.formData();
    console.log('Form Data (Edit):', Object.fromEntries(formData)); // Debug log

    const id = parseInt(formData.get('id'));
    const notes = await loadNotes();
    const updatedNote = {
      id,
      title: formData.get('title') || '',
      page: formData.get('page') || '',
      book: formData.get('book') || '',
      tags: (formData.get('tags') || '').split(',').map(tag => tag.trim()).filter(Boolean),
      description: formData.get('description') || '',
      comments: formData.get('comments') || '',
      helpfulness: parseFloat(formData.get('helpfulness')) || 0, // Changed to parseFloat
      createdAt: formData.get('createdAt'),
      updatedAt: new Date().toISOString(),
    };
    const updatedNotes = notes.map(note => (note.id === id ? updatedNote : note));
    await saveNotes(updatedNotes);
    return { success: true };
  },

  delete: async ({ request }) => {
    const formData = await request.formData();
    console.log('Form Data (Delete):', Object.fromEntries(formData)); // Debug log

    const id = parseInt(formData.get('id'));
    const notes = await loadNotes();
    const updatedNotes = notes.filter(note => note.id !== id);
    await saveNotes(updatedNotes);
    return { success: true };
  }
};