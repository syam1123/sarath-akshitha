<template>
  <div class="about-container bride">
    <div class="about-section">
      <div class="image-container">
        <div class="image" />
      </div>
      <h1>Akshitha</h1>
      <dl class="profile">
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
.about-container{
  /* background: orange; */
  height: 100vh;
}
.image-container {
  width: 100%;
  height: 350px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.groom .image-container {
  background: url(https://www.onlygfx.com/wp-content/uploads/2018/01/green-paint-brush-stroke-8.png) no-repeat;
  background-size: contain;
  background-position: center;
}
.bride .image-container {
  background: url(https://img.freepik.com/free-photo/textured-blue-paint-brushstroke-white_23-2147746844.jpg?size=626&ext=jpg) no-repeat;
  background-size: contain;
  background-position: center;
}
.image-container .image {
  width: 250px;
  height: 250px;
  border-radius: 100%;
}
.bride .image {
  background: url(https://bit.ly/2xMUrMz);
  box-shadow: 0px 0px 16px 3px #63f1f7 inset;
  background-position: top 0px center;
  background-size: 100%;
}
.about-section h1{
  text-align: center;
  font-size: 40px;
  margin-top: 10px;
  font-family: fantasy;
}
.profile{
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  padding: 1em;
  margin: auto;
  margin-bottom: 2em;
  max-width: 500px;
}
.profile dt {
  width: 45%;
  display: block;
}
.profile dd {
  width: 50%;
  margin: 0.3em 0em;
  font-weight: 500;
}
</style>
