<script lang="ts">
	import { goto } from '$app/navigation';
	import { errorStore } from '$lib/stores';

	// Modal Utils
	import { getModalStore } from '@skeletonlabs/skeleton';
	import type { ModalSettings } from '@skeletonlabs/skeleton';

	// Environment Variables
	import { PUBLIC_BACKEND_URL } from '$env/static/public';

	const modalStore = getModalStore();

	// Form data
	let username: string;
	let password: string;
	let keepLoggedIn: boolean;
	let error: string | null = null;

	// Sync the store with a local variable
	$: $errorStore, (error = $errorStore);

	function modalAlert(message: string): void {
		const modal: ModalSettings = {
			type: 'alert',
			title: 'Error',
			body: message
		};
		modalStore.trigger(modal);
	}

	async function handleSubmit() {
		try {
			const response = await fetch(PUBLIC_BACKEND_URL + '/accounts/login', {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify({ username, password }),
				mode: 'cors',
				credentials: 'include'
			});

			if (response.ok) {
				const data = await response.json();
				const token = data.token;

				if (token) {
					goto('/dashboard', { replaceState: true });
					location.reload();
				} else {
					throw new Error('Token not found in response');
				}
			} else {
				const { message } = await response.json();
				throw new Error(`Error: ${message}`);
			}
		} catch (err) {
			const errorMessage = (err as Error).message;
			errorStore.set(errorMessage);
			modalAlert(errorMessage);
		}
	}
</script>

<div class="wrapper">
	<div class="card p-6 space-y-6 shadow-xl">
		<p class="font-semibold">Welcome, login with</p>
		<div class="flex flex-wrap space-y-4 space-x-0 md:flex-nowrap md:space-x-4 md:space-y-0">
			<button class="btn variant-ringed-surface w-full gap-2"
				><i class="fa-brands fa-google"></i>Google</button
			>
			<button class="btn text-white w-full gap-2" style="background-color: #4267B2;"
				><i class="fa-brands fa-facebook"></i>Facebook</button
			>
		</div>
		<div class="text-center">
			<hr class="-mb-4" />
			<span class="bg-surface-100-800-token p-2 text-sm">Or continue with email</span>
		</div>
		<form class="space-y-4" on:submit|preventDefault={handleSubmit}>
			<label class="label">
				<span>Email</span>
				<input
					type="email"
					bind:value={username}
					placeholder="your-email@example.com"
					class="input"
				/>
			</label>
			<label class="label">
				<span>Password</span>
				<input type="password" bind:value={password} placeholder="Your password" class="input" />
			</label>
			<label class="inline-flex items-center">
				<input type="checkbox" bind:checked={keepLoggedIn} class="checkbox" />
				<span class="ml-2">Keep me logged in</span>
			</label>
			<button class="btn variant-filled-primary w-full">Login</button>
		</form>
		<div class="flex justify-between flex-wrap">
			<p class="text-sm unstyled py-2 text-slate-500">
				Don't have an account? <a href="/">Register</a>
			</p>
		</div>
	</div>
</div>

<style>
	.wrapper {
		display: flex;
		justify-content: center;
		align-items: center;
		height: 80vh;
		width: 100%; /* Ensure the wrapper takes full width */
	}

	.card {
		width: 100%; /* Make the card take full width of the wrapper */
		max-width: 600px;
	}
</style>
