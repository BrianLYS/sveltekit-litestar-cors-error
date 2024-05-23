<script lang="ts">
	// Import styles and components
	import '../app.postcss';
	import Header from '$lib/components/header.svelte';
	import { initializeStores, Modal, storePopup } from '@skeletonlabs/skeleton';

	// Floating UI for Popups
	import { computePosition, autoUpdate, flip, shift, offset, arrow } from '@floating-ui/dom';
	storePopup.set({ computePosition, autoUpdate, flip, shift, offset, arrow });

	// Initialise Modal Store
	initializeStores();
</script>

<div class="scrollable-container">
	<!-- Page Route Content -->
	<Header />
	<slot />
</div>

<style>
	.scrollable-container {
		overflow-y: auto;
		height: calc(100vh - 64px);
	}
</style>
