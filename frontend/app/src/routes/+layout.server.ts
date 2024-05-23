import type { LayoutServerLoad } from './$types';

export const load = (async ({ locals }) => {
	return {
		id: locals.id
	};
}) satisfies LayoutServerLoad;
