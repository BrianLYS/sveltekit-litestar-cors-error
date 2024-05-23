import { PUBLIC_BACKEND_URL } from '$env/static/public';

interface ValidateResponse {
	userId: string;
	username: string;
	// Add other properties as needed
}

export async function validate_token(id: string | undefined): Promise<ValidateResponse | false> {
	if (!id) {
		// console.error('No ID provided');
		return false;
	}

	try {
		const validateResponse = await fetch(PUBLIC_BACKEND_URL + '/accounts/validate_token', {
			method: 'GET',
			headers: {
				Cookie: `id=${id}`
			},
			credentials: 'include'
		});

		if (validateResponse.status === 200) {
			const data = await validateResponse.json();
			// console.log('Validation successful:', data);
			return data;
		} else {
			// console.error('Validation failed with status:', validateResponse.status);
			return false;
		}
	} catch (error) {
		// console.error('Error during validation:', error);
		return false;
	}
}
