<script lang="ts">
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { PUBLIC_BACKEND_URL } from '$env/static/public';

	let email = '';
	let password = '';
	let confirmPassword = '';
	let agreeToTerms = false;
	let errorMessage = '';

	async function handleRegister(event: Event) {
		event.preventDefault();

		if (password !== confirmPassword) {
			errorMessage = 'Passwords do not match';
			return;
		}

		const response = await fetch(PUBLIC_BACKEND_URL + '/accounts/register', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				email,
				password,
				username: email // Assuming username is the same as email
			})
		});

		const result = await response.json();

		if (response.ok) {
			// Handle successful registration (e.g., redirect to login page)
			goto('/login');
		} else {
			// Handle error
			errorMessage = result.error || 'Registration failed';
		}
	}
</script>

<header class="text-center py-4">
	<div class="text-center mb-2 text-3xl font-bold">Create an Account</div>
	<p class="unstyled text-sm md:text-base opacity-50">
		Already have an account? <a href="/login">Login</a>
	</p>
</header>
<div class="container mx-auto max-w-md">
	<div class="card p-6 space-y-6 shadow-xl text-left">
		<form class="space-y-4" on:submit={handleRegister}>
			<label class="label">
				<span>Email</span>
				<input type="email" placeholder="your-email@example.com" class="input" bind:value={email} />
			</label>
			<label class="label">
				<span>Password</span>
				<input type="password" placeholder="Your password" class="input" bind:value={password} />
			</label>
			<label class="label">
				<span>Confirm Password</span>
				<input
					type="password"
					placeholder="Confirm your password"
					class="input"
					bind:value={confirmPassword}
				/>
			</label>
			<label class="inline-flex items-center">
				<input type="checkbox" class="checkbox" bind:checked={agreeToTerms} />
				<span class="ml-2">I agree to the terms and conditions</span>
			</label>
			{#if errorMessage}
				<p class="text-red-500">{errorMessage}</p>
			{/if}
			<button class="btn variant-filled-primary w-full" type="submit" disabled={!agreeToTerms}
				>Register</button
			>
		</form>
	</div>
</div>

<style>
	.container {
		max-width: 400px; /* Adjust the max-width as needed */
		margin: 0 auto;
	}
</style>
