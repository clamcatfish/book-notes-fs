import { promises as fs } from 'fs';
import path from 'path';

const filePath = path.resolve('data/notes.json');

async function ensureDirectory() {
  await fs.mkdir(path.dirname(filePath), { recursive: true });
}

export async function loadNotes() {
  try {
    const data = await fs.readFile(filePath, 'utf-8');
    return JSON.parse(data);
  } catch (error) {
    if (error.code === 'ENOENT') {
      return [];
    }
    throw error;
  }
}

export async function saveNotes(notes) {
  await ensureDirectory();
  await fs.writeFile(filePath, JSON.stringify(notes, null, 2), 'utf-8');
}