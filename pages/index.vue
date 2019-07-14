<template>
  <div class="wedding-container">
    <div class="banner-container">
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
      <div class="arrow-down">
        <i class="fa fa-angle-double-down"></i>
      </div>
    </div>
    <AboutGroom />
    <AboutBride />
    <Location />
  </div>
</template>

<script>
import Logo from '~/components/Logo.vue'
import AboutGroom from '~/components/AboutGroom'
import AboutBride from '~/components/AboutBride'
import Location from '~/components/Location'

export default {
  components: {
    Logo,
    AboutGroom,
    AboutBride,
    Location
  }
}
</script>

<style>
.banner-container {
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

.arrow-down{
  position: absolute;
  bottom: 20px;
}

.arrow-down i {
	-moz-animation: bounce 3s infinite;
	-webkit-animation: bounce 3s infinite;
	animation: bounce 3s infinite;
  font-size: 20px;
  color: #f07574;
}
@-moz-keyframes bounce {
  0%, 20%, 50%, 80%, 100% {
    -moz-transform: translateY(0);
    transform: translateY(0);
  }
  40% {
    -moz-transform: translateY(-30px);
    transform: translateY(-30px);
  }
  60% {
    -moz-transform: translateY(-15px);
    transform: translateY(-15px);
  }
}
@-webkit-keyframes bounce {
  0%, 20%, 50%, 80%, 100% {
    -webkit-transform: translateY(0);
    transform: translateY(0);
  }
  40% {
    -webkit-transform: translateY(-30px);
    transform: translateY(-30px);
  }
  60% {
    -webkit-transform: translateY(-15px);
    transform: translateY(-15px);
  }
}
@keyframes bounce {
  0%, 20%, 50%, 80%, 100% {
    -moz-transform: translateY(0);
    -ms-transform: translateY(0);
    -webkit-transform: translateY(0);
    transform: translateY(0);
  }
  40% {
    -moz-transform: translateY(-30px);
    -ms-transform: translateY(-30px);
    -webkit-transform: translateY(-30px);
    transform: translateY(-30px);
  }
  60% {
    -moz-transform: translateY(-15px);
    -ms-transform: translateY(-15px);
    -webkit-transform: translateY(-15px);
    transform: translateY(-15px);
  }
}
</style>
