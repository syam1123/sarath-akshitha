<template>
  <div class="about-container bride">
    <div class="about-section">
      <div class="image-container">
        <div class="image" />
      </div>
      <h1>Akshitha</h1>
      <h2>(5 things about her by him)</h2>
      <ul class="profile-details">
        <li>"Food, Sleep and Work - Favourite trio"</li>
        <li>"Can hold a conversation until 4am and go to work at 8"</li>
        <li>"Thought she is really cute when first met,... still does"</li>
        <li>"She knows i can't fix the internet" </li>
        <li>"Amsterdam, currenrt favourite destination"</li>
      </ul>
      <!-- <dl class="profile">
        <dt>Name</dt>
        <dd>Akshitha S Pillai</dd>
        <dt>Birthday</dt>
        <dd>13 November, 1994</dd>
        <dt>Childhood dream</dt>
        <dd>Doctor</dd>
        <dt>Current job</dt>
        <dd>Dental specialist</dd>
        <dt>Current location</dt>
        <dd>Chengannur</dd>
        <dt>Favorite destination</dt>
        <dd>Thailand</dd>
        <dt>Favorite food</dt>
        <dd>Appam & Duck roast</dd>
        <dt>Favorite drink</dt>
        <dd>Coffee</dd>
      </dl>-->
    </div>
  </div>
</template>
<script>
export default {
  name: 'AboutGroom'
}
</script>

<style>
.about-container{
  /* background: orange; */
  min-height: 100vh;
  height: auto;
  display: flex;
  align-items: center;
}
.image-container {
  width: 100%;
  height: 350px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.groom .image-container {
  background: url(https://www.crownpeak.com/images/Why/Tech-Companies/Take-off-color-burst1.jpg) no-repeat;
  background-size: contain;
  background-position: center;
}
.bride .image-container {
  background: url(https://freedesignfile.com/upload/2016/10/Stock-Photo-Splash-of-Color-background.jpg) no-repeat;
  background-size: 370px;
  background-position: center;
}
.image-container .image {
  width: 300px;
  height: 300px;
}
.bride .image {
  background: url(~assets/akshi.png) no-repeat;
  background-position: top 0px center;
  background-size: 100%;
}
.about-section h1{
  text-align: center;
  font-size: 40px;
  margin-top: 10px;
  font-family: fantasy;
}
.about-section h2{
  font-size: 1em;
  color: #c17209;
  margin-bottom: 10px;
}
.profile{
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  padding: 1em;
  margin: auto;
  margin-bottom: 2em;
  max-width: 500px;
  justify-content: space-between;
}
.profile dt {
  width: 45%;
  display: block;
  color: #777;
  padding-right: 1em;
}
.profile dd {
  width: 50%;
  margin: 0.3em 0em;
  font-weight: 500;
}
</style>
