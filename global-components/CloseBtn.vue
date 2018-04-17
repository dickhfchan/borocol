<template lang="pug">
.close-btn(@click="$emit('click', $event)")
  Icon.close-btn-icon(name="close-md")
</template>

<script>
export default {
  // components: {},
  // data() {
  //   return {}
  // },
  // computed: {},
  // watch: {},
  // methods: {},
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
.close-btn{
  position: absolute;
  right: .5em;
  top: .5em;
  cursor: pointer;
  $side: 20px;
  width: $side;
  height: $side;
  line-height: $side;
  text-align: center;
  border-radius: 100%;
  background-color: rgba(119, 119, 119, 0.3);
  color: rgb(255, 255, 255);
  &:hover{
    color: #eef;
    background-color: rgba(119, 119, 119, 0.9);
  }
}
.close-btn-icon{
  font-size: 12px;
}
</style>
