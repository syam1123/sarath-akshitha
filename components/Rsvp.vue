<template>
  <div class="rsvp">
    <div class="top">
    </div>
    <div class="form">
      <div class ="info">
      <h1>RSVP</h1>
      <h2>for the wedding of</h2>
      <h1>Sarath & Akshitha</h1>
        <p class= "line">________________________________________</p>
        <h2>The Details</h2>
        <p>Thursday, Sept 05, 2019</p>
        <p>11:00 AM</p>
        <br>
        <h2>Ceremony & Reception</h2>
        <p>Thiruvanvandoor Mahavishnu Temple</p>
        <p>Chengannur - Thiruvalla</p>
            <p class= "line">________________________________________</p>
      <input type="text" placeholder="Name">
      <input type="number" placeholder="# of Guests">
      </div>
      <button class ="accept" @click="acceptRsvp">Accept</button>
      <button class ="regret">Cancel</button>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Rsvp',
  methods: {
    acceptRsvp () {
      alert('Accepted')
    }
  }
}
</script>
<style>
  .rsvp{
    height: auto;
    padding-bottom: 2em;
    min-height: 100vh;
    width: 100%;
    background-color: #BDC3C7;
    background-image: url(https://cdn.pixabay.com/photo/2013/07/13/12/32/grass-159804_960_720.png);
    background-position: bottom -152px left;
    background-repeat: repeat-x;
  }
  .top {
    background-color: #264356;
    height: 200px;
    margin:0;
    padding:0;
    box-shadow: 2px 2px 4px rgb(0, 0, 0, .25);
  }

  .form {
    height: 590px;
    width: 400px;
    max-width: 95%;
    background-color: #fff;
    margin: -110px auto;
    border-radius: 10px;
    color: #666;
    padding: 0px 0px;
    box-shadow: 2px 2px 4px rgb(0, 0, 0, .25);
  }

  .info {
    padding: 10px;
  }

  h1, h2, p {
    text-align: center;
    padding: 0px;
    margin: 5px 5px;
  }

  h2 {
    font-weight: 100;
  }

  p.line {
    margin: 0px auto 20px auto;
    color: #999;
    max-width: 100%;
    margin: auto;
    overflow: hidden;
  }

  .form input {
    font-size: 15px;
    color: #666;
    padding: 6px;
    margin: 25px auto 20px;
    display: block;
    width: 75%;
  }

  input:focus {
    outline: 0;
  }

  .button button {
    display: inline-block;
    width: 400px;
  }
  button {
    color: #666;
    background-color: #264356;
    color: white;
    border: none;
    font-size: 16px;
    font-weight: 600;
    padding: 15px 32px;
    width: 50%;
    margin: 31px auto 0px auto;
    float:left;
    cursor: pointer;
  }

  button.accept {
    border-radius: 0px 0px 0px 10px;
    border-right: solid 1px #173040;
  }

  button.regret {
    border-radius: 0px 0px 10px 0px;
  }

  button:hover {
    background-color: #173040;
    transition: .5s;
  }

  button:focus {
    outline: 0;
  }

  @media screen and (max-width: 500px){
    .rsvp{
      min-height: 750px;
      background-position: bottom -52px left;
      background-repeat: repeat-x;
      background-size: 300px;
    }
  }
</style>
