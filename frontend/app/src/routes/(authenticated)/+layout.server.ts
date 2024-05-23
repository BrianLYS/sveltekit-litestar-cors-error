import type { LayoutServerLoad } from './$types';
import { redirect } from '@sveltejs/kit';
import { validate_token } from '$lib/components/auth/auth';

export const load: LayoutServerLoad = async ({ locals }) => {
	// console.log('Load function called with locals:', locals);
	const id = locals.id;

	const validateResponse = await validate_token(id);

	if (validateResponse) {
		// console.log('User is authenticated, staying on authenticated page');
		return { user: validateResponse };
	} else {
		// console.log('User is not authenticated, redirecting to /login');
		throw redirect(302, '/login');
	}
};
