<template>
  <div class="container">
    <div>
      <logo />
      <h1 class="title">
        Sarath & Akshitha
      </h1>
      <h2 class="subtitle">
        Starting a new life on
      </h2>
      <p class="text">05 Sept 2019, 11.00am</p>
      <p class="text">at Thiruvanvandoor Gosalakrishna Temple</p>
    </div>
  </div>
</template>

<script>
import Logo from '~/components/Logo.vue'

export default {
  components: {
    Logo
  }
}
</script>

<style>
.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title {
  font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,
    'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.text {
  color: #565555;
  line-height: 20px;
}
</style>
