<script lang="ts">
  let message: string = ''
  let messageLimit: number = 100
  let isLoading: boolean = false
  let isSpam: boolean = false

  async function handleClick () {
    isLoading = true
    try {
      const response = await fetch('https://spamhampy.herokuapp.com/api/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message })
      })
      
      const data = await response.json()
      isLoading = false
      isSpam = data.isSpam
      message = ''
    } catch(err) {
      console.log(err)
    } 
  }
</script>

<main class="p-4 mx-auto max-w-none sm:max-w-lg text-black">
	<h1 class="mb-4 text-[#ef6fb5] uppercase text-6xl">Is it spam<br>or ham?</h1>
	<p class="my-2">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Temporibus praesentium labore ad laudantium est numquam possimus velit aliquam, exercitationem nihil excepturi voluptatum voluptates. Deserunt, fuga? Nobis omnis nostrum quibusdam distinctio!</p>
  <div class="mt-4 text-center uppercase text-2xl {isSpam ? 'text-red-600' : 'text-[#ef6fb5]'}">
    {isSpam ? 'This is spam!' : 'This is probably not spam?'}
  </div>
  <textarea
    class="p-3 my-2 border-black shadow-[5px_5px_#00000045] rounded-none outline-none transition-shadow
    text-lg w-full resize-none hover:shadow-[7px_7px_#00000045] focus:shadow-[7px_7px_#00000045]"
    placeholder="Write your message here!"
    bind:value={message}
    maxlength={messageLimit}
  />
  <div class="flex flex-col items-end gap-3">
    {message.length} / {messageLimit}
    <button
      class="px-4 py-2 border-black shadow-[5px_5px_#00000045] rounded-none font-bold outline-none transition-shadow
      hover:shadow-[7px_7px_#00000045] focus:shadow-[7px_7px_#00000045] flex gap-3 items-center justify-around
      {isLoading ? 'pointer-events-none opacity-50 cursor-not-allowed' : undefined}"
      disabled={isLoading}
      on:click={handleClick}
    >
    {#if isLoading}
        <div
          class="w-5 h-5 animate-spin rounded-full border-4 
          border-[#ef6fb552] border-r-[#ef6fb5]">
          Processing...
        </div>
      {:else}
        Spam 🤢🤮 or ham 😍?
      {/if}
    </button>
  </div>
</main>

<style lang="postcss" global>
  @tailwind base;
  @tailwind components;
  @tailwind utilities;
</style>
