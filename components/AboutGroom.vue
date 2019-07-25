<template>
  <div class="about-container groom">
    <div class="about-section">
      <div class="image-container">
        <div class="image" />
      </div>
      <h1>Sarath</h1>
      <h2>(5 things about him by her)</h2>
      <ul class="profile-details">
        <li>"Proud of him on following his passion"</li>
        <li>"Give advices for an hour and say he hates advices"</li>
        <li>"Until I meet him, bugs were just insects"</li>
        <li>"Amma mon (Mom's child)"</li>
        <li>"Never get's bored of listening to him"</li>
      </ul>
      <!-- <dl class="profile">
        <dt>Name</dt>
        <dd>Sarath Sadasivan Pillai</dd>
        <dt>Birthday</dt>
        <dd>13 November, 1992</dd>
        <dt>Childhood dream</dt>
        <dd>Computer engineer (I called so)</dd>
        <dt>Current job</dt>
        <dd>Sr. Software engineer at Messagebird</dd>
        <dt>Current location</dt>
        <dd>Amsterdam</dd>
        <dt>Favorite destination</dt>
        <dd>Norway</dd>
        <dt>Favorite food</dt>
        <dd>Kappa & beef fry</dd>
        <dt>Favorite drink</dt>
        <dd>Tea</dd>
      </dl> -->
    </div>
  </div>
</template>
<script>
export default {
  name: 'AboutGroom'
}
</script>

<style>
.groom .image {
  background: url('~assets/sara.png');
  background-position: top -140px center;
  background-size: 160%;
}
ul.profile-details {
  list-style: none;
  font-family: lato;
  color: #444;
  padding-left: 0;
  text-align: center;
}

ul.profile-details li {
  margin: 10px 0px;
  font-style: oblique;
  font-family: cursive;
  font-weight: bold;
  color: #555;
}
</style>
