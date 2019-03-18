<template>
  <div class="not-found">
    <div class="page-body">
      <el-row :gutter="10">
        <el-col :xs="2" :sm="8" :md="8" :lg="8" :xl="9">
          <div class="grid-content"></div>
        </el-col>
        <el-col :xs="20" :sm="8" :md="8" :lg="8" :xl="6">
          <div>
            <img src="../assets/notFound.png">
            <!--<h1>对不住，兄弟，这页没了</h1>-->
            <h3>试试<router-link to="/Home">去首页</router-link></h3>
          </div>
        </el-col>
      </el-row>
    </div>
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
  width: 100%;
  top: 50px;
}
.page-body {
  padding-top: 60px;
}
.grid-content {
  min-height: 36px;
}
</style>
