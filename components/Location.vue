<template>
  <div class="location-container">
    <h2>Wedding</h2>
    <h1>THURSDAY, 05 SEPT 2019</h1>
    <p>At</p>
    <h3>Thiruvanvandoor Mahavishnu Temple</h3>
    <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d15747.55170260684!2d76.5801186!3d9.3431847!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xe5179c90f8b23cd!2sThiruvanvandoor+Mahavishnu+Temple!5e0!3m2!1sen!2sde!4v1563654214229!5m2!1sen!2sde" height="300" frameborder="0" style="border:0" allowfullscreen></iframe>
  </div>
</template>
<script>
export default {
  name: 'Location'
}
</script>

<style>
  .location-container {
    background: #193076;
    height: auto;
    color: white;
    text-align: center;
    padding-top: 4em;
    font-family: lato;
  }

  .location-container h2{
    letter-spacing: 0.9px;
  }

  .location-container iframe {
    width: 100vw;
    margin-top: 2em;
    margin-bottom: -4px;
  }

  .location-container h1{
    font-family: monospace;
    margin: 0.5em;
    font-size: 3em;
    background: -webkit-linear-gradient(right, #ffa710, #f9ff31, #f936f7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .location-container h3{
    font-size: 1.7em;
    margin-top: .5em;
    color: #f1efef;
  }
</style>
