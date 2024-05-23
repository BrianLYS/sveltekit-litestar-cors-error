import type { LayoutServerLoad } from './$types';
import { redirect } from '@sveltejs/kit';
import { validate_token } from '$lib/components/auth/auth';

export const load: LayoutServerLoad = async ({ locals }) => {
	// console.log('Load function called with locals:', locals);
	const id = locals.id;

	const validateResponse = await validate_token(id);

	if (validateResponse) {
		// console.log('User is authenticated, redirecting to /dashboard');
		throw redirect(302, '/dashboard');
	} else {
		// console.log('User is not authenticated, staying on auth page');
		return {};
	}
};
