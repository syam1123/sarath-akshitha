<template>
  <div class="about-container groom">
    <div class="about-section">
      <div class="image-container">
        <div class="image" />
      </div>
      <h1>Sarath</h1>
      <dl class="profile">
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
      </dl>
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
</style>
