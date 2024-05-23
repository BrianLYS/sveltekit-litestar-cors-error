import type { Handle } from '@sveltejs/kit';

export const handle: Handle = async ({ event, resolve }) => {
	// Get the session token from the cookies
	const id = event.cookies.get('id');
	event.locals.id = id;

	return resolve(event);
};
