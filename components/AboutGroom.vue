<template>
  <div class="about-container groom">
    <div class="about-section">
      <div class="image-container">
        <div class="image" />
      </div>
      <h1>Sarath</h1>
      <h2>(Five things about him by her)</h2>
      <ul class="profile-details">
        <li>"Proud of him following his passion"</li>
        <li>"Can advise for hours and says he doesn't like advice"</li>
        <li>"Until I met him, bugs were just insects"</li>
        <li>"Amma mon (Mom's child)"</li>
        <li>"Never get's bored of listening to him"</li>
      </ul>
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
