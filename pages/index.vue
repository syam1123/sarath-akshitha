<template>
  <div class="wedding-container">
    <div class="banner-container">
      <div id="introduction">
        <logo />
        <h1 class="title">
          Sarath & Akshitha
        </h1>
        <h2 class="subtitle">
          Starting a new life on
        </h2>
        <p class="text">05 Sept 2019, 11.00am</p>
        <p class="text"><a href="https://goo.gl/maps/Q4CzCsjtqjnxJUKL9">at Thiruvanvandoor Gosalakrishna Temple</a></p>
      </div>
      <div class="arrow-down">
        <i class="fa fa-angle-double-down"></i>
      </div>
    </div>
    <div class="about-main-container">
      <AboutGroom />
      <AboutBride />
    </div>
    <!-- <div class="engagement-container">
      <div class="overlay">
        <h2>Engagement</h2>
        <h1>Monday, 08 JUL 2019</h1>
      </div>
    </div> -->
    <Location />
    <Rsvp />
    <Instagram />
    <div class="credits">
      Created with ❤️ by <a href="https://syamsp.com" target="_blank">@Syam</a>
    </div>
  </div>
</template>

<script>
import Logo from '~/components/Logo.vue'
import AboutGroom from '~/components/AboutGroom'
import AboutBride from '~/components/AboutBride'
import Location from '~/components/Location'
import Instagram from '~/components/Instagram'
import Rsvp from '~/components/Rsvp'

export default {
  components: {
    Logo,
    AboutGroom,
    AboutBride,
    Location,
    Instagram,
    Rsvp
  }
}
</script>

<style>
body {
  font-family: 'Work Sans', sans-serif;
}
.subtitle,.title {
  font-family: 'Satisfy', cursive;
}

#introduction a {
  text-decoration: none !important;
  color: black;
}

.wedding-container{
  overflow: hidden;
}

.banner-container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  background: gray url(https://t4.ftcdn.net/jpg/02/40/24/73/240_F_240247304_b8OlrQSQIqrXnuaUp2hhTGU1ozobtP9K.jpg) repeat 0 0;
  width: 100%;
  margin: 0;
  text-align: center;
  height: 100vh;
  padding-top: 150px;
  box-sizing: border-box;
  -webkit-animation: slide 40s linear infinite;
  animation: slide 40s linear infinite;
  background-repeat: repeat-x;
  background-color: white;
  height: auto;
}

.title {
  display: block;
  font-weight: 600;
  font-size: 62px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 16px;
  color: #526488;
  padding-bottom: 15px;
}

.text {
  color: #565555;
  line-height: 24px;
  font-size: 20px;
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

.about-main-container {
  display: flex;
  max-width: 1200px;
  width: 95%;
  justify-content: space-between;
  margin: 3em auto;
  height: auto;
}

.engagement-container {
  height: 400px;
  -webkit-animation: slide 20s linear infinite;
  animation: slide 20s linear infinite;
  background-image: url('~assets/engagement.png');
  position: relative;
}

.overlay {
  position: absolute;
  top: 0;
  right: 0;
  left: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  color: white;
}

.credits {
  background: black;
  color: white;
  text-align: center;
  padding: 1em;
  font-family: lato;
}

.credits a{
  color: #fff;
  text-decoration: none;
  font-weight: 600;
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

@keyframes slide {
  0% { background-position: 0 0; }
  5% { background-position: -10px 0;}
  45% { background-position: -190px 0; }
  50% { background-position: -200px 0; }
  55% { background-position: -190px 0; }
  95% { background-position: -10px 0;}
  100% { background-position: 0 0; }
}

@media screen and (max-width: 500px) {
  .title{
    font-size: 36px;
  }
  .subtitle{
    font-size: 14px;
  }
  .text {
    color: #565555;
    line-height: 20px;
    font-size: 16px;
    font-weight: 500;
    /* color: #440202; */
  }
}

@media screen and (max-width: 800px) {
  .about-main-container {
    flex-direction: column;
  }

  .about-container.bride {
    margin-top: 2em;
  }
}
</style>
