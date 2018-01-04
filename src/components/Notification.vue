<template lang="pug">
.notifications.notification-layer(@mouseenter="enter", @mouseleave="leave")
  transition-group(name="list-fade", tag="div")
    .alert.notifications-alert(:class="['alert-' + item.type]", v-for="(item, index) in notifications", :key="index" v-show="item.visible")
      a.close(@click="item.visible = false") &times;
      .fa(:class="['fa-' + item.icon]")
      |  {{item.text}}
</template>

<script>
const notifications = []
const Notification = {
  install (Vue) {
    const iconMap = {
      success: 'check',
      info: 'bullhorn',
      warning: 'warning',
      danger: 'remove'
    }
    function notify (text, type, time = 3000, fixed = false, sticky = false) {
      const item = {
        icon: iconMap[type],
        text,
        type,
        time,
        fixed,
        sticky,
        visible: true
      }

      if (sticky) {
        notifications.splice(0, 0, item)
      } else {
        notifications.push(item)
      }

      item.close = function () {
        window.clearTimeout(item.timer)
        item.visible = false
        // remove item after 10s
        window.setTimeout(() => {
          const index = notifications.indexOf(item)
          if (index > -1) {
            notifications.splice(index, 1)
          }
        }, 10000)
      }
      if (!fixed) {
        item.timer = window.setTimeout(item.close, item.time)
      }

      return item.close
    }
    let temp = {}
    Vue.notification = Vue.prototype.$notification = {
      time (time) {
        temp.time = time
        return this
      },
      fixed () {
        temp.fixed = true
        return this
      },
      sticky () {
        temp.sticky = true
        return this
      },
      success (text = 'Success') {
        const close = notify(text, 'success', temp.time, temp.fixed, temp.sticky)
        temp = {}
        return close
      },
      info (text) {
        const close = notify(text, 'info', temp.time, temp.fixed, temp.sticky)
        temp = {}
        return close
      },
      warning (text = 'Warning') {
        const close = notify(text, 'warning', temp.time, temp.fixed, temp.sticky)
        temp = {}
        return close
      },
      error (text = 'Error') {
        const close = notify(text, 'danger', temp.time, temp.fixed, temp.sticky)
        temp = {}
        return close
      },
      notify
    }
  }
}

export default {
  data: function () {
    return {
      notifications
    }
  },
  methods: {
    enter () {
      this.notifications.filter(item => item.visible && !item.fixed).forEach(item => {
        window.clearTimeout(item.timer)
      })
    },
    leave () {
      this.notifications.filter(item => item.visible && !item.fixed).forEach(item => {
        item.timer = window.setTimeout(item.close, item.time)
      })
    }
  },
  created() {
    this.$root.constructor.use(Notification)
  }
}

</script>

<style lang="scss">
.notifications{
  position: fixed;
  width: 300px;
  top: 30px;
  right: 20px;
  overflow-x: hidden;
}
.notifications-alert{
  margin: 10px 0;
}
.list-fade-enter-active, .list-fade-leave-active {
  transition: all .5s;
}
.list-fade-enter, .list-fade-leave-active {
  opacity: 0;
}
</style>
