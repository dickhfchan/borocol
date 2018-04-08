<template lang="pug" functional>
.has-read-more
  slot
  .read-more
    Icon(name="search")
    span.mls READ MORE
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
.has-read-more {
  position: relative;
  display: block;

  .read-more {
    width: 100%;
    height: 100%;
    display: none;
    position: absolute;
    top: 0;
    left: 0;
    align-items: center;
    justify-content: center;
    color: #fff;
    font-size: 21px;
    font-weight: 500;

    .icon-search {
      font-size: 18px;
      position: relative;
      top: 1px;
    }
  }

  &:hover {
    .read-more {
      display: flex;
      background-color: rgba(125, 125, 125, 0.6);
      color: #fff;
    }
  }
}

</style>
