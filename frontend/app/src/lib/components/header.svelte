<script lang="ts">
	import { AppBar, LightSwitch } from '@skeletonlabs/skeleton';
	import { page } from '$app/stores';
	import { PUBLIC_BACKEND_URL } from '$env/static/public';

	// Handle Logout
	async function handleLogout(event: Event) {
		event.preventDefault();
		const response = await fetch(PUBLIC_BACKEND_URL + '/accounts/logout', {
			method: 'POST',
			mode: 'cors',
			credentials: 'include'
		});

		if (response.ok) {
			location.reload();
		} else {
			console.error('Failed to logout:', response);
		}
	}
</script>

<AppBar background="bg-primary-200 dark:bg-primary-800">
	<svelte:fragment slot="lead"></svelte:fragment>
	<svelte:fragment slot="trail">
		{#if $page.data.id}
			<a class="btn btn-sm variant-ghost-surface" href="/dashboard"> Dashboard </a>
			<form on:submit={handleLogout}>
				<button type="submit" class="btn btn-sm variant-ghost-surface">Logout</button>
			</form>
		{:else}
			<a class="btn btn-sm variant-ghost-surface" href="/login"> Login </a>
			<a class="btn btn-sm variant-ghost-surface" href="/register"> Register </a>
		{/if}
		<LightSwitch rounded="rounded-full" />
	</svelte:fragment>
</AppBar>
<hr class="divider border-black dark:border-white" />
