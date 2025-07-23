<script>
	import { onMount } from 'svelte';

	export let data;
	let notes = data.notes;
	let newNote = {
		title: '',
		page: '',
		book: '',
		tags: '',
		description: '',
		comments: '',
		helpfulness: 0
	};
	let editNote = null;
	let searchTitle = '';
	let searchBook = '';
	let searchTag = '';
	let searchKeyword = '';
	let searchRating = '';
	let randomCount = 10;

	let titleSelect;

	// Set up hotkey on mount
	onMount(() => {
		const handleKeydown = (event) => {
			if (
				event.key === '/' &&
				!['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName) &&
				!document.activeElement.isContentEditable
			) {
				event.preventDefault(); // Prevent browser default behavior (e.g., bookmark in some browsers)
				if (titleSelect) {
					titleSelect.focus();
					const filterSection = document.querySelector('#filter-section');
					filterSection.scrollIntoView({ behavior: 'instant', block: 'start' });
				}
			}
		};

		// Add event listener
		document.addEventListener('keydown', handleKeydown);

		// Cleanup on component destroy
		return () => {
			document.removeEventListener('keydown', handleKeydown);
		};
	});

	function resetNewNote() {
		newNote = {
			title: '',
			page: '',
			book: '',
			tags: '',
			description: '',
			comments: '',
			helpfulness: 0
		};
	}

	function startEdit(note) {
		// Find the original note from the source notes array
		const originalNote = notes.find((n) => n.id === note.id);
		if (originalNote) {
			editNote = { ...originalNote, tags: originalNote.tags.join(', ') };
			setTimeout(() => {
				const editSection = document.querySelector('#edit-section');
				if (editSection) {
					editSection.scrollIntoView({ behavior: 'instant', block: 'start' });
				}
			}, 0);
		}
	}

	let selectedBook = '';
	let selectedTag = '';

	// Get unique book titles
	$: uniqueBooks = [...new Set(notes.map((note) => note.book))].sort();
	$: uniqueTags = [...new Set(notes.flatMap((note) => note.tags))].sort();

	$: countHelpfulnessOne = notes.filter(note => note.helpfulness === 1).length;
	$: countHelpfulnessFivePlus = notes.filter(note => note.helpfulness >= 5).length;

	// Modified filteredNotes to use selectedBook
	$: filteredNotes = notes.filter((note) => {
		const matchesTitle = searchTitle
			? note.title.toLowerCase().includes(searchTitle.toLowerCase())
			: true;
		const matchesBook = selectedBook ? note.book === selectedBook : true;
		const matchesTag = selectedTag ? note.tags.includes(selectedTag) : true;
		const matchesKeyword = searchKeyword
			? note.description.toLowerCase().includes(searchKeyword.toLowerCase()) ||
				note.comments.toLowerCase().includes(searchKeyword.toLowerCase())
			: true;
		const matchesRating = searchRating ? note.helpfulness >= parseFloat(searchRating) : true;
		return matchesTitle && matchesBook && matchesTag && matchesKeyword && matchesRating;
	});

	// Update hasActiveFilter
	$: hasActiveFilter = selectedBook || searchTitle || selectedTag || searchKeyword || searchRating;
	let randomNotes = getRandomNotes(randomCount);

	// Update random notes when count changes or notes update
	$: randomNotes = getRandomNotes(randomCount);

	function getRandomNotes(count) {
		// Ensure count is valid
		const validCount = Math.min(Math.max(1, count || 0), notes.length);

		// Filter notes with helpfulness of exactly 1 or >= 5
		const eligibleNotes = notes.filter((note) => note.helpfulness === 6);
		// const eligibleNotes = notes.filter(note => note.helpfulness === 1 || note.helpfulness >= 5);

		// Create a copy of the filtered notes array
		const shuffled = [...eligibleNotes];

		// Fisher-Yates shuffle
		for (let i = shuffled.length - 1; i > 0; i--) {
			const j = Math.floor(Math.random() * (i + 1));
			[shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]]; // Swap elements
		}

		// Return the requested number of notes (or all if fewer are available)
		return shuffled.slice(0, validCount);
	}

	// Ensure randomNotes updates reactively
	$: randomNotes = getRandomNotes(randomCount);

	async function handleAdd(event) {
		const formData = new FormData(event.target);
		const response = await fetch('?/add', {
			method: 'POST',
			body: formData
		});
		const result = await response.json();
		resetNewNote();
	}

	async function handleEdit(event) {
		const formData = new FormData(event.target);
		const response = await fetch('?/edit', {
			method: 'POST',
			body: formData
		});
		const result = await response.json();
		editNote = null;
		searchTitle = '';
		searchBook = '';
		searchTag = '';
		searchKeyword = '';
		searchRating = '';
	}

	async function handleDelete(event) {
		const formData = new FormData(event.target);
		const response = await fetch('?/delete', {
			method: 'POST',
			body: formData
		});
		const result = await response.json();
		if (result.success) {
			notes = await loadNotesFromServer();
		}
	}

	async function loadNotesFromServer() {
		const response = await fetch('/api/notes');
		return await response.json();
	}

	function renderNoteDetails(note) {
		return `
            <strong>${note.title}</strong> (Page ${note.page || 'N/A'}, ${note.book})<br />
            Tags: ${note.tags.join(', ')}<br />
            <strong>Description</strong><br />${note.description}<br />
            <strong>Comments</strong><br />${note.comments}<br />
            Helpfulness: ${note.helpfulness}
        `;
	}
</script>

<main>
	<h1>Book Notes</h1>

	<!-- Add Note Form -->
	<section>
		<h2>Add Note</h2>
		<form method="POST" action="?/add" on:submit|preventDefault={handleAdd}>
			<input name="title" bind:value={newNote.title} placeholder="Title" required />
			<input name="page" bind:value={newNote.page} placeholder="Page Number" type="number" />
			<input name="book" bind:value={newNote.book} placeholder="Book" required />
			<input name="tags" bind:value={newNote.tags} placeholder="Tags (comma-separated)" />
			<textarea name="description" bind:value={newNote.description} placeholder="Description"
			></textarea>
			<textarea name="comments" bind:value={newNote.comments} placeholder="Comments"></textarea>
			<input
				name="helpfulness"
				bind:value={newNote.helpfulness}
				placeholder="Helpfulness (0-10)"
				type="number"
				min="0"
				max="10"
				step="0.1"
			/>
			<button type="submit">Add Note</button>
		</form>
	</section>

	<!-- Edit Note Form -->
	{#if editNote}
		<section id="edit-section">
			<h2>Edit Note</h2>
			<form method="POST" action="?/edit" on:submit|preventDefault={handleEdit}>
				<input type="hidden" name="id" value={editNote.id} />
				<input type="hidden" name="createdAt" value={editNote.createdAt} />
				<input name="title" bind:value={editNote.title} placeholder="Title" required />
				<input name="page" bind:value={editNote.page} placeholder="Page Number" type="number" />
				<input name="book" bind:value={editNote.book} placeholder="Book" required />
				<input name="tags" bind:value={editNote.tags} placeholder="Tags (comma-separated)" />
				<textarea name="description" bind:value={editNote.description} placeholder="Description"
				></textarea>
				<textarea name="comments" bind:value={editNote.comments} placeholder="Comments"></textarea>
				<input
					name="helpfulness"
					bind:value={editNote.helpfulness}
					placeholder="Helpfulness (0-10)"
					type="number"
					min="0"
					max="10"
					step="0.1"
				/>
				<button type="submit">Save</button>
				<button type="button" on:click={() => (editNote = null)}>Cancel</button>
			</form>
		</section>
	{/if}

	<!-- Search Filters -->
	<section id="filter-section">
		<h2>Filter Notes</h2>
		<input bind:value={searchTitle} bind:this={titleSelect} placeholder="Search by Title" />
		<select bind:value={selectedBook}>
			<option value="">Search by Book</option>
			{#each uniqueBooks as book}
				<option value={book}>{book}</option>
			{/each}
		</select>
		<select bind:value={selectedTag}>
			<option value="">Search by Tag</option>
			{#each uniqueTags as tag}
				<option value={tag}>{tag}</option>
			{/each}
		</select>
		<input bind:value={searchKeyword} placeholder="Search Description/Comments" />
		<input
			bind:value={searchRating}
			placeholder="Search by Helpfulness Rating"
			type="number"
			min="0"
			max="10"
			step="0.1"
		/>
	</section>

	<!-- Display Filtered Notes -->
	<section>
		<h2>Filtered Notes ({filteredNotes.length})</h2>
		{#if hasActiveFilter}
			<ul>
				{#each filteredNotes as note (note.id)}
					<li>
						{@html renderNoteDetails(note)}
						<br />
						<button on:click={() => startEdit(note)}>Edit</button>
						<form
							method="POST"
							action="?/delete"
							style="display: inline;"
							on:submit|preventDefault={handleDelete}
						>
							<input type="hidden" name="id" value={note.id} />
							<button type="submit">Delete</button>
						</form>
					</li>
				{/each}
			</ul>
		{:else}
			<p>Please apply a filter to view notes</p>
		{/if}
	</section>

	<!-- Random Notes -->
	<section>
		<h2>Random Notes ({countHelpfulnessFivePlus}) ({countHelpfulnessOne})</h2>
		<input bind:value={randomCount} type="number" min="1" placeholder="Number of random notes" />
		<ul>
			{#each randomNotes as note (note.id)}
				<li>
					{@html renderNoteDetails(note)}
				</li>
			{/each}
		</ul>
	</section>
</main>

<style>
	main {
		max-width: 800px;
		margin: 0 auto;
		padding: 20px;
	}
	section {
		margin-bottom: 20px;
	}
	input,
	textarea {
		display: block;
		margin: 5px 0;
		width: 100%;
		box-sizing: border-box;
		word-wrap: break-word;
		overflow-wrap: break-word;
		resize: vertical;
	}
	button {
		margin-right: 5px;
	}
	ul {
		list-style: none;
		padding: 0;
	}
	li {
		background-color: whitesmoke;
		border: 1px solid #ddd;
		padding: 10px;
		margin-bottom: 10px;
		word-wrap: break-word;
		overflow-wrap: break-word;
		max-width: 100%;
		overflow-x: auto;
	}
	select {
		color: gray;
		display: block;
		margin: 5px 0;
		width: 100%;
		padding-top: 1px;
		padding-bottom: 2px;
	}
	option {
		color: black;
	}
</style>
