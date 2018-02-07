<template lang="pug">
include ../common.pug
.Message
  .container
    .title-bar
      .title Message
      .search.input-with-icon
        +inputLg(placeholder="Search school name or conversation")
        span.icon.icon-search
    .content-card
      .left
        .name-list
          .item.unread
            img.avatar(src="https://picsum.photos/40/40?image=399")
            .name Admin
            span.unread-icon.icon.icon-circle
            span.unread-text Unread
          .item.unread
            img.avatar(src="https://picsum.photos/40/40?image=400")
            .name Cape Town English Language Institute
            span.unread-icon.icon.icon-circle
            span.unread-text Unread
          .item
            img.avatar(src="https://picsum.photos/40/40?image=401")
            .name Bay Learning Academy
          .item
            img.avatar(src="https://picsum.photos/40/40?image=402")
            .name Avenue English
          .item
            img.avatar(src="https://picsum.photos/40/40?image=403")
            .name The Burlington School of English
      .right
        .message-list
          .item.other
            img.avatar(src="https://picsum.photos/40/40?image=399")
            .text-area
              .arrow
              .name Admin
              .content Customer Advocate
          .item.self
            .text-area
              .arrow
              .name Emma
              .content Hey There!
            img.avatar(src="https://picsum.photos/40/40?image=398")
          .item.other
            img.avatar(src="https://picsum.photos/40/40?image=399")
            .text-area
              .arrow
              .name Admin
              .content Hey! I hope you are doing great. How may I help?
          .clearfix
        form.message-form
          +textarea(rows="6" placeholder="Type your message here...")
          button.send-btn.btn.btn-primary.btn-md.pull-right Send
          .clearfix
</template>

<script>
export default {
  components: {},
  data() {
    return {
    }
  },
  // computed: {},
  // watch: {},
  // methods: {},
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
@import "~@/assets/css/global.scss";
.Message{
  // common
  .avatar{
    $side: 40px;
    width: $side;
    height: $side;
  }
  //
  background-image: url(~@/assets/img/message-bg.jpg);
  background-position: center;
  background-size: cover;
  .container{
    width: 1400px;
    padding: 0;
  }
  .title-bar{
    display: flex;
    justify-content: space-between;
    margin-top: 100px;
  }
  .search{
    width: 500px;
  }
  .title {
    font-size: 70px;
    font-weight: 300;
  }
  .content-card{
    border-top: 30px solid #000;
    border-radius: 0;
    margin-top: 30px;
    padding: 0;
    height: 700px;
    display: flex;
  }
  .left{
    width: 450px;
    background: #f3f2f0;
    padding: 30px 20px;
    height: 100%;
    overflow: auto;
  }
  .name-list{
    .item{
      display: flex;
      align-items: center;
      padding: 8px;
      border-bottom: 1px solid $bd1;
      .avatar{
        margin-right: 1em;
      }
      .name{
        margin-right: .5em;
      }
      .unread-icon{
        color: $bg2;
        margin-right: .5em;
        font-size: 10px;
      }
      .unread-text{
        font-style: italic;
        font-size: 12px;
      }
      &.unread{
        .name{
          font-weight: bold;
        }
      }
    }
  }
  .right{
    flex-grow: 1;
    padding: 20px 90px;
    display: flex;
    flex-direction: column;
    .avatar{
      border-radius: 200px;
    }
  }
  .message-list{
    flex-grow: 1;
    overflow: auto;
    .item{
      display: flex;
      margin-bottom: 50px;
      &.other{
        .text-area{
          margin-left: 1em;
          background-color: rgb(243, 242, 240);
        }
        .arrow{
          position: absolute;
          width: 0;
          height: 0;
          border-style: solid;
          border-width: 5px 10px 5px 0;
          border-color: transparent #f3f2f0 transparent transparent;
          top: 15px;
          right: 100%;
        }
      }
      &.self{
        justify-content: flex-end;
        .text-area{
          margin-right: 1em;
          background: #e1f0f1;
        }
        .arrow{
          position: absolute;
          width: 0;
          height: 0;
          border-style: solid;
          border-width: 5px 0 5px 10px;
          border-color: transparent transparent transparent #e1f0f1;
          top: 15px;
          left: 100%;
        }
      }
    }
    .text-area{
      padding: 10px;
      width: 420px;
      border-radius: 3px;
      position: relative;
    }
    .name{
      font-weight: bold;
    }
    .content{
      margin-top: 5px;
      min-height: 30px;
    }
  }
  .message-form {
    margin-top: 16px;
    padding-top: 16px;
    border-top: 1px solid $bd1;
  }
  .send-btn{
    margin-top: 16px;
  }
}
</style>
