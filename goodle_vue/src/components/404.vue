<template>
  <div class="not-found">
    <img src="../assets/notFound.png">
    <h1>对不住，兄弟，这页没了</h1>
    <h3>试试<router-link to="/Home">去首页</router-link></h3>
  </div>
</template>

<script>
export default {
  name: 'notFound'
}
</script>

<style scoped>
.not-found {
  text-align: center;
}
.not-found img{
  width: 500px;
  top: 50px;
}
</style>
