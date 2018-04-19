<template lang="pug">
el-input.phone-input(v-model="value2")
  el-dropdown(trigger="click" slot="prepend" ref="dropdown")
    span.el-dropdown-link(:title="selectedCountry ? selectedCountry.name : null")
      | {{areaCode || 'area'}}
      i.el-icon-arrow-down.el-icon--right
    el-dropdown-menu.phone-input__country-dropdown(slot="dropdown")
      .pas
        el-input(v-model="search" placeholder="Search" size="small")
      .phone-input__country-list
        .phone-input__country-item(v-for="item in filteredCountries" @click="selectCountry(item)") {{item.name}} {{item.area_code}}
</template>

<script>
import countries from '@/plugins/countries.json'
import valueDetails from './valueDetails'

export default {
  mixins: [valueDetails],
  props: {
    value: {},
  },
  components: {},
  data() {
    return {
      countries,
      search: null,
      areaCode: '',
      value2: '',
    }
  },
  computed: {
    countriesLowerCase() {
      return this.countries.map(v => ({str: v.name.toLowerCase() + v.area_code, data: v}))
    },
    filteredCountries() {
      if (!this.search) {
        return this.countries
      }
      const s = this.search.toLowerCase()
      const r = []
      this.countriesLowerCase.forEach(({str, data}) => {
        if (str.indexOf(s) !== -1) {
          r.push(data)
        }
      })
      return r
    },
    value3() {
      return this.areaCode + ' ' + this.value2
    },
    selectedCountry() {
      const ac = this.areaCode
      if (!ac) {
        return null
      } else {
        return this.countries.find(v => v.area_code === ac)
      }
    },
  },
  watch: {
    value3(val, oldVal) {
      if (val !== oldVal) {
        this.setValue(val)
      }
    },
  },
  methods: {
    selectCountry(item) {
      this.areaCode = item.area_code
      this.$refs.dropdown.hide()
    },
    getValueDetails(value) {
      if (!value) {
        this.areaCode = ''
        this.value2 = ''
      } else {
        [this.areaCode, this.value2] = value.split(' ')
      }
    },
  },
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
.phone-input{
  .el-input-group__prepend{
    padding: 0;
  }
  .el-dropdown-link{
    display: block;
    padding: 10px;
  }
}
.phone-input__country-dropdown{
  padding: 0;
}
.phone-input__country-list{
  max-height: 300px;
  overflow: auto;
}
.phone-input__country-item{
  padding: 3px 5px;
  cursor: pointer;
  &:hover{
    background: #ececec;
  }
}
</style>
